# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Python package structure with proper setuptools configuration
- `social_analyzer` package with `__init__.py` exposing `SocialAnalyzer` class
- Console script entry point `social-analyzer` command
- `setup.py` with `find_packages()` and versioned dependencies
- `setup.cfg` with license metadata
- `MANIFEST.in` for including README, LICENSE, and data files
- `requirements.txt` with pinned dependency versions
- GitHub Actions CI workflow (`.github/workflows/ci.yml`)
  - Matrix testing for Python 3.10 and 3.11
  - Automated pytest execution
  - Optional ruff linting
- Python-based `Dockerfile.python` for containerized deployments
  - Based on Python 3.11-slim
  - System dependencies for lxml and other packages
  - Port 8000 exposure
- `start.sh` entrypoint script for Docker container
- `docker-compose.override.yml` for local development
- Unit tests in `tests/test_basic.py`
  - Import validation tests
  - Initialization tests
  - Attribute validation tests
- `tox.ini` for test automation
- `PRIVACY_AND_COMPLIANCE.md` documentation
  - Guidance on handling sensitive data
  - Recommendations for production use
  - Compliance considerations
- `CHANGELOG.md` for tracking changes

### Changed
- Updated `setup.py` to use modern setuptools practices
- Improved dependency specifications with version ranges
- Enhanced package metadata and classifiers

### Fixed
- Package installation and distribution issues
- Missing entry point for CLI tool

## [0.45] - Previous Release

### Initial Features
- Social media profile analysis across 300+ websites
- CLI interface for username searches
- Web interface with Node.js/Express
- Multiple detection modes (fast, slow, special)
