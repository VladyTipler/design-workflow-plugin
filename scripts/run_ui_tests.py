#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / 'skills/ui-ux-pro-max/scripts/tests'
# These suites require tools from the original upstream checkout, not runtime files.
UPSTREAM_ONLY = {'test_catalog_refresh', 'test_catalog_summary_line_endings',
                 'test_relevance_evaluator', 'test_skill_script_paths'}
sys.dont_write_bytecode = True
sys.path.insert(0, str(TESTS))
loader = unittest.TestLoader()
suite = unittest.TestSuite()
modules = sorted(p.stem for p in TESTS.glob('test_*.py') if p.stem not in UPSTREAM_ONLY)
for module in modules:
    suite.addTests(loader.loadTestsFromName(module))
print('Portable UI modules: ' + ', '.join(modules))
print('Upstream-only modules excluded: ' + ', '.join(sorted(UPSTREAM_ONLY)))
result = unittest.TextTestRunner(verbosity=1).run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
