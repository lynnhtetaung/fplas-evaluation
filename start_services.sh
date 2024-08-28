#!/bin/bash

# Define the ports
FLASK_PORT=5000
WEB_PORT=8080

# Check if the Flask port is in use and release it if necessary.
echo "Checking if Flask port $FLASK_PORT is in use..."
if [ "$(lsof -t -i :$FLASK_PORT)" ]; then
  echo "Flask port $FLASK_PORT is in use. Stopping the process on that port..."
  fuser -k -n tcp $FLASK_PORT
fi

# Check if the web port is in use and release it if necessary.
echo "Checking if web port $WEB_PORT is in use..."
if [ "$(lsof -t -i :$WEB_PORT)" ]; then
  echo "Web port $WEB_PORT is in use. Stopping the process on that port..."
  fuser -k -n tcp $WEB_PORT
fi

# Start Xvfb (optional)
echo "Starting Xvfb..."
Xvfb :99 -screen 0 1280x720x24 &

# Set display environment variable
export DISPLAY=:99

# Start the Flask API
echo "Starting Flask API on port $FLASK_PORT..."
python3 /app/main.py &

# Switch to the web construction directory
cd /app/build/web/

# Start the web server on the specified port
echo "Starting the web server on port $WEB_PORT..."
python3 -m http.server $WEB_PORT
