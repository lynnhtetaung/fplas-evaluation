import os
import argparse
import subprocess
import shutil
import time
from playwright.sync_api import sync_playwright
from flask import Flask
from config.config import Config

# Assuming these functions exist and are properly implemented
from app.services.flutter_screenshot import process_single_dart_file, process_dart_folder
from app.services.image_comparison import check_image_size_and_similarity

# Flask app setup
app = Flask(__name__)
app.config.from_object(Config)

# Directory configurations
correct_images_dir = app.config['CORRECT_IMAGES_DIR']
output_folder = app.config['OUTPUT_FOLDER']
static_folder = app.config['STATIC_FOLDER']

def main():
    parser = argparse.ArgumentParser(description="Run Flutter and take screenshots for Dart files.")
    parser.add_argument("--dart_folder", help="Folder containing Dart files.")
    parser.add_argument("--dart_file", help="Specific Dart file to run.")
    parser.add_argument("--screenshot_folder", required=True, help="Folder to save the screenshots.")
    parser.add_argument("--exercise_number", required=True, help="Exercise number (e.g., p1, p2).")

    args = parser.parse_args()

    os.makedirs(args.screenshot_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    dart_files_base_dir = os.path.join(static_folder, 'dart_files', args.exercise_number)

    if args.dart_file:
        dart_file_path = os.path.join(dart_files_base_dir, args.dart_file)
        if not os.path.exists(dart_file_path):
            print(f"❌ Dart file not found: {dart_file_path}")
            return

        filename_without_ext = os.path.splitext(os.path.basename(dart_file_path))[0]
        screenshot_path = os.path.join(args.screenshot_folder, f"{filename_without_ext}.png")
        
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        process_single_dart_file(dart_file_path, screenshot_path, args.exercise_number)

        try:
            # Using the static correct image path as requested
            correct_image_path = os.path.join(correct_images_dir, f'correct_answer_exercise_{args.exercise_number}.png')
            
            if not os.path.exists(correct_image_path):
                print(f"⚠️ Correct image not found for comparison: {correct_image_path}")
            else:
                result = check_image_size_and_similarity([correct_image_path], screenshot_path, output_folder)
                
                if result.get('highlight_image_path'):
                    print(f"⚠️ Differences found for {filename_without_ext}. Saving error image.")
                    print({
                        "status": "difference",
                        "file": filename_without_ext,
                        "highlight_image_path": result['highlight_image_path']
                    })
                else:
                    print(f"✅ No differences found for {filename_without_ext}.")
                    print({
                        "status": "success",
                        "file": filename_without_ext,
                    })

        except Exception as e:
            print({"status": "error", "message": f"Error during image comparison: {str(e)}"})

    elif args.dart_folder:
        dart_folder_path = os.path.abspath(args.dart_folder)
        if not os.path.exists(dart_folder_path):
            print(f"❌ Dart folder not found: {dart_folder_path}")
            return
            
        try:
            generated_screenshots = process_dart_folder(dart_folder_path, args.screenshot_folder, args.exercise_number)
            
            # Using the static correct image path as requested
            correct_image_path = os.path.join(correct_images_dir, f'correct_answer_exercise_{args.exercise_number}.png')

            if not os.path.exists(correct_image_path):
                print(f"⚠️ Correct image not found for comparison: {correct_image_path}")
                return

            for screenshot_path in generated_screenshots:
                filename = os.path.basename(screenshot_path)
                filename_without_ext = os.path.splitext(filename)[0]

                result = check_image_size_and_similarity([correct_image_path], screenshot_path, output_folder)
                
                if result.get('highlight_image_path'):
                    print(f"⚠️ Differences found for {filename_without_ext}. Saving error image.")
                    print({
                        "status": "difference",
                        "file": filename,
                        "highlight_image_path": result['highlight_image_path']
                    })
                else:
                    print(f"✅ No differences found for {filename_without_ext}.")
                    print({
                        "status": "success",
                        "file": filename
                    })

        except Exception as e:
            print({"status": "error", "message": f"Error processing folder: {str(e)}"})

if __name__ == "__main__":
    main()