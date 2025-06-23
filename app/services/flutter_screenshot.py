import os
from .screenshot import run_flutter_and_screenshot

def process_single_dart_file(dart_file_path, screenshot_path, exercise_number):
    print(f"📄 Running individual file: {os.path.basename(dart_file_path)}")
    run_flutter_and_screenshot(dart_file_path, screenshot_path, exercise_number)

def process_dart_folder(dart_folder, screenshot_folder, exercise_number):
    dart_files = sorted([f for f in os.listdir(dart_folder) if f.endswith('.dart')])
    if not dart_files:
        print("❌ No Dart files found.")
        return
    for dart_file in dart_files:
        dart_file_path = os.path.join(dart_folder, dart_file)
        screenshot_path = os.path.join(screenshot_folder, exercise_number, f"{os.path.splitext(dart_file)[0]}.png")
        print(f"🔧 Executing script for {dart_file_path}...")
        run_flutter_and_screenshot(dart_file_path, screenshot_path, exercise_number)
