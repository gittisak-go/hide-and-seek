#!/bin/bash

# Entrypoint script for the Docker container
# Simply run the app directly with Python

echo "Starting social-analyzer with python..."
exec python app.py "$@"
