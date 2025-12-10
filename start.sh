#!/bin/bash
set -e

# Start script for social-analyzer
# Uses gunicorn if available, otherwise falls back to python app.py

if command -v gunicorn &> /dev/null; then
    echo "Starting with gunicorn..."
    gunicorn -w 4 -b 0.0.0.0:8000 app:app
else
    echo "Gunicorn not found, starting with python..."
    python app.py
fi
