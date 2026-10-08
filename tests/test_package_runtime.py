import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class PackageRuntimeTests(unittest.TestCase):
    def test_verification_runtime_state_is_not_published_or_hashed(self):
        with tempfile.TemporaryDirectory() as directory:
            copied = pathlib.Path(directory) / 'package with spaces'
            shutil.copytree(ROOT, copied, ignore=shutil.ignore_patterns('.git', '.scar', '__pycache__'))
            runtime = copied / '.scar' / 'sessions' / 'test'
            runtime.mkdir(parents=True)
            (runtime / 'contract.json').write_text(json.dumps({'private': 'C:' + '/Users/test/check'}), encoding='utf-8')
            for script in ('build_manifest.py', 'verify_package.py'):
                result = subprocess.run([sys.executable, '-B', str(copied / 'scripts' / script)],
                                        cwd=directory, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            manifest = json.loads((copied / 'FILE_MANIFEST.json').read_text(encoding='utf-8'))
            self.assertFalse(any(entry['path'].startswith('.scar/') for entry in manifest['files']))
            references = (copied / 'EXTERNAL_REFERENCES.json').read_text(encoding='utf-8')
            self.assertNotIn('contract.json', references)

    def test_published_skill_change_is_detected_after_manifest_generation(self):
        with tempfile.TemporaryDirectory() as directory:
            copied = pathlib.Path(directory) / 'package'
            shutil.copytree(ROOT, copied, ignore=shutil.ignore_patterns('.git', '.scar', '__pycache__'))
            generated = subprocess.run([sys.executable, '-B', str(copied / 'scripts/build_manifest.py')],
                                       capture_output=True, text=True)
            self.assertEqual(generated.returncode, 0, generated.stderr)
            source = copied / 'skills/design-workflow/SKILL.md'
            source.write_text(source.read_text(encoding='utf-8') + '\nChanged source.\n', encoding='utf-8')
            verified = subprocess.run([sys.executable, '-B', str(copied / 'scripts/verify_package.py')],
                                      capture_output=True, text=True)
            self.assertNotEqual(verified.returncode, 0)
            self.assertIn('Manifest hash mismatch: skills/design-workflow/SKILL.md', verified.stdout)
