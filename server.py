from flask import Flask, render_template, request, Response, jsonify
import os
import subprocess

app = Flask(__name__)

OUTPUT_FOLDER = 'static/output'
SCREENSHOT_FOLDER = 'static/screenshots'

@app.route('/')
def compare_list():
    # Get filenames from both folders
    output_files = set(os.listdir(OUTPUT_FOLDER))
    screenshot_files = set(os.listdir(SCREENSHOT_FOLDER))

    # Only show files that exist in both folders
    common_files = sorted(list(output_files & screenshot_files))

    return render_template('list.html', projects=common_files)

# Route for flutter component generation
@app.route("/")
def index():
    return render_template("index.html")
    
@app.route('/dart-thumbnails')
def dart_thumbnails():
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

    return render_template('dart_thumbnails.html', projects=projects)

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
            'python3', 'script_single.py',
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
            '--dart_content', dart_path,
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
