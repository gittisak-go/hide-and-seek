#!/bin/bash
set -e

# Check if gunicorn is available and app module can be used as WSGI
if command -v gunicorn &> /dev/null; then
    echo "Starting with gunicorn..."
    # Note: app.py is a CLI tool, not a WSGI app
    # For now, just run python app.py
    exec python -m social_analyzer.app "$@"
else
    echo "Starting with python..."
    exec python -m social_analyzer.app "$@"
fi
