import os
import subprocess
import shutil
import time
from playwright.sync_api import sync_playwright
from flask import Flask

from handlers import NewImageHandler  # Make sure this exists
from image_similarity import check_image_size_and_similarity  # Ensure this module works

# Flask app setup (not used directly but needed for static paths)
app = Flask(__name__)

# Directory configurations
correct_images_dir = os.path.join(app.static_folder, 'correct_images')
output_folder = os.path.join(app.static_folder, 'output')
template_project_dir = "/home/lynnhtetaung/Documents/develop/plas/fplas-evaluation"
template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')
flutter_executable = "/home/lynnhtetaung/flutter/bin/flutter"
error_image_path = os.path.join(app.static_folder, 'error_image.png')
FIXED_FLUTTER_PORT = 8081

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)


def run_flutter_and_screenshot(dart_file_path, screenshot_path, exercise_number):
    """
    Dynamically builds Flutter project, runs a web server, and captures a screenshot.
    """
    try:
        dart_file_path = os.path.abspath(dart_file_path)
        print(f"🔧 Loading Dart file: {dart_file_path}")

        # Step 1: Copy Dart code into Flutter project
        with open(dart_file_path, 'r') as dart_file, open(template_main_dart_path, 'w') as main_dart:
            main_dart.write(dart_file.read())

        # Step 2: Free the Flutter web port if in use
        port_in_use = subprocess.run(["lsof", "-t", "-i", f":{FIXED_FLUTTER_PORT}"],
                                     capture_output=True, text=True)
        if port_in_use.stdout:
            print(f"⚠️ Port {FIXED_FLUTTER_PORT} is in use. Killing it...")
            subprocess.run(["fuser", "-k", "-n", "tcp", str(FIXED_FLUTTER_PORT)])

        # Step 3: Build the Flutter project
        print("🏗️ Building Flutter project...")
        build_proc = subprocess.Popen([flutter_executable, "build", "web"], cwd=template_project_dir)
        build_proc.wait()

        if build_proc.returncode != 0:
            print("❌ Flutter build failed.")
            shutil.copy(error_image_path, screenshot_path)
            return

        # Step 4: Start a simple web server
        print(f"🌐 Starting local server on port {FIXED_FLUTTER_PORT}...")
        server_proc = subprocess.Popen(["python3", "-m", "http.server", str(FIXED_FLUTTER_PORT)],
                                       cwd=os.path.join(template_project_dir, 'build', 'web'))

        time.sleep(10)  # Let the server initialize

        # Step 5: Take screenshot with Playwright
        with sync_playwright() as p:
            print("📸 Capturing screenshot...")
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto(f"http://localhost:{FIXED_FLUTTER_PORT}")
            page.wait_for_selector('body', timeout=60000)
            page.screenshot(path=screenshot_path)
            print(f"✅ Screenshot saved: {screenshot_path}")
            browser.close()

        # Step 6: Kill the server process
        server_proc.terminate()

        # Step 7: Run image comparison
        try:
            correct_image_path = os.path.join(correct_images_dir, f'correct_answer_exercise_{exercise_number}.png')
            result = check_image_size_and_similarity([correct_image_path], screenshot_path, output_folder)
            print(f"📊 Similarity check complete. Highlight image: {result.get('highlight_image_path')}")
        except Exception as sim_err:
            print(f"⚠️ Image comparison error: {sim_err}")

    except Exception as e:
        print(f"❌ Error during Flutter build or screenshot: {e}")
