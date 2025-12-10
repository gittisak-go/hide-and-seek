FROM python:3.11-slim

# Install system dependencies for lxml
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libxml2-dev \
    libxslt-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt || \
    pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY app.py .
COPY data/ ./data/

# Expose port 8000
EXPOSE 8000

# Default command
CMD ["python", "app.py"]

