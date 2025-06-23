import os
import argparse
import subprocess
import shutil
import time
from playwright.sync_api import sync_playwright
from flask import Flask

from handlers import NewImageHandler  # Ensure you have the `handlers` module
from image_similarity import check_image_size_and_similarity  # Ensure you have this module

# Flask app setup
app = Flask(__name__)

# Directory configurations
correct_images_dir = os.path.join(app.static_folder, 'correct_images')
output_folder = os.path.join(app.static_folder, 'output')
template_project_dir = "/home/lynnhtetaung/Documents/develop/plas/fplas-evaluation"  # Update to your Flutter project path
template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')
flutter_executable = "/home/lynnhtetaung/flutter/bin/flutter"
error_image_path = os.path.join(app.static_folder, 'error_image.png')  # Placeholder error image
FIXED_FLUTTER_PORT = 8081

# Ensure required directories exist
os.makedirs(output_folder, exist_ok=True)


def run_flutter_and_screenshot(dart_file_path, screenshot_path, exercise_number):
    """
    Dynamically builds Flutter project, runs a web server, and captures a screenshot.
    """
    try:
        # Copy Dart content to the main.dart file
        with open(dart_file_path, 'r') as dart_file, open(template_main_dart_path, 'w') as main_dart:
            main_dart.write(dart_file.read())

        # Stop any process using the specified Flutter port
        port_in_use_process = subprocess.run(["lsof", "-t", "-i", f":{FIXED_FLUTTER_PORT}"], capture_output=True, text=True)
        if port_in_use_process.stdout:
            print(f"Port {FIXED_FLUTTER_PORT} is in use. Stopping the process...")
            subprocess.run(["fuser", "-k", "-n", "tcp", str(FIXED_FLUTTER_PORT)])

        # Rebuild Flutter web project
        print(f"Building Flutter web project for {dart_file_path}...")
        build_process = subprocess.Popen([flutter_executable, 'build', 'web'], cwd=template_project_dir)
        build_process.wait()

        if build_process.returncode != 0:
            print(f"Flutter build failed for {dart_file_path}.")
            shutil.copy(error_image_path, screenshot_path)  # Use an error placeholder image
            return

        # Start a web server to host the built Flutter project
        print(f"Starting web server on port {FIXED_FLUTTER_PORT}...")
        server_process = subprocess.Popen(["python3", "-m", "http.server", str(FIXED_FLUTTER_PORT)],
                                          cwd=os.path.join(template_project_dir, 'build', 'web'))

        time.sleep(10)  # Allow the server some time to start

        # Capture screenshot using Playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto(f"http://localhost:{FIXED_FLUTTER_PORT}")
            page.wait_for_selector('body', timeout=60000)  # Ensure the page has loaded
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
            browser.close()

        # Terminate the web server
        server_process.terminate()

    except Exception as e:
        print(f"Error during Flutter build or screenshot: {e}")
        return

    # Compare the screenshot with the correct image
    try:
        correct_image_path = os.path.join(correct_images_dir, f'correct_answer_exercise_{exercise_number}.png')
        result = check_image_size_and_similarity([correct_image_path], screenshot_path, output_folder)

        highlight_image_path = result.get('highlight_image_path')
        print({
            "status": "success",
        })

    except Exception as e:
        print({"status": "error", "message": str(e)})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Flutter and take screenshots for multiple Dart files.")
    parser.add_argument("--dart_content", required=True, help="Folder containing Dart files.")
    parser.add_argument("--screenshot_folder", required=True, help="Folder to save the screenshots.")
    parser.add_argument("--exercise_number", required=True, help="Exercise number for comparison.")

    args = parser.parse_args()

    dart_content_path = args.dart_content
