import os
import logging
from ultralytics import YOLO

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the model path
MODEL_DIR = os.path.join('models', 'YOLO', 'flutter_basic')
MODEL_PATH = os.path.join(MODEL_DIR, 'best.pt')

# Define the default error image path
ERROR_IMAGE_PATH = os.path.join('static', 'error_images', '404_error_image.png')

# Log the model loading step
logging.info(f"Loading YOLOv8 model from {MODEL_PATH}")
yolo_model = YOLO(MODEL_PATH)

def detect_components(image_path):
    """
    Detect components in the UI screenshot using the YOLOv8 model.
    """
    logging.info(f"Running YOLOv8 inference on image: {image_path}")
    try:
        results = yolo_model(image_path)  # Run inference on the image

        # Extract detected classes
        detected_classes = [yolo_model.names[int(box.cls)] for box in results[0].boxes]
        logging.info(f"Detected classes: {detected_classes}")

        required_classes = ['input_box', 'button', 'dropdown']  # Define your component classes
        detected_count = sum(1 for cls in required_classes if cls in detected_classes)
        logging.info(f"Detected components count: {detected_count}/{len(required_classes)}")

        # Calculate percentage of detected components
        percentage = (detected_count / len(required_classes)) * 100
        logging.info(f"Detection percentage: {percentage}%")

        if percentage == 0:
            logging.warning(f"No required components detected. Returning error image: {ERROR_IMAGE_PATH}")
            return percentage, ERROR_IMAGE_PATH

        # Generate the rendered image with bounding boxes
        rendered_image_path = os.path.join('static', 'output', f'result_{os.path.basename(image_path)}')
        results[0].save(rendered_image_path)
        logging.info(f"Saved rendered image with bounding boxes at {rendered_image_path}")
        
        return percentage, rendered_image_path

    except Exception as e:
        logging.error(f"Error during YOLOv8 inference: {e}")
        return 0, ERROR_IMAGE_PATH
