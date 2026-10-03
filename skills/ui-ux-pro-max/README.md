# UI/UX Pro Max — local data bundle

Use Python 3 to run scripts/search.py by its actual installed path. It uses only the Python standard library and bundled data; it does not need a server or package installation.

Examples:
    python "<skill-directory>/scripts/search.py" "task dashboard" --design-system
    python "<skill-directory>/scripts/search.py" "visible focus" --domain ux
    python "<skill-directory>/scripts/search.py" "chip overflow" --stack html-tailwind

scripts/validate_data.py validates the local data contract. Runtime modules are core.py, search.py, design_system.py and reasoning_contract.py.

The complete inherited data, references, tests and fixtures are preserved. Four maintenance suites depend on scripts from their original upstream checkout; those absent tools are explicitly listed in ../../docs/validation.md. Do not interpret this portable bundle as a complete upstream catalog-maintenance repository.

License/source certainty is recorded in ../../THIRD_PARTY_NOTICES.md; do not assume all catalog data shares one license.
