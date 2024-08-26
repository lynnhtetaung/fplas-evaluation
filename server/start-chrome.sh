#!/bin/bash

# Start Xvfb to run Chrome without a display
Xvfb :99 -screen 0 1280x1024x24 &

# Set the DISPLAY environment variable to tell Chrome where to render
export DISPLAY=:99

# Run Google Chrome with necessary flags as the 'chrome' user
/usr/bin/google-chrome-stable --no-sandbox --disable-dev-shm-usage --headless --disable-gpu --remote-debugging-port=9222 &

# Wait for all background processes to finish
wait
