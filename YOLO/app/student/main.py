from ultralytics import YOLO
from flask import Flask, request, jsonify

app = Flask(__name__)
model = YOLO("/app/models/best.pt")  # Load YOLO model

@app.route("/detect", methods=["POST"])
def detect():
    file = request.files['image']
    img_path = f"/app/uploads/{file.filename}"
    file.save(img_path)

    # Run YOLO detection
    results = model(img_path)
    detected = [
        {"class": int(box.cls[0]), "bbox": box.xyxy[0].tolist(), "conf": float(box.conf[0])}
        for box in results[0].boxes
    ]

    return jsonify(detected)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
