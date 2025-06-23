import os
import time
import shutil
import subprocess
from playwright.sync_api import sync_playwright
import argparse

# Path configurations
template_project_dir = '/home/lynnhtetaung/Documents/develop/plas/flutter-evaluation'  # for Local
flutter_executable = '/home/lynnhtetaung/flutter/bin/flutter'

template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')
FIXED_FLUTTER_PORT = 8081

error_image_path = os.path.join(template_project_dir, 'error_images', 'error_image.png')  # Path to your error image

# Function to rebuild Flutter and take a screenshot
def run_flutter_and_screenshot(dart_file_path, screenshot_path):
    try:
        # Write the current Dart file to main.dart
        with open(dart_file_path, 'r') as dart_file, open(template_main_dart_path, 'w') as main_dart:
            main_dart.write(dart_file.read())

        # Stop any process using the port
        port_in_use_process = subprocess.run(["lsof", "-t", "-i", f":{FIXED_FLUTTER_PORT}"], capture_output=True, text=True)
        if port_in_use_process.stdout:
            print(f"Port {FIXED_FLUTTER_PORT} is in use. Stopping the process...")
            subprocess.run(["fuser", "-k", "-n", "tcp", str(FIXED_FLUTTER_PORT)])

        # Rebuild Flutter web project
        print(f"Building Flutter web project for {dart_file_path}...")
        build_process = subprocess.Popen([flutter_executable, 'build', 'web'], cwd=template_project_dir)
        build_process.wait()  # Wait for the build to complete

        # Check if the build was successful
        if build_process.returncode != 0:
            print(f"Flutter build failed for {dart_file_path}. Stopping process.")
            shutil.copy(error_image_path, screenshot_path)  # Copy error image
            return  # Stop further processing

        # Start the web server after the Flutter build
        print(f"Starting the web server on port {FIXED_FLUTTER_PORT} for {dart_file_path}...")
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

if __name__ == "__main__":
    # Command-line arguments
    parser = argparse.ArgumentParser(description="Run Flutter and take screenshots for multiple Dart files.")
    parser.add_argument("--dart_content", required=True, help="Folder containing Dart files.")
    parser.add_argument("--screenshot_folder", required=True, help="Folder to save the screenshots.")
    args = parser.parse_args()
    dart_content_path = args.dart_content
    screenshot_folder = args.screenshot_folder
    # Ensure the screenshot folder exists
    os.makedirs(screenshot_folder, exist_ok=True)
    # Process each Dart file in the folder
    dart_files = [f for f in os.listdir(dart_content_path) if f.endswith('.dart')]
    if not dart_files:
        print("No Dart files found in the specified folder.")
        exit(1)
    for dart_file in dart_files:
        dart_file_path = os.path.join(dart_content_path, dart_file)
        screenshot_path = os.path.join(screenshot_folder, f"{os.path.splitext(dart_file)[0]}_screenshot.png")
        print(f"Processing {dart_file}...")
        run_flutter_and_screenshot(dart_file_path, screenshot_path)
