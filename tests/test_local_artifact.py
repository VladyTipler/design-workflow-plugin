import importlib.util
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/web-artifacts/scripts/save_local.py'


class LocalArtifactTests(unittest.TestCase):
    def run_save(self, html, output, *args):
        source = output.parent / 'input.html'
        source.write_text(html, encoding='utf-8')
        return subprocess.run([sys.executable, str(SCRIPT), '--input', str(source),
                               '--output', str(output), *args], capture_output=True, text=True)

    def test_self_contained_html_is_saved_and_returns_file_url(self):
        with tempfile.TemporaryDirectory() as directory:
            output = pathlib.Path(directory) / 'prototype.html'
            result = self.run_save('<!doctype html><html><head><meta name="viewport" '
                                   'content="width=device-width,initial-scale=1"></head>'
                                   '<body><button>Choose</button><script>const n=1;</script>'
                                   '</body></html>', output)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(output.resolve().as_uri(), result.stdout)
            self.assertTrue(output.exists())

    def test_network_resources_and_module_imports_are_rejected(self):
        snippets = ['<script src="https://cdn.example.com/a.js"></script>',
                    '<script type="module">import x from "./x.js"</script>',
                    '<script>fetch("./data.json")</script>',
                    '<style>body{background:url(https://example.com/a.png)}</style>',
                    '<img srcset="https://example.com/a.png 2x">',
                    '<iframe src="https://example.com"></iframe>',
                    '<svg><image href="https://example.com/a.png"/></svg>',
                    '<svg><use xlink:href="https://example.com/a.svg#icon"/></svg>']
        for snippet in snippets:
            with self.subTest(snippet=snippet), tempfile.TemporaryDirectory() as directory:
                output = pathlib.Path(directory) / 'prototype.html'
                result = self.run_save('<html><head><meta name="viewport" content="width=device-width">'
                                       '</head><body>'+snippet+'</body></html>', output)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(output.exists())

    def test_existing_output_is_preserved_without_explicit_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            output = pathlib.Path(directory) / 'prototype.html'
            output.write_text('keep', encoding='utf-8')
            result = self.run_save('<html></html>', output)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(output.read_text(), 'keep')

    def test_external_navigation_link_is_not_a_runtime_dependency(self):
        with tempfile.TemporaryDirectory() as directory:
            output = pathlib.Path(directory) / 'prototype.html'
            result = self.run_save('<html><head><meta name="viewport" content="width=device-width">'
                                   '</head><body><a href="https://example.com">Source</a>'
                                   '</body></html>', output)
            self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
