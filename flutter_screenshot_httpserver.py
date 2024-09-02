import os
import time
import subprocess
from playwright.sync_api import sync_playwright

# Path configurations
template_project_dir = '/home/lynnhtetaung/Documents/develop/plas/flutter_app' # for Local
flutter_executable = '/home/lynnhtetaung/flutter/bin/flutter'

template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')

FIXED_FLUTTER_PORT = 8081

# Function to rebuild Flutter and take a screenshot
def run_flutter_and_screenshot(main_dart_file_content, screenshot_path):
    try:
        # Write the received Dart source code to main.dart
        with open(template_main_dart_path, 'w') as f:
            f.write(main_dart_file_content)

        # Stop any process using the port
        port_in_use_process = subprocess.run(["lsof", "-t", "-i", f":{FIXED_FLUTTER_PORT}"], capture_output=True, text=True)
        if port_in_use_process.stdout:
            print(f"Port {FIXED_FLUTTER_PORT} is in use. Stopping the process...")
            subprocess.run(["fuser", "-k", "-n", "tcp", str(FIXED_FLUTTER_PORT)])

        # Rebuild Flutter web project
        print("Building Flutter web project...")
        flutter_process = subprocess.Popen([flutter_executable, 'build', 'web'], cwd=template_project_dir)
        flutter_process.wait()  # Wait for the build to complete

        # Start the web server after the Flutter build
        print(f"Starting the web server on port {FIXED_FLUTTER_PORT}...")
        server_process = subprocess.Popen(["python3", "-m", "http.server", str(FIXED_FLUTTER_PORT)], cwd=os.path.join(template_project_dir, 'build', 'web'))

        # Wait for the server to start
        time.sleep(15)

        # Take screenshot using Playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto(f"http://localhost:{FIXED_FLUTTER_PORT}")
            
            # Ensure the page is fully loaded
            page.wait_for_selector('body', timeout=60000)  # Wait for body to be present
            page.wait_for_load_state("networkidle", timeout=60000)  # Ensure all network activity has stopped

            # Take the screenshot
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)  # Ensure directory exists
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
            browser.close()

        # Stop the web server after screenshot
        server_process.terminate()

    except Exception as e:
        print(f"Error: {e}")