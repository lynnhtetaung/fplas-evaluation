from flask import Flask, render_template, request, Response, jsonify, send_file, send_from_directory
import os
import csv
import subprocess

app = Flask(__name__)

OUTPUT_FOLDER = 'static/output'
SCREENSHOT_FOLDER = 'static/screenshots'
CSV_PATH = os.path.join(app.root_path, 'static/output/similarity_results.csv')
YOLO_CSV_PATH = os.path.join(app.root_path, 'static/output/results.csv')

@app.route('/student_scores')
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

@app.route('/yolo_student_scores')
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

@app.route('/save-student-scores', methods=['POST'])
def save_student_scores():
    data = request.json
    with open(CSV_PATH, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Student Image', 'Similarity (%)', 'Score', 'Remark'])
        writer.writerows(data)
    return jsonify({'status': 'success'})

@app.route('/save-yolo-scores', methods=['POST'])
def save_yolo_scores():
    data = request.json
    with open(YOLO_CSV_PATH, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Student Image', 'Similarity (%)', 'Score', 'Remark'])
        writer.writerows(data)
    return jsonify({'status': 'success'})

@app.route('/download-scores')
def download_scores():
    return send_file(CSV_PATH, as_attachment=True, download_name='student_scores.csv')

@app.route('/download-yolo-scores')
def download_yolo_scores():
    return send_file(YOLO_CSV_PATH, as_attachment=True, download_name='yolo_student_scores.csv')

@app.route('/compare_list')
def compare_list():
    # Get filenames from both folders
    output_files = set(os.listdir(OUTPUT_FOLDER))
    screenshot_files = set(os.listdir(SCREENSHOT_FOLDER))

    # Only show files that exist in both folders
    common_files = sorted(list(output_files & screenshot_files))

    return render_template('list.html', projects=common_files)

@app.route("/yolo_list")
def yolo_list():
    base_path = os.path.join(app.static_folder, "screenshots")
    categories = {}

    # Loop through subfolders like 'p1', 'p2'
    for folder in sorted(os.listdir(base_path)):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path):
            images = sorted([
                img for img in os.listdir(folder_path)
                if img.endswith((".png", ".jpg", ".jpeg"))
            ])
            categories[folder] = images

    return render_template("yolo_list.html", categories=categories)

# Route for flutter component generation
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/yolo_evaluation")
def yolo_evaluation():
    return render_template("yolo_evaluation.html")

@app.route("/image_evaluation")
def image_evaluation():
    return render_template("image_evaluation.html")
    
@app.route('/student_answers')
def student_answers():
    root_folder = os.path.join(app.root_path, 'static', 'dart_files')
    projects = {}

    for folder in sorted(os.listdir(root_folder)):
        folder_path = os.path.join(root_folder, folder)
        if os.path.isdir(folder_path):
            entries = []
            for file in sorted(os.listdir(folder_path)):
                if file.endswith('.dart'):
                    with open(os.path.join(folder_path, file), 'r') as f:
                        code_preview = f.read(300)  # Preview first 300 characters
                    entries.append({
                        'dart': file,
                        'name': file.rsplit('.', 1)[0],
                        'preview': code_preview
                    })
            if entries:
                projects[folder] = entries

    return render_template('student_answers.html', projects=projects)

@app.route('/yolo_student_answers')
def yolo_student_answers():
    root_folder = os.path.join(app.root_path, 'static', 'yolo_dart_files')
    projects = {}

    for folder in sorted(os.listdir(root_folder)):
        folder_path = os.path.join(root_folder, folder)
        if os.path.isdir(folder_path):
            entries = []
            for file in sorted(os.listdir(folder_path)):
                if file.endswith('.dart'):
                    with open(os.path.join(folder_path, file), 'r') as f:
                        code_preview = f.read(300)  # Preview first 300 characters
                    entries.append({
                        'dart': file,
                        'name': file.rsplit('.', 1)[0],
                        'preview': code_preview
                    })
            if entries:
                projects[folder] = entries

    return render_template('yolo_student_answers.html', projects=projects)

@app.route('/run-dart', methods=['POST'])
def run_dart():
    data = request.get_json()
    folder = data['folder']
    filename = data['filename']

    base_dir = os.path.join(app.root_path, 'static', 'dart_files')
    screenshot_dir = os.path.join(app.root_path, 'static', 'screenshots')

    dart_path = os.path.join(base_dir, folder, filename)
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

@app.route('/run-dart-group', methods=['POST'])
def run_dart_group():
    data = request.get_json()
    folder = data['folder']
    base_dir = os.path.join(app.root_path, 'static', 'dart_files')
    screenshot_dir = os.path.join(app.root_path, 'static', 'screenshots')

    dart_path = os.path.join(base_dir, folder)

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
