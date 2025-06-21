import os
import argparse

import subprocess
import shutil
import time
from playwright.sync_api import sync_playwright
from flask import Flask

from screenshot_csv import run_flutter_and_screenshot  # ✅ import the actual logic
# from handlers import NewImageHandler  # Ensure you have the `handlers` module
# from image_similarity import check_image_size_and_similarity  # Ensure you have this module

# Flask app setup
app = Flask(__name__)

# Directory configurations
dart_files_dir = os.path.join(app.static_folder, 'dart_files')

def main():
    parser = argparse.ArgumentParser(description="Run Flutter and take screenshots for Dart files.")
    parser.add_argument("--dart_folder", help="Folder containing Dart files.")
    parser.add_argument("--dart_file", help="Specific Dart file to run.")
    parser.add_argument("--screenshot_folder", required=True, help="Folder to save the screenshots.")
    parser.add_argument("--exercise_number", required=True, help="Exercise number (e.g., p1, p2).")

    args = parser.parse_args()

    os.makedirs(args.screenshot_folder, exist_ok=True)

    if args.dart_file:
        dart_file_path = os.path.join(dart_files_dir, args.exercise_number, args.dart_file)
        if not os.path.exists(dart_file_path):
            print(f"❌ Dart file not found: {dart_file_path}")
            return

        filename = os.path.basename(dart_file_path)
        screenshot_path = os.path.join(args.screenshot_folder, args.exercise_number, f"{os.path.splitext(filename)[0]}.png")
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

        print(f"📄 Running individual file: {filename}")
        run_flutter_and_screenshot(dart_file_path, screenshot_path, args.exercise_number)

    elif args.dart_folder:
        dart_folder = os.path.abspath(args.dart_folder)
        dart_files = sorted([f for f in os.listdir(dart_folder) if f.endswith('.dart')])

        if not dart_files:
            print("❌ No Dart files found.")
            return

        for dart_file in dart_files:
            dart_file_path = os.path.join(dart_folder, dart_file)
            screenshot_path = os.path.join(args.screenshot_folder, args.exercise_number, f"{os.path.splitext(dart_file)[0]}.png")

            print(f"🔧 Executing script for {dart_file_path}...")
            run_flutter_and_screenshot(dart_file_path, screenshot_path, args.exercise_number)


if __name__ == "__main__":
    main()
