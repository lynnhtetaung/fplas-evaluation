from flask import Flask, request, jsonify, render_template
import os
from handlers import NewImageHandler
from watchdog.observers import Observer
from flutter_screenshot import run_flutter_and_screenshot
from image_similarity_old import check_image_size_and_similarity

app = Flask(__name__)

screenshot_save_dir = os.path.join(app.static_folder, 'screenshots')
correct_images_dir = os.path.join(app.static_folder, 'correct_images')
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

    screenshot_path = os.path.join(screenshot_save_dir, f'{student_id}_{exercise_name}_{exercise_number}.png')

    # Run the Flutter web rebuild and take the screenshot
    try:
        run_flutter_and_screenshot(main_dart_file_content, screenshot_path)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    # Check if the screenshot was created
    if not os.path.exists(screenshot_path):
        return jsonify({"status": "error", "message": "Screenshot not found"}), 500

    # Run image similarity function if the screenshot was created
    correct_image_path = os.path.join(correct_images_dir, f'correct_answer_exercise_{exercise_number}.png')
    result = check_image_size_and_similarity([correct_image_path], screenshot_path, output_folder)

    highlight_image_path = result.get('highlight_image_path')

    result_template = render_template('result.html', 
                            student_image=f'screenshots/{os.path.basename(screenshot_path)}', 
                            correct_image=f'correct_images/{os.path.basename(correct_image_path)}', 
                            highlight_image=f'output/{os.path.basename(highlight_image_path)}')

    return jsonify({"status": "success", "resultTemplate": result_template}), 200

if __name__ == '__main__':
    correct_image_paths = [os.path.join(correct_images_dir, f'correct_answer_exercise_p{i}.png') for i in range(1, 6)]
    event_handler = NewImageHandler(correct_image_paths, output_folder, check_image_size_and_similarity)
    observer = Observer()
    observer.schedule(event_handler, screenshot_save_dir, recursive=False)
    observer.start()

    app.run(host="0.0.0.0", port=5000)

    observer.stop()
    observer.join()
