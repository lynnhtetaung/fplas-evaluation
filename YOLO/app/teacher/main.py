from flask import Flask, render_template, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

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
        return jsonify({"message": "Model trained successfully"})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Training failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
