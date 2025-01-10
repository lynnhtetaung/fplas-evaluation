import pytesseract
from PIL import Image
import cv2
import numpy as np
import os

def detect_components(image_path):
    """
    Detect components (like buttons, text, or dropdowns) in an image using OCR.
    Returns a percentage score and a result image with detected components highlighted with red boxes.
    """
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    
    # Apply sharpening filter to the image
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened = cv2.filter2D(img, -1, sharpen_kernel)

    # Convert the sharpened image to HSV color space for better masking
    hsv = cv2.cvtColor(sharpened.copy(), cv2.COLOR_BGR2HSV)
    
    # Mask out regions that are too dark (based on HSV values)
    mask_grey = cv2.inRange(hsv, (0, 0, 100), (255, 5, 255))
    
    # Build mask of non-black pixels.
    nzmask = cv2.inRange(hsv, (0, 0, 5), (255, 255, 255))
    
    # Erode the mask - all pixels around a black pixel should not be masked.
    nzmask = cv2.erode(nzmask, np.ones((3,3)))
    mask_grey = mask_grey & nzmask
    
    # Create a cleaned background image by masking non-black regions
    cleaned_bg_img = img.copy()
    cleaned_bg_img[np.where(mask_grey)] = 255  # White background where masked
    
    # Convert the image to grayscale for OCR
    gray = cv2.cvtColor(cleaned_bg_img, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to detect text in the image with bounding boxes
    custom_config = r'--oem 3 --psm 6'  # Configuration for OCR
    dpm_result = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT, config=custom_config)

    # Debug print: Check if OCR is detecting any text
    print("OCR Detected Text:", dpm_result['text'])

    # Analyze the detected text to calculate a detection score
    detected_keywords = ['Home', 'text', 'Exercise', 'subtitle', 'Business']  # Example keywords
    keyword_count = 0
    for i, word in enumerate(dpm_result['text']):
        if word.strip().lower() in detected_keywords:
            keyword_count += 1
            # Get the bounding box for each detected word
            x, y, w, h = dpm_result['left'][i], dpm_result['top'][i], dpm_result['width'][i], dpm_result['height'][i]
            
            # Draw a red rectangle around the detected word
            cleaned_bg_img = cv2.rectangle(cleaned_bg_img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red rectangle (BGR format)

    # Calculate a simple score based on how many keywords were detected
    total_keywords = len(detected_keywords)
    percentage = (keyword_count / total_keywords) * 100

    # Save the result image with bounding boxes
    result_image_path = os.path.splitext(image_path)[0] + "_with_boxes" + os.path.splitext(image_path)[1]
    cv2.imwrite(result_image_path, cleaned_bg_img)

    # Convert the result image to PIL Image for return
    result_img_pil = Image.fromarray(cv2.cvtColor(cleaned_bg_img, cv2.COLOR_BGR2RGB))

    print(f"Result image saved at: {result_image_path}")

    return percentage, result_img_pil

# Example usage:
# image_path = "path_to_your_image.jpg"
# detect_components(image_path)
