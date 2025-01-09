from flask import Flask, render_template, request, jsonify
import os
import logging
import subprocess

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the ui_scripts folder path
YOLO_dir = '/home/lynnhtetaung/Documents/develop/plas/flutter_app/YOLO/app/teacher/ui_scripts'

# Route for flutter component generation
@app.route("/")
def index():
    return render_template("index.html")

# Define a function to run Python scripts and return the output
def run_python_script(script_name):
    ui_scripts_path = os.path.join(YOLO_dir, script_name)
    logging.info(f"UI Scripts Location: {ui_scripts_path}")
    try:
        result = subprocess.run(['python3', ui_scripts_path], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/train", methods=["POST"])
def train_model():
    data_path = request.json.get("data_path")
    epochs = request.json.get("epochs", 25)
    img_size = request.json.get("imgsz", 416)

    if not data_path or not os.path.exists(data_path):
        return jsonify({"error": "Invalid dataset path"}), 400

    try:
        # YOLO training command
        command = [
            "yolo",
            "task=detect",
            "mode=train",
            f"data={data_path}",
            "model=yolov8n.pt",
            f"epochs={epochs}",
            f"imgsz={img_size}",
            "plots=True"
        ]
        subprocess.run(command, check=True)
        logging.info("Model trained successfully")
        return jsonify({"message": "Model trained successfully"})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Training failed: {str(e)}"}),         

# Route to render model-train.html
@app.route('/model-train')
def train_model_view():
    return render_template('model-train.html')

# Routes for each generate script
@app.route("/generate/icon", methods=["POST"])
def generate_icon():
    output = run_python_script("icon_generate.py")
    logging.info(f"Generate icon output: {output}")
    return jsonify({"output": output})

@app.route("/generate/checkbox", methods=["POST"])
def generate_checkbox():
    output = run_python_script("checkbox_generate.py")
    logging.info(f"Generate checkbox output: {output}")
    return jsonify({"output": output})

@app.route("/generate/text", methods=["POST"])
def generate_text():
    output = run_python_script("text_generate.py")
    logging.info(f"Generate text output: {output}")
    return jsonify({"output": output})

@app.route("/generate/dropdown", methods=["POST"])
def generate_dropdown():
    output = run_python_script("dropdown_generate.py")
    logging.info(f"Generate dropdown output: {output}")
    return jsonify({"output": output})

@app.route("/generate/button", methods=["POST"])
def generate_button():
    output = run_python_script("button_generate.py")
    logging.info(f"Generate button output: {output}")
    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
