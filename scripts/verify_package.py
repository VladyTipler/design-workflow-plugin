#!/usr/bin/env python3
import json
import hashlib
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def package_file(path):
    rel = path.relative_to(ROOT)
    return path.is_file() and not any(x in {'.git','.scar','__pycache__','artifacts'} for x in rel.parts) and path.suffix!='.pyc' and path.name not in {'.design-workflow.json','.env'} and not path.name.startswith('.env.')
EXPECTED = {'design-workflow','agent-browser','ux-heuristics','ux-principles',
            'ui-ux-pro-max','design-system-docs','web-artifacts','frontend-design'}
problems = []
actual = {p.name for p in (ROOT/'skills').iterdir() if p.is_dir()}
if actual != EXPECTED: problems.append(f'Skill set differs: {actual ^ EXPECTED}')
for name in sorted(EXPECTED):
    file = ROOT/'skills'/name/'SKILL.md'
    text = file.read_text(encoding='utf-8')
    front = text.split('---',2)[1] if text.startswith('---') else ''
    match = re.search(r'^name:\s*[\"\']?([a-z0-9-]+)',front,re.M)
    if not match or match.group(1)!=name: problems.append(f'{file}: name mismatch')
    if not re.search(r'^description:\s*\S',front,re.M): problems.append(f'{file}: missing description')
    for resource in re.findall(r'(?<![\w/])(?:references|templates|scripts)/[A-Za-z0-9_.-]+\.(?:md|py|html|sh)',text):
        if not (file.parent/resource).is_file(): problems.append(f'{name}: missing {resource}')
    for sibling in re.findall(r'\.\./([a-z0-9-]+)/SKILL\.md',text):
        if sibling not in EXPECTED: problems.append(f'{name}: missing sibling {sibling}')
for file in (p for p in ROOT.rglob('*.md') if package_file(p)):
    text=file.read_text(encoding='utf-8')
    for link in re.findall(r'\[[^\]]+\]\(([^\s)]+)\)',text):
        if link.startswith(('http:','https:','mailto:','#')) or '<' in link: continue
        target=(file.parent/link.split('#',1)[0]).resolve()
        if not target.exists(): problems.append(f'{file.relative_to(ROOT)}: broken link {link}')
for rel in ['plugin.json','.codex-plugin/plugin.json','.claude-plugin/plugin.json','.zcode-plugin/plugin.json']:
    data=json.loads((ROOT/rel).read_text(encoding='utf-8'))
    if data.get('name')!='design-workflow': problems.append(f'{rel}: wrong plugin name')
for rel in ['marketplace.json','.claude-plugin/marketplace.json','.agents/plugins/marketplace.json']:
    data=json.loads((ROOT/rel).read_text(encoding='utf-8'))
    if data.get('name')!='design-workflow-local' or len(data.get('plugins',[]))!=1:
        problems.append(f'{rel}: wrong marketplace identity')
    for entry in data.get('plugins',[]):
        source=entry.get('source')
        path=source.get('path') if isinstance(source,dict) else source
        if entry.get('name')!='design-workflow' or (ROOT/path).resolve()!=ROOT:
            problems.append(f'{rel}: wrong local source')
for entry in json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())['files']:
    if not (ROOT/entry['path']).is_file(): problems.append(f'Missing original resource: {entry["path"]}')
# User identifiers, mandatory integrations, and machine-specific paths must not ship.
private=re.compile(r'kanev\.space|canon-jr|vlad-signature|Job Radar|graphiti|wiki-query|data-first-design|[A-Z]:[\\/]Users[\\/]',re.I)
for file in ROOT.rglob('*'):
    if file != Path(__file__).resolve() and package_file(file) and file.suffix in {'.md','.py','.json','.html','.sh','.csv'}:
        if private.search(file.read_text(encoding='utf-8')): problems.append(f'{file.relative_to(ROOT)}: nonportable/private token')
snapshot=json.loads((ROOT/'FILE_MANIFEST.json').read_text(encoding='utf-8'))
expected={entry['path'] for entry in snapshot['files']}
actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if package_file(p) and p.name!='FILE_MANIFEST.json'}
if actual!=expected: problems.append(f'Manifest file set differs: {actual ^ expected}')
for entry in snapshot['files']:
    file=ROOT/entry['path']
    if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest()!=entry['sha256']:
        problems.append(f'Manifest hash mismatch: {entry["path"]}')
if problems:
    print('\n'.join(problems))
    raise SystemExit(1)
files=[p for p in ROOT.rglob('*') if package_file(p)]
print(f'PASS: {len(EXPECTED)} skills, resources, markdown links, source coverage, manifests, anonymization; {len(files)} files.')
