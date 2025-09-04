import os

# Configuration file placeholder

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
    STATIC_FOLDER = 'app/static'
    OUTPUT_FOLDER = os.path.join(STATIC_FOLDER, 'output')
    SCREENSHOT_FOLDER = os.path.join(STATIC_FOLDER, 'screenshots')
    DART_SCREENSHOT_FOLDER = os.path.join(STATIC_FOLDER, 'dart_screenshots')
    CORRECT_IMAGES_DIR = os.path.join(STATIC_FOLDER, 'correct_images')
    ERROR_IMAGE_PATH = os.path.join(STATIC_FOLDER, 'error_image.png')
    FLUTTER_EXECUTABLE = '/home/lynnhtetaung/flutter/bin/flutter'
    TEMPLATE_PROJECT_DIR = '/home/lynnhtetaung/Documents/develop/plas/fplas-evaluation'
    TEMPLATE_MAIN_DART_PATH = os.path.join(TEMPLATE_PROJECT_DIR, 'lib', 'main.dart')
    FIXED_FLUTTER_PORT = 8081
