import os
import time
import subprocess
from playwright.sync_api import sync_playwright

# Path configurations
# template_project_dir = '/home/lynnhtetaung/Documents/develop/plas-local/flutter_app' # for Local
# flutter_executable = '/home/lynnhtetaung/flutter/bin/flutter'

template_project_dir = '/app'
flutter_executable = '/usr/local/flutter/bin/flutter'
template_main_dart_path = os.path.join(template_project_dir, 'lib', 'main.dart')

FIXED_FLUTTER_PORT = 80  # Nginx will serve on port 80
shared_dir = '/usr/share/nginx/html'  # Path to the shared volume

# Function to rebuild Flutter and take a screenshot
def run_flutter_and_screenshot(main_dart_file_content, screenshot_path):
    try:
        # Write the received Dart source code to main.dart
        with open(template_main_dart_path, 'w') as f:
            f.write(main_dart_file_content)

        # Rebuild Flutter web project
        print("Building Flutter web project...")
        flutter_process = subprocess.Popen([flutter_executable, 'build', 'web'], cwd=template_project_dir)
        flutter_process.wait()  # Wait for the build to complete

        # Copy the built web project to the shared directory
        print("Copying build/web to shared volume...")
        build_web_path = os.path.join(template_project_dir, 'build', 'web')
        subprocess.run(['cp', '-r', f'{build_web_path}/.', shared_dir])

        # Take screenshot using Playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto(f"http://nginx-app:8080")  # Nginx will serve from port 80 in the nginx-app container

            # Ensure the page is fully loaded
            page.wait_for_selector('body', timeout=60000)  # Wait for body to be present
            page.wait_for_load_state("networkidle", timeout=60000)  # Ensure all network activity has stopped

            # Take the screenshot
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)  # Ensure directory exists
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
            browser.close()

    except Exception as e:
        print(f"Error: {e}")