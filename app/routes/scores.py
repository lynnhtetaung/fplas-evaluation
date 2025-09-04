from flask import Blueprint, render_template, request, Response, jsonify, send_file
import os
import csv
import subprocess
from config.config import Config

bp = Blueprint('scores', __name__)

OUTPUT_FOLDER = Config.OUTPUT_FOLDER
SCREENSHOT_FOLDER = Config.SCREENSHOT_FOLDER
CSV_PATH = os.path.join(os.getcwd(), Config.OUTPUT_FOLDER, 'similarity_results.csv')
YOLO_CSV_PATH = os.path.join(os.getcwd(), Config.OUTPUT_FOLDER, 'model2_GPU.csv')

@bp.route('/student_scores')
def student_scores():
    rows = []
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip header
            for row in reader:
                while len(row) < 4:
                    row.append('')  # Fill missing Remark if needed
                rows.append(row)
    return render_template('student_scores.html', rows=rows)

@bp.route('/yolo_student_scores')
def yolo_student_scores():
    rows = []
    if os.path.exists(YOLO_CSV_PATH):
        with open(YOLO_CSV_PATH, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip header
            for row in reader:
                while len(row) < 4:
                    row.append('')  # Fill missing Remark if needed
                rows.append(row)
    return render_template('yolo_student_scores.html', rows=rows)

@bp.route('/save-student-scores', methods=['POST'])
def save_student_scores():
    data = request.json
    with open(CSV_PATH, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Student Image', 'Similarity (%)', 'Score', 'Remark'])
        writer.writerows(data)
    return jsonify({'status': 'success'})

@bp.route('/save-yolo-scores', methods=['POST'])
def save_yolo_scores():
    data = request.json
    with open(YOLO_CSV_PATH, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Student Answer', 'Problem Type', 'Model v1 (CPU)', 'Model v2 (GPU)'])
        writer.writerows(data)
    return jsonify({'status': 'success'})

@bp.route('/download-scores')
def download_scores():
    return send_file(CSV_PATH, as_attachment=True, download_name='student_scores.csv')

@bp.route('/download-yolo-scores')
def download_yolo_scores():
    return send_file(YOLO_CSV_PATH, as_attachment=True, download_name='yolo_student_scores.csv')

@bp.route('/compare_list')
def compare_list():
    app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_files = set(os.listdir(os.path.join(app_dir, 'static', 'output')))
    screenshot_files = set(os.listdir(os.path.join(app_dir, 'static', 'dart_screenshots')))
    common_files = sorted(list(output_files & screenshot_files))
    return render_template('list.html', projects=common_files)

@bp.route('/yolo_list')
def yolo_list():
    app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_path = os.path.join(app_dir, 'static', 'screenshots')
    categories = {}
    if not os.path.exists(base_path):
        print(f"[ERROR] screenshots folder not found: {base_path}")
    else:
        for folder in sorted(os.listdir(base_path)):
            folder_path = os.path.join(base_path, folder)
            if os.path.isdir(folder_path):
                images = sorted([
                    img for img in os.listdir(folder_path)
                    if img.lower().endswith((".png", ".jpg", ".jpeg"))
                ])
                print(f"Folder: {folder}, Images: {images}")  # Debug print
                categories[folder] = images
    return render_template('yolo_list.html', categories=categories)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/yolo_evaluation')
def yolo_evaluation():
    return render_template('yolo_evaluation.html')

@bp.route('/image_evaluation')
def image_evaluation():
    return render_template('image_evaluation.html')

@bp.route('/student_answers')
def student_answers():
    root_folder = os.path.join(Config.STATIC_FOLDER, 'dart_files')
    projects = {}
    for folder in sorted(os.listdir(root_folder)):
        folder_path = os.path.join(root_folder, folder)
        if os.path.isdir(folder_path):
            entries = []
            for file in sorted(os.listdir(folder_path)):
                if file.endswith('.dart'):
                    with open(os.path.join(folder_path, file), 'r') as f:
                        code_preview = f.read(300)
                    entries.append({
                        'dart': file,
                        'name': file.rsplit('.', 1)[0],
                        'preview': code_preview
                    })
            if entries:
                projects[folder] = entries
    return render_template('student_answers.html', projects=projects)

@bp.route('/yolo_student_answers')
def yolo_student_answers():
    root_folder = os.path.join(Config.STATIC_FOLDER, 'yolo_dart_files')
    projects = {}
    for folder in sorted(os.listdir(root_folder)):
        folder_path = os.path.join(root_folder, folder)
        if os.path.isdir(folder_path):
            entries = []
            for file in sorted(os.listdir(folder_path)):
                if file.endswith('.dart'):
                    with open(os.path.join(folder_path, file), 'r') as f:
                        code_preview = f.read(300)
                    entries.append({
                        'dart': file,
                        'name': file.rsplit('.', 1)[0],
                        'preview': code_preview
                    })
            if entries:
                projects[folder] = entries
    return render_template('yolo_student_answers.html', projects=projects)

@bp.route('/run-dart', methods=['POST'])
def run_dart():
    data = request.get_json()
    folder = data['folder']
    filename = data['filename']
    dart_files_dir = os.path.join(Config.STATIC_FOLDER, 'dart_files')
    screenshot_dir = Config.DART_SCREENSHOT_FOLDER
    dart_path = os.path.join(dart_files_dir, folder, filename)
    if not os.path.exists(dart_path):
        return jsonify({"error": "Dart file not found"}), 404
    def generate():
        yield f"🔧 Executing script for {folder}/{filename}...\n"
        command = [
            'python3', 'script.py',
            '--screenshot_folder', screenshot_dir,
            '--exercise_number', folder,
            '--dart_file', filename
        ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in iter(process.stdout.readline, ''):
            yield line
        process.stdout.close()
        process.wait()
        yield "\n✅ Done.\n"
    return Response(generate(), mimetype='text/plain')

@bp.route('/run-dart-group', methods=['POST'])
def run_dart_group():
    data = request.get_json()
    folder = data['folder']
    dart_files_dir = os.path.join(Config.STATIC_FOLDER, 'dart_files')
    screenshot_dir = Config.DART_SCREENSHOT_FOLDER
    dart_path = os.path.join(dart_files_dir, folder)
    if not os.path.exists(dart_path):
        return jsonify({"error": "Dart folder not found"}), 404
    def generate():
        yield f"🔧 Executing script for {folder}...\n"
        command = [
            'python3', 'script.py',
            '--dart_folder', dart_path,
            '--screenshot_folder', screenshot_dir,
            '--exercise_number', folder
        ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in iter(process.stdout.readline, ''):
            yield line
        process.stdout.close()
        process.wait()
        yield "\n✅ Group done.\n"
    return Response(generate(), mimetype='text/plain')

@bp.route('/yolo-run-dart', methods=['POST'])
def yolo_run_dart():
    data = request.get_json()
    folder = data['folder']
    filename = data['filename']
    dart_files_dir = os.path.join(Config.STATIC_FOLDER, 'yolo_dart_files')
    screenshot_dir = Config.SCREENSHOT_FOLDER
    dart_path = os.path.join(dart_files_dir, folder, filename)
    if not os.path.exists(dart_path):
        return jsonify({"error": "Dart file not found"}), 404
    def generate():
        yield f"🔧 Executing script for {folder}/{filename}...\n"
        command = [
            'python3', 'script_yolo.py',
            '--screenshot_folder', screenshot_dir,
            '--exercise_number', folder,
            '--dart_file', filename
        ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in iter(process.stdout.readline, ''):
            yield line
        process.stdout.close()
        process.wait()
        yield "\n✅ Done.\n"
    return Response(generate(), mimetype='text/plain')

@bp.route('/yolo-run-dart-group', methods=['POST'])
def yolo_run_dart_group():
    data = request.get_json()
    folder = data['folder']
    dart_files_dir = os.path.join(Config.STATIC_FOLDER, 'yolo_dart_files')
    screenshot_dir = Config.SCREENSHOT_FOLDER
    dart_path = os.path.join(dart_files_dir, folder)
    if not os.path.exists(dart_path):
        return jsonify({"error": "Dart folder not found"}), 404
    def generate():
        yield f"🔧 Executing script for {folder}...\n"
        command = [
            'python3', 'script_yolo.py',
            '--dart_folder', dart_path,
            '--screenshot_folder', screenshot_dir,
            '--exercise_number', folder
        ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in iter(process.stdout.readline, ''):
            yield line
        process.stdout.close()
        process.wait()
        yield "\n✅ Group done.\n"
    return Response(generate(), mimetype='text/plain')
