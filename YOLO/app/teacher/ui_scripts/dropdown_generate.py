import os
import random
import time
import shutil
import subprocess
from playwright.sync_api import sync_playwright
from flask import Flask


app = Flask(__name__)

# Paths
template_project_dir = '/home/lynnhtetaung/Documents/develop/plas/flutter_app'  # Flutter project directory
flutter_executable = '/home/lynnhtetaung/flutter/bin/flutter'  # Flutter executable path
template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')

screenshot_output_dir = os.path.join(app.static_folder, 'screenshot_output')  # Change to your desired output path
dart_files_output_dir = os.path.join(app.static_folder, 'dart_files_output')  # Path to save generated Dart files

# Fixed Flutter port
FIXED_FLUTTER_PORT = 8081

# Ensure output directories exist
os.makedirs(screenshot_output_dir, exist_ok=True)
os.makedirs(dart_files_output_dir, exist_ok=True)

def generate_dropdown_widget():
    options = random.sample(["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"], 3)

    dropdown_items = ",\n                  ".join(
        [f"DropdownMenuItem(value: '{opt}', child: Text('{opt}'))" for opt in options]
    )

    return f"""
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {{
  const MyApp({{super.key}});

  @override
  Widget build(BuildContext context) {{
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Flutter Dropdown Example'),
        ),
        body: Center(
          child: DropdownButton<String>(
            items: [
              {dropdown_items}
            ],
            onChanged: (value) {{}},
            hint: const Text('Select one'),
            // Increase the size of the dropdown
            iconSize: 30.0, // Increase the size of the dropdown icon
            style: TextStyle(fontSize: 20.0), // Increase the font size of the text
            dropdownColor: Colors.white, // Optional: Adjust dropdown background color
            isExpanded: true, // Make the dropdown button fill available space
            padding: EdgeInsets.symmetric(horizontal: 20.0), // Add padding for larger size
          ),
        ),
      ),
    );
  }}
}}
"""

# Function to rebuild Flutter and take a screenshot
def run_flutter_and_screenshot(main_dart_file_content, screenshot_path):
    try:
        # Write Dart source code to main.dart
        with open(template_main_dart_path, 'w') as f:
            f.write(main_dart_file_content)

        # Stop any process using the port
        port_in_use_process = subprocess.run(["lsof", "-t", "-i", f":{FIXED_FLUTTER_PORT}"], capture_output=True, text=True)
        if port_in_use_process.stdout:
            print(f"Port {FIXED_FLUTTER_PORT} is in use. Stopping the process...")
            subprocess.run(["fuser", "-k", "-n", "tcp", str(FIXED_FLUTTER_PORT)])

        # Build Flutter web project
        print("Building Flutter web project...")
        build_process = subprocess.Popen([flutter_executable, 'build', 'web'], cwd=template_project_dir)
        build_process.wait()

        if build_process.returncode != 0:
            print("Flutter build failed. Skipping this UI.")
            return

        # Start web server
        print(f"Starting web server on port {FIXED_FLUTTER_PORT}...")
        server_process = subprocess.Popen(["python3", "-m", "http.server", str(FIXED_FLUTTER_PORT)], cwd=os.path.join(template_project_dir, 'build', 'web'))
        time.sleep(5)  # Allow server time to start

        # Take screenshot
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto(f"http://localhost:{FIXED_FLUTTER_PORT}")
            page.wait_for_selector('body', timeout=60000)
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
            browser.close()

        server_process.terminate()

    except Exception as e:
        print(f"Error: {e}")

# Generate Dart files and capture screenshots
num_files = 2
for i in range(1, num_files + 1):
    dart_code = generate_dropdown_widget()
    dart_file_path = os.path.join(dart_files_output_dir, f"dropdown_ui_{i}.dart")
    screenshot_path = os.path.join(screenshot_output_dir, f"dropdown_ui_{i}.png")

    # Save Dart file
    with open(dart_file_path, 'w') as f:
        f.write(dart_code)

    # Take screenshot
    run_flutter_and_screenshot(dart_code, screenshot_path)
