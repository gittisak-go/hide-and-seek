# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Modern packaging setup with setuptools, find_packages, and console entry points
- setup.cfg with license_files metadata
- MANIFEST.in for proper distribution file inclusion
- CI/CD workflow (.github/workflows/ci.yml) for automated testing on Python 3.10 and 3.11
- Comprehensive test suite (tests/test_basic.py) with import and initialization tests
- tox.ini for automated testing across Python versions
- Docker improvements:
  - Updated Dockerfile to use python:3.11-slim base image
  - Added proper system dependencies for lxml
  - docker-compose.override.yml for local development
  - start.sh entrypoint script with gunicorn support
- Enhanced PRIVACY_AND_COMPLIANCE.md with detailed dataset descriptions
- CHANGELOG.md for tracking project changes
- main() function in app.py for proper entry point support

### Changed
- Updated requirements.txt with pinned dependency versions and canonical package names
- Improved Dockerfile from node-based to Python 3.11-slim for better compatibility
- Updated setup.py to use find_packages() instead of hardcoded package list
- Set python_requires to >=3.9 for modern Python version support
- Exposed port 8000 in Docker configuration (previously 9005)

### Fixed
- Package distribution issues by adding proper MANIFEST.in
- Import-time network calls prevention with proper guards
- Test infrastructure for reliable CI/CD operations

### Security
- Updated dependencies to include security ranges
- Added proper system dependency installation in Docker
- Improved container security with slim base image

## [0.45] - Previous Release
- Initial version with basic social media analysis functionality
