# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Setuptools-based packaging with `setup.py` using `find_packages()`
- Entry point `social-analyzer` -> `app:main` for CLI usage
- `setup.cfg` with license_files metadata
- `MANIFEST.in` to include README.rst, README.md, LICENSE, and data files
- Pinned dependency ranges in `requirements.txt` matching Python >=3.9
- CI workflow `.github/workflows/ci.yml` for pytest on Python 3.10 and 3.11
- Optional ruff linting in CI
- Improved `Dockerfile` for python:3.11-slim with lxml system dependencies
- `docker-compose.override.yml` for local development with port 8000 mapping and volume mount
- `start.sh` entrypoint script using gunicorn if available, otherwise python app.py
- `tests/test_basic.py` with basic tests importing SocialAnalyzer without network calls
- `tox.ini` to run pytest in py311 environment
- `PRIVACY_AND_COMPLIANCE.md` with dataset descriptions and usage recommendations
- This CHANGELOG.md file to track changes
- `main()` function wrapper in `app.py` for entry point compatibility

### Changed
- Updated `requirements.txt` with canonical pip package names and version ranges
- Modified `setup.py` to use modern setuptools with `find_packages()` and proper entry points
- Set `python_requires>=3.9` in setup.py
- Updated Dockerfile to use Python 3.11 slim base image instead of Node.js
- Exposed port 8000 instead of 9005 in Docker configuration

### Fixed
- Ensured app.py does not perform network/IO at import time
- Tests now only import class definitions to avoid network calls

## [0.45] - Previous Release

### Note
This version represents the state of the project before the packaging and CI improvements.
