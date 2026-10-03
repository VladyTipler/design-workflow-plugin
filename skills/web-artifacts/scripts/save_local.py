#!/usr/bin/env python3
"""Save a conservative single-file offline prototype; never upload or start a server.

This is a contract check for generated prototypes, not a security sandbox for untrusted JS.
Only --open explicitly asks the default browser to open the resulting file URL.
"""
import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
import webbrowser


class OfflineHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.problems = []
        self.viewport = False
        self.html = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        self.html |= tag == 'html'
        self.viewport |= tag == 'meta' and values.get('name', '').lower() == 'viewport'
        if tag == 'script' and values.get('type', '').lower() == 'module':
            self.problems.append('Use a prebuilt classic script instead of runtime modules.')
        if tag in ('iframe', 'object', 'embed', 'base'):
            self.problems.append(f'Unsupported single-file resource element: {tag}.')
        for attr in ('src', 'srcset', 'poster', 'data', 'action', 'formaction'):
            value = values.get(attr, '')
            if value and not value.startswith(('data:', '#')):
                self.problems.append(f'Embed {tag}[{attr}] instead of loading {value}.')
        if tag in ('image', 'use', 'feimage'):
            for attr in ('href', 'xlink:href'):
                value = values.get(attr, '')
                if value and not value.startswith(('data:', '#')):
                    self.problems.append('Embed SVG resource references before delivery.')
        if tag == 'link' and values.get('href', '') and not values['href'].startswith('data:'):
            self.problems.append('Inline CSS/fonts; external link resources are unsupported.')
        if tag == 'meta' and values.get('http-equiv', '').lower() == 'refresh':
            self.problems.append('Automatic navigation is unsupported.')


def inspect_html(content):
    parser = OfflineHTML()
    parser.feed(content)
    if not parser.html:
        parser.problems.append('An html element is required.')
    if not parser.viewport:
        parser.problems.append('A mobile viewport meta element is required.')
    if re.search(r'\b(?:fetch|import)\s*\(|\b(?:XMLHttpRequest|WebSocket|EventSource)\b|\bsendBeacon\s*\(', content):
        parser.problems.append('Runtime fetch/import/network APIs violate the offline contract.')
    if re.search(r'@import\b', content, re.I):
        parser.problems.append('Inline CSS imports before delivery.')
    for match in re.finditer(r'url\(\s*[\"\']?([^\"\')\s]+)', content, re.I):
        if not match.group(1).startswith(('data:', '#')):
            parser.problems.append('Embed CSS URL resources before delivery.')
    return sorted(set(parser.problems))


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument('--input', type=Path, required=True, help='Prepared single-file HTML')
    args.add_argument('--output', type=Path, required=True, help='User-selected output HTML path')
    args.add_argument('--overwrite', action='store_true', help='Explicitly replace the selected output')
    args.add_argument('--open', action='store_true', help='Open file URL in the default browser')
    options = args.parse_args()
    output = options.output.resolve()
    if output.exists() and not options.overwrite:
        args.error('Output exists; choose another path or explicitly authorize --overwrite.')
    if output.suffix.lower() != '.html':
        args.error('Output must have the .html extension.')
    content = options.input.read_text(encoding='utf-8-sig')
    problems = inspect_html(content)
    if problems:
        args.error('\n'.join(problems))
    output.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive create protects against another process creating the output after the check.
    with output.open('w' if options.overwrite else 'x', encoding='utf-8', newline='\n') as handle:
        handle.write(content)
    print(output.as_uri())
    if options.open and not webbrowser.open(output.as_uri()):
        print('Browser did not accept the request; open the printed file URL manually.')


if __name__ == '__main__':
    main()
