# Build and Deployment Guide

## Quick Start

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Run tests:**
   ```bash
   pip install pytest
   pytest tests/ -v
   ```

### Docker

Build and run with Docker Compose:
```bash
docker-compose up --build
```

Access the application at `http://localhost:8000`

### Package Installation

Install the package in development mode:
```bash
pip install -e .
```

Use the CLI:
```bash
social-analyzer --username johndoe --websites youtube
```

## CI/CD

The project now includes automated testing via GitHub Actions:
- Tests run on Python 3.10 and 3.11
- Linting with ruff (optional, continues on error)
- Triggered on push and pull requests to main branch

## Testing

Run tests with tox:
```bash
pip install tox
tox -e py311
```

Or directly with pytest:
```bash
pytest tests/ -v
```

## New Files

- `.github/workflows/ci.yml` - CI configuration
- `tests/test_basic.py` - Basic unit tests
- `tox.ini` - Tox configuration
- `setup.cfg` - Package metadata
- `MANIFEST.in` - Package data files
- `start.sh` - Docker entrypoint script
- `docker-compose.override.yml` - Local development config
- `CHANGELOG.md` - Version history
- `PRIVACY_AND_COMPLIANCE.md` - Data usage guidelines
