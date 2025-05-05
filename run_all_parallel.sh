#!/bin/bash

# Define the base command
BASE_COMMAND="python3 script.py --screenshot_folder /home/lynnhtetaung/Documents/develop/plas/fplas-evaluation/static/screenshots"

# Define dart content directories and exercise numbers
declare -A exercises=(
    ["p1"]="/home/lynnhtetaung/Documents/develop/plas/fplas-evaluation/p1"
    ["p2"]="/home/lynnhtetaung/Documents/develop/plas/fplas-evaluation/p2"
    ["p3"]="/home/lynnhtetaung/Documents/develop/plas/fplas-evaluation/p3"
    ["p4"]="/home/lynnhtetaung/Documents/develop/plas/fplas-evaluation/p4"
    ["p5"]="/home/lynnhtetaung/Documents/develop/plas/fplas-evaluation/p5"
)

# Execute each script in parallel
for exercise in "${!exercises[@]}"; do
    DART_CONTENT=${exercises[$exercise]}
    echo "Running script for $exercise in the background..."
    $BASE_COMMAND --dart_content "$DART_CONTENT" --exercise_number "$exercise" &
done

# Wait for all background processes to finish
wait
echo "All scripts executed successfully in parallel."
