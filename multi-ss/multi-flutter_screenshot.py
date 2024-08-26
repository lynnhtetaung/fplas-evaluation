import os
import time
import subprocess
from playwright.sync_api import sync_playwright

# Path configurations
# template_project_dir = '/home/lynnhtetaung/Documents/develop/PLAS/flutter_app' # for Local
template_project_dir = '/app' # for Docker

template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')
flutter_executable = '/home/lynnhtetaung/flutter/bin/flutter'
FIXED_FLUTTER_PORT = 8080

def run_flutter_and_screenshot(main_dart_file, screenshot_folder, exercise_number):
    try:
        # Write the main Dart file content to the template file
        with open(template_main_dart_path, 'w') as f:
            f.write(main_dart_file)

        # Start the Flutter app
        flutter_process = subprocess.Popen([
            flutter_executable, 'run', '-d', 'chrome',
            '--web-port', str(FIXED_FLUTTER_PORT)
        ], cwd=template_project_dir)

        # Wait for the Flutter app to start
        time.sleep(60)

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            # Load the Flutter app
            page.goto(f"http://localhost:{FIXED_FLUTTER_PORT}")
            time.sleep(10)

            # Generate unique filenames based on the exercise number
            screenshot_count = 1

            while True:
                screenshot_path = os.path.join(screenshot_folder, f'exercise_{exercise_number}_page_{screenshot_count}.png')
                
                # Ensure unique filename
                while os.path.exists(screenshot_path):
                    screenshot_count += 1
                    screenshot_path = os.path.join(screenshot_folder, f'exercise_{exercise_number}_page_{screenshot_count}.png')

                page.screenshot(path=screenshot_path)
                print(f"Screenshot {screenshot_count} taken: {screenshot_path}")

                # Try to find an element to click
                buttons = page.locator('text=Continue, text=Press me')  # Adjust selectors as needed
                if buttons.count() > 0:
                    buttons.first.click()
                    time.sleep(10)  # Wait for the new page to load
                    screenshot_count += 1
                else:
                    break  # No more buttons to click

            browser.close()

        # Terminate the Flutter process
        flutter_process.terminate()
    except Exception as e:
        print(f"Error: {e}")
