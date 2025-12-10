# Build, Test, and Deploy Instructions

This document provides instructions for building, testing, and deploying the social-analyzer Python package.

## Prerequisites

- Python 3.9 or higher (3.10 or 3.11 recommended)
- pip package manager
- Docker (optional, for containerized deployment)
- docker-compose (optional, for local development)

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/gittisak-go/hide-and-seek.git
cd hide-and-seek

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

### Using pip (when published)

```bash
pip install social-analyzer
```

## Usage

### Command Line Interface

After installation, you can use the `social-analyzer` command:

```bash
# List all available websites
social-analyzer --list

# Search for a username across all sites (fast mode)
social-analyzer --username johndoe --websites all --mode fast

# Search on specific websites
social-analyzer --username johndoe --websites youtube tiktok tumblr

# Get help
social-analyzer --help
```

### Python API

```python
from social_analyzer import SocialAnalyzer

# Create an analyzer instance
analyzer = SocialAnalyzer(silent=False)

# Initialize the analyzer
analyzer.init_logic()

# Use the analyzer programmatically
# (See app.py for more methods)
```

## Development

### Running Tests

```bash
# Install test dependencies
pip install pytest

# Run tests
pytest tests/ -v

# Run with coverage
pip install pytest-cov
pytest tests/ --cov=social_analyzer --cov-report=html
```

### Using tox

```bash
# Install tox
pip install tox

# Run tests in isolated environment
tox

# Run linting
tox -e lint
```

### Linting

```bash
# Install ruff
pip install ruff

# Check code
ruff check social_analyzer tests

# Auto-fix issues
ruff check --fix social_analyzer tests
```

## Docker

### Building the Docker Image

```bash
# Build the Python-based image
docker build -f Dockerfile.python -t social-analyzer:latest .
```

### Running with Docker

```bash
# Run with command line arguments
docker run social-analyzer:latest --list

# Run with specific username search
docker run social-analyzer:latest --username johndoe --websites youtube
```

### Using docker-compose

```bash
# Start the service with docker-compose
docker-compose -f docker-compose.override.yml up --build

# Run in detached mode
docker-compose -f docker-compose.override.yml up -d --build

# Stop the service
docker-compose -f docker-compose.override.yml down
```

## Continuous Integration

The project includes GitHub Actions CI workflow that:

- Tests on Python 3.10 and 3.11
- Installs system dependencies for lxml
- Runs pytest
- Performs optional linting with ruff

The CI workflow is triggered on:
- Push to main branch
- Pull requests to main branch

## Package Structure

```
hide-and-seek/
├── social_analyzer/          # Main package directory
│   ├── __init__.py          # Package initialization
│   ├── app.py               # Main CLI and analyzer logic
│   └── data/                # Data files (sites, languages)
├── tests/                    # Test directory
│   ├── __init__.py
│   └── test_basic.py        # Basic unit tests
├── setup.py                  # Package setup configuration
├── setup.cfg                 # Additional metadata
├── MANIFEST.in              # Files to include in distribution
├── requirements.txt          # Python dependencies
├── tox.ini                  # Tox configuration
├── Dockerfile.python        # Python-based Dockerfile
├── docker-compose.override.yml  # Docker compose for local dev
├── start.sh                 # Docker entrypoint script
├── .github/workflows/ci.yml # CI/CD configuration
├── PRIVACY_AND_COMPLIANCE.md # Privacy guidance
└── CHANGELOG.md             # Version history
```

## Privacy and Compliance

Please review [PRIVACY_AND_COMPLIANCE.md](PRIVACY_AND_COMPLIANCE.md) for important information about:
- Handling sensitive data
- Legal compliance requirements
- Best practices for production use

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

This project is licensed under AGPL-3.0. See the LICENSE file for details.

## Support

For issues, questions, or contributions, please visit:
https://github.com/gittisak-go/hide-and-seek
