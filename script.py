import os
import argparse

import subprocess
import shutil
import time
from playwright.sync_api import sync_playwright
from flask import Flask

from flutter_screenshot import run_flutter_and_screenshot  # ✅ import the actual logic
from handlers import NewImageHandler  # Ensure you have the `handlers` module
from image_similarity import check_image_size_and_similarity  # Ensure you have this module

# Flask app setup
app = Flask(__name__)

# Directory configurations
dart_files_dir = os.path.join(app.static_folder, 'dart_files')

correct_images_dir = os.path.join(app.static_folder, 'correct_images')
output_folder = os.path.join(app.static_folder, 'output')
template_project_dir = "/home/lynnhtetaung/Documents/develop/plas/fplas-evaluation"  # Update to your Flutter project path
template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')
flutter_executable = "/home/lynnhtetaung/flutter/bin/flutter"
error_image_path = os.path.join(app.static_folder, 'error_image.png')  # Placeholder error image
FIXED_FLUTTER_PORT = 8081

# Ensure required directories exist
os.makedirs(output_folder, exist_ok=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Flutter and take screenshots for Dart files.")
    parser.add_argument("--dart_folder", help="Folder containing Dart files.")
    parser.add_argument("--dart_file", help="Specific Dart file to run.")
    parser.add_argument("--screenshot_folder", required=True, help="Folder to save the screenshots.")
    parser.add_argument("--exercise_number", required=True, help="Exercise number for comparison.")

    args = parser.parse_args()
    os.makedirs(args.screenshot_folder, exist_ok=True)

    if args.dart_file:
        dart_file_path = dart_files_dir + '/' + args.dart_file
        filename = os.path.basename(dart_file_path)
        screenshot_path = os.path.join(args.screenshot_folder, f"{os.path.splitext(filename)[0]}.png")
        print(f"📄 Running individual file: {filename}")
        run_flutter_and_screenshot(dart_file_path, screenshot_path, args.exercise_number)



    elif args.dart_folder:
        dart_files = sorted([f for f in os.listdir(args.dart_folder) if f.endswith('.dart')])
        if not dart_files:
            print("No Dart files found in the specified folder.")
            exit(1)

        for dart_file in dart_files:
            dart_file_path = os.path.join(args.dart_folder, dart_file)
            screenshot_path = os.path.join(args.screenshot_folder, f"{os.path.splitext(dart_file)[0]}.png")
            print(f"🔧 Executing script for {dart_file_path}...")
            run_flutter_and_screenshot(dart_file_path, screenshot_path, args.exercise_number)
