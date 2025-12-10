#!/bin/bash
# Entrypoint script for social-analyzer
# Uses gunicorn if available, otherwise falls back to python app.py

set -e

if command -v gunicorn &> /dev/null; then
    echo "Starting with gunicorn..."
    exec gunicorn -b 0.0.0.0:8000 -w 4 --timeout 120 app:main
else
    echo "Gunicorn not found, starting with python app.py..."
    exec python app.py
fi
