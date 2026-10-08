#!/usr/bin/env python3
import hashlib
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def package_file(path):
    rel = path.relative_to(ROOT)
    return path.is_file() and not any(x in {'.git','.scar','__pycache__','artifacts'} for x in rel.parts) and path.suffix!='.pyc' and path.name not in {'.design-workflow.json','.env'} and not path.name.startswith('.env.')
EXCLUDED = {'FILE_MANIFEST.json'}
TEXT_SUFFIXES = {'.md','.json','.csv','.py','.html','.sh','.txt'}
# Generated reference index is not an input to its own index.
references = {}
for file in sorted(ROOT.rglob('*')):
    if not package_file(file) or file.name in EXCLUDED | {'EXTERNAL_REFERENCES.json'}:
        continue
    if file.suffix not in TEXT_SUFFIXES:
        continue
    for line, text in enumerate(file.read_text(encoding='utf-8').splitlines(), 1):
        for url in re.findall(r'https?://[^\s<>\"\'\x60,]+', text):
            url = url.rstrip(').;]')
            references.setdefault(url, set()).add((file.relative_to(ROOT).as_posix(),line))
external = {'description':'Literal HTTP(S) references, not runtime dependencies. Occurrences are package-relative.',
            'count':len(references), 'references':[
                {'url':url,'occurrences':[{'path':path,'line':line} for path,line in sorted(locations)]}
                for url,locations in sorted(references.items())]}
(ROOT/'EXTERNAL_REFERENCES.json').write_text(json.dumps(external,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
originals = {x['path']:x['sourceSha256'] for x in json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())['files']}
entries = []
for file in sorted(ROOT.rglob('*')):
    if not package_file(file) or file.name in EXCLUDED:
        continue
    path=file.relative_to(ROOT).as_posix()
    digest=hashlib.sha256(file.read_bytes()).hexdigest()
    entry={'path':path,'bytes':file.stat().st_size,'sha256':digest,
           'status':'unchanged' if originals.get(path)==digest else 'adapted' if path in originals else 'added'}
    if path in originals:entry['sourceSha256']=originals[path]
    entries.append(entry)
skills={p.name:sum(1 for x in entries if x['path'].startswith('skills/'+p.name+'/'))
        for p in sorted((ROOT/'skills').iterdir()) if p.is_dir()}
manifest={'description':'Complete package snapshot. This manifest itself is excluded from hashes to avoid self-reference.',
          'totalFilesIncludingManifest':len(entries)+1,'originalResourceCount':len(originals),
          'skillFileCounts':skills,'externalReferenceCount':len(references),'files':entries}
(ROOT/'FILE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Manifest: {len(entries)+1} files; {len(originals)} original resources; {len(references)} external references.')
