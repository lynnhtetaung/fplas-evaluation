## YOLO Installation:
- Added ultralytics library for YOLOv8.
- You can now use YOLO functionality in your Python scripts.

## YOLO Weights:
- Include the best.pt file (your YOLOv8 model weights) by copying it into the Docker image.
- Store weights in /app/models/ for easier access

## YOLOv8 Integration:
- Kept ultralytics installed via pip for YOLOv8 support.
- Added a COPY instruction to include your trained YOLOv8 model weights (best.pt).
- Focus on Python and Flask:
- Retained Flask and other Python dependencies for your API and inference logic.
- You can extend this base Dockerfile to handle YOLOv8 inference.

## Directory structure
- /app/
  ├── main.py           # Your Flask API or main script for YOLO
  ├── models/
  │     └── best.pt     # YOLOv8 trained model weights
  ├── requirements.txt  # Optional, if you prefer managing dependencies via a file
  └── Dockerfile 

## Docker image
- docker build -t yolo-flask-app .

## Docker container 
- docker run -p 5000:5000 yolo-flask-app

## requirements.txt 
- flask: Framework for creating your API to serve YOLO inference.
- watchdog: Optional but useful if you monitor directories or files dynamically.
- opencv-python: Useful for pre- and post-processing images, like resizing or augmenting input.
- Pillow: For general image manipulation, like cropping or format conversion.
- pytest-playwright: If you are using Playwright for browser automation or UI validation.
- ultralytics: The core YOLOv8 library for inference and training.

## Train Dataset and Generate Model (Run from any directory)
yolo task=detect mode=train data=/home/lynnhtetaung/Documents/develop/plas/flutter_app/YOLO/flutter-basic/dataset/data.yaml model=yolov8n.pt epochs=25 imgsz=416 plots=True
