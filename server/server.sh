#!/bin/bash

# Define the ports
PORT_FLASK=5000
PORT_FLUTTER=8080

# Check if the Flask port is in use and release it if necessary.
echo "Checking if port $PORT_FLASK is in use..."
if netstat -tuln | grep ":$PORT_FLASK "; then
  echo "Port $PORT_FLASK is in use. Stopping the process on that port..."
  fuser -k -n tcp $PORT_FLASK
fi

# Check if the Flutter web port is in use and release it if necessary.
echo "Checking if port $PORT_FLUTTER is in use..."
if netstat -tuln | grep ":$PORT_FLUTTER "; then
  echo "Port $PORT_FLUTTER is in use. Stopping the process on that port..."
  fuser -k -n tcp $PORT_FLUTTER
fi

# Switch to the web construction directory for Flutter
cd /app/build/web/

# Start the web server on the specified Flutter port
echo "Starting the Flutter server on port $PORT_FLUTTER..."
python3 -m http.server $PORT_FLUTTER &

# Start Flask on port 5000
echo "Starting Flask server on port $PORT_FLASK..."
flask run --host=0.0.0.0 --port=$PORT_FLASK
