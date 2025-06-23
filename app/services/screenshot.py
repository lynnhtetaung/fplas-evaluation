import os
import subprocess
import shutil
import time
from playwright.sync_api import sync_playwright
from flask import Flask
from config.config import Config
from .utils import _write_csv

# Directory configurations using config
correct_images_dir = Config.CORRECT_IMAGES_DIR
output_folder = Config.OUTPUT_FOLDER
template_project_dir = Config.TEMPLATE_PROJECT_DIR
template_main_dart_path = Config.TEMPLATE_MAIN_DART_PATH
flutter_executable = Config.FLUTTER_EXECUTABLE
error_image_path = Config.ERROR_IMAGE_PATH
FIXED_FLUTTER_PORT = Config.FIXED_FLUTTER_PORT

os.makedirs(output_folder, exist_ok=True)


def run_flutter_and_screenshot(dart_file_path, screenshot_path, exercise_number):
    try:
        dart_file_path = os.path.abspath(dart_file_path)
        student_id = os.path.splitext(os.path.basename(dart_file_path))[0] or 'No StudentID'
        csv_path = os.path.join(output_folder, "results.csv")
        print(f"🔧 Loading Dart file: {dart_file_path}")
        with open(dart_file_path, 'r') as dart_file, open(template_main_dart_path, 'w') as main_dart:
            main_dart.write(dart_file.read())
        port_check = subprocess.run(["lsof", "-t", "-i", f":{FIXED_FLUTTER_PORT}"], capture_output=True, text=True)
        if port_check.stdout:
            print(f"⚠️ Port {FIXED_FLUTTER_PORT} is in use. Terminating...")
            subprocess.run(["fuser", "-k", "-n", "tcp", str(FIXED_FLUTTER_PORT)])
        print("🏗️ Building Flutter project...")
        build_proc = subprocess.Popen([flutter_executable, "build", "web"], cwd=template_project_dir)
        build_proc.wait()
        if build_proc.returncode != 0:
            print("❌ Flutter build failed.")
            shutil.copy(error_image_path, screenshot_path)
            _write_csv(csv_path, student_id, exercise_number, "Flutter Build Failed")
            return
        print(f"🌐 Starting web server on port {FIXED_FLUTTER_PORT}...")
        server_proc = subprocess.Popen(["python3", "-m", "http.server", str(FIXED_FLUTTER_PORT)], cwd=os.path.join(template_project_dir, 'build', 'web'))
        time.sleep(10)
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
        server_proc.terminate()
        _write_csv(csv_path, student_id, exercise_number, "Success")
    except Exception as e:
        print(f"❌ Error during Flutter build or screenshot: {e}")
        student_id = os.path.splitext(os.path.basename(dart_file_path))[0] or 'No StudentID'
        csv_path = os.path.join(output_folder, "results.csv")
        _write_csv(csv_path, student_id, exercise_number, f"Error: {e}")
