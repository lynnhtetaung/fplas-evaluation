import cv2
import pytesseract
import numpy as np

# Path to your image

image_path = '/home/lynnhtetaung/Documents/develop/plas/flutter_app/assets/station.jpg'

# Load image
img = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to get a binary image (optional but helps OCR)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(thresh)

# List of keywords to look for
keywords = ['button', 'text', 'dropdown', 'okayama']
# Initialize the score
score = 0

# Check if the image contains any known keywords for buttons, text, or dropdowns
for keyword in keywords:
    if keyword.lower() in text.lower():
        score += 25  # Add 25% to the score for each found keyword

# Optionally, you can also find contours of button-like regions using OpenCV:
# Detect contours that could represent button-like regions
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# For each detected contour, check if it is a button-like area
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w > 50 and h > 20:  # You can adjust the size as per your requirement
        # Draw a rectangle around the button-like area
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Crop and apply OCR to the button-like area to extract its text
        button_area = img[y:y + h, x:x + w]
        button_text = pytesseract.image_to_string(button_area)

        # Check if the button contains any of the keywords
        if any(keyword.lower() in button_text.lower() for keyword in keywords):
            score += 25  # Add 25% to the score for detected button text

# Final Score Calculation
if score > 100:
    score = 100  # Ensure the score does not exceed 100%

print(f"Final detection score: {score}%")

# Show the image with detected button areas (for visualization)
cv2.imshow('Detected Buttons', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
