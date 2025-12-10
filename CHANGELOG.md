# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Modern packaging setup with setuptools using py_modules and console entry points
- setup.cfg with license_files metadata
- MANIFEST.in for proper distribution file inclusion (README.rst, README.md, LICENSE, data/*)
- CI/CD workflow (.github/workflows/ci.yml) for automated testing on Python 3.10 and 3.11
  - Includes optional ruff linting
  - Installs system dependencies for lxml
  - Proper GITHUB_TOKEN permissions
- Comprehensive test suite (tests/test_basic.py) with import and initialization tests
  - Tests avoid network calls for fast, reliable CI
- tox.ini for automated testing across Python 3.9, 3.10, and 3.11
- Docker improvements:
  - Updated Dockerfile to use python:3.11-slim base image
  - Added proper system dependencies for lxml (libxml2-dev, libxslt1-dev)
  - docker-compose.override.yml for local development with volume mounting
  - start.sh entrypoint script for flexible execution
- Enhanced PRIVACY_AND_COMPLIANCE.md with:
  - Detailed descriptions of all datasets
  - Privacy principles and compliance recommendations
  - Special notes about Thai law enforcement data files
  - Legal disclaimers and usage guidelines
- CHANGELOG.md for tracking project changes
- main() function in app.py for proper entry point support

### Changed
- Updated requirements.txt with pinned dependency versions and canonical package names
  - beautifulsoup4 (was BeautifulSoup4)
  - Added version ranges for all dependencies
- Improved Dockerfile from node-based to Python 3.11-slim for Python-focused workflow
- Updated setup.py to use py_modules=['app'] for single-module application
- Set python_requires to >=3.9 for modern Python version support
- Exposed port 8000 in Docker configuration (previously 9005)
- Updated .gitignore to exclude Python build artifacts

### Fixed
- Package distribution issues by adding proper MANIFEST.in
- Test suite no longer requires sys.path manipulation
- GitHub Actions workflow now has proper permissions configuration
- start.sh entrypoint simplified to work with Python CLI app

### Security
- Updated dependencies to include security ranges
- Added proper system dependency installation in Docker
- Improved container security with slim base image
- Fixed missing GITHUB_TOKEN permissions in CI workflow

## [0.45] - Previous Release
- Initial version with basic social media analysis functionality
