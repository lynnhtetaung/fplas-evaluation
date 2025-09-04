import os
import argparse
import subprocess
import shutil
import time
from playwright.sync_api import sync_playwright
from flask import Flask
from config.config import Config

from app.services.flutter_screenshot import process_single_dart_file, process_dart_folder

# Flask app setup
app = Flask(__name__)

# Directory configurations
# Use config settings for directories

def main():
    parser = argparse.ArgumentParser(description="Run Flutter and take screenshots for Dart files.")
    parser.add_argument("--dart_folder", help="Folder containing Dart files.")
    parser.add_argument("--dart_file", help="Specific Dart file to run.")
    parser.add_argument("--screenshot_folder", required=True, help="Folder to save the screenshots.")
    parser.add_argument("--exercise_number", required=True, help="Exercise number (e.g., p1, p2).")

    args = parser.parse_args()

    os.makedirs(args.screenshot_folder, exist_ok=True)

    # Use config for dart_files_dir
    dart_files_dir = os.path.join(Config.STATIC_FOLDER, 'yolo_dart_files')

    if args.dart_file:
        dart_file_path = os.path.join(dart_files_dir, args.exercise_number, args.dart_file)
        if not os.path.exists(dart_file_path):
            print(f"❌ Dart file not found: {dart_file_path}")
            return
        filename = os.path.basename(dart_file_path)
        screenshot_path = os.path.join(args.screenshot_folder, args.exercise_number, f"{os.path.splitext(filename)[0]}.png")
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        process_single_dart_file(dart_file_path, screenshot_path, args.exercise_number)
    elif args.dart_folder:
        dart_folder = os.path.abspath(args.dart_folder)
        process_dart_folder(dart_folder, args.screenshot_folder, args.exercise_number)

if __name__ == "__main__":
    main()
