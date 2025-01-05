# Base image for Python environment
FROM debian:latest AS build-env

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       sudo curl git wget unzip \
       python3 python3-pip python3-venv \
       build-essential cmake \
       fonts-liberation libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcairo2 libcups2 \
       libgbm1 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libu2f-udev libxcomposite1 libxdamage1 libxrandr2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app/

# Copy requirements.txt for Python dependencies
COPY requirements.txt /app/requirements.txt

# Create a virtual environment and install Python dependencies
RUN python3 -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install -r /app/requirements.txt \
    && /venv/bin/playwright install \
    && /venv/bin/playwright install-deps

# Set virtual environment in PATH
ENV PATH="/venv/bin:$PATH"

# Copy YOLO model weights
COPY models/best.pt /app/models/best.pt

# Expose port for Flask
EXPOSE 5000

# Start the Flask API (or any Python application)
CMD ["python3", "main.py"]
