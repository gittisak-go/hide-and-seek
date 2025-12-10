#!/bin/bash

# Entrypoint script for the Docker container
# Try to use gunicorn if available, otherwise fall back to python app.py

if command -v gunicorn &> /dev/null; then
    echo "Starting with gunicorn..."
    exec gunicorn -w 4 -b 0.0.0.0:8000 app:app
else
    echo "Gunicorn not found, starting with python..."
    exec python app.py
fi
