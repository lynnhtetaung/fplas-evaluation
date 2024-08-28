# Base image for building the Flutter web app
FROM debian:latest AS build-env

# Install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       sudo curl git wget unzip \
       python3 python3-pip python3-venv \
       build-essential cmake \
       fonts-liberation libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcairo2 libcups2 \
       libgbm1 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libu2f-udev libxcomposite1 libxdamage1 libxrandr2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Download Flutter SDK
RUN git clone https://github.com/flutter/flutter.git /usr/local/flutter

# Set Flutter environment path
ENV PATH="/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin:${PATH}"

# Run Flutter doctor
RUN flutter doctor

# Enable Flutter web support
RUN flutter channel master \
    && flutter upgrade \
    && flutter config --enable-web

# Set working directory
WORKDIR /app/

# Copy application files
COPY . /app/

# Build Flutter web app
RUN flutter clean
RUN flutter pub get
RUN flutter build web

# Install Python dependencies
RUN python3 -m venv /venv \
    && /venv/bin/pip install --upgrade pip setuptools wheel \
    && /venv/bin/pip install flask watchdog opencv-python Pillow pytest-playwright \
    && /venv/bin/playwright install \
    && /venv/bin/playwright install-deps

# Set virtual environment in PATH
ENV PATH="/venv/bin:$PATH"

# Expose ports for Flask and Nginx
EXPOSE 5000

# Start both Flask and Nginx
CMD ["python3", "main.py"]
