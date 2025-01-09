from flask import Flask, request, jsonify, render_template
import os
from components.yolo_detector import detect_components  # Import the detect_components function
from components.flutter_screenshot_httpserver import run_flutter_and_screenshot

app = Flask(__name__)

# Directories
screenshot_save_dir = os.path.join(app.static_folder, 'screenshots')
output_folder = os.path.join(app.static_folder, 'output')

# Ensure directories exist
os.makedirs(screenshot_save_dir, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()

    main_dart_file_content = data.get('sourceCode')
    student_id = data.get('studentId')
    exercise_name = data.get('exerciseName')
    exercise_number = data.get('exerciseNumber')

    if not main_dart_file_content or not student_id or not exercise_number:
        return jsonify({"status": "error", "message": "Missing sourceCode, studentId, or exerciseNumber"}), 400

    # Save student screenshot
    screenshot_path = os.path.join(screenshot_save_dir, f'{student_id}_{exercise_name}_{exercise_number}.png')
    try:
        # Save the Flutter output screenshot here (integration required)
        run_flutter_and_screenshot(main_dart_file_content, screenshot_path)
        pass
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    # Ensure screenshot exists
    if not os.path.exists(screenshot_path):
        return jsonify({"status": "error", "message": "Screenshot not found"}), 500

    # Detect components using YOLO
    try:
        percentage, result_image = detect_components(screenshot_path)

        # If `result_image` is a file path, copy it to the output folder
        if isinstance(result_image, str):  # Check if it's a file path
            result_image_path = os.path.join(output_folder, f'result_{student_id}_{exercise_name}_{exercise_number}.png')
            if os.path.exists(result_image):  # Copy error image if it exists
                os.makedirs(output_folder, exist_ok=True)
                os.system(f"cp {result_image} {result_image_path}")  # Use OS copy command
        else:  # If it's an image object, save it
            result_image_path = os.path.join(output_folder, f'result_{student_id}_{exercise_name}_{exercise_number}.png')
            result_image.save(result_image_path)

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    # Render result template
    result_template = render_template(
        'yolo-result.html',
        student_image=f'screenshots/{os.path.basename(screenshot_path)}',
        result_image=f'output/{os.path.basename(result_image_path)}',
        detection_percentage=percentage
    )

    return jsonify({"status": "success", "resultTemplate": result_template}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
