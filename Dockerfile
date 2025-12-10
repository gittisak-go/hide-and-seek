FROM python:3.11-slim

WORKDIR /usr/src/app

# Install system dependencies for lxml
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libxml2-dev libxslt1-dev gcc g++ && \
    rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 8000

# Default command
CMD ["python", "app.py"]
