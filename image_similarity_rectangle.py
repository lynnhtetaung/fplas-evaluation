import os
import csv
import cv2
import numpy as np
from PIL import Image
import pytesseract
from scipy.spatial import distance as dist

def check_image_size_and_similarity(correct_image_paths, student_image_path, output_folder):
    similarity_results = []
    
    for correct_image_path in correct_image_paths:
        correct_image = Image.open(correct_image_path)
        correct_width, correct_height = correct_image.size

        student_image = Image.open(student_image_path)
        student_width, student_height = student_image.size
        threshold = 95.00

        if (student_width, student_height) == (correct_width, correct_height):
            similarity_percentage = calculate_similarity_by_SIFT(correct_image_path, student_image_path)
            similarity_results.append({'Image': os.path.basename(student_image_path), 'Similarity (%)': similarity_percentage, 'Remark': similarity_percentage})
        else:
            similarity_percentage = calculate_similarity_by_ORB(correct_image_path, student_image_path)
            if similarity_percentage >= threshold:
                similarity_results.append({'Image': os.path.basename(student_image_path), 'Similarity (%)': similarity_percentage, 'Remark': 100.00})
            else:
                similarity_results.append({'Image': os.path.basename(student_image_path), 'Similarity (%)': similarity_percentage, 'Remark': similarity_percentage})

    similarity_results.sort(key=lambda x: x['Similarity (%)'], reverse=True)
    output_csv_path = os.path.join(output_folder, 'similarity_results.csv')

    write_header = not os.path.isfile(output_csv_path)
    with open(output_csv_path, 'a', newline='') as csvfile:
        fieldnames = ['Image', 'Similarity (%)', 'Remark']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if write_header:
            writer.writeheader()

        for result in similarity_results:
            writer.writerow({'Image': result['Image'], 'Similarity (%)': f"{result['Similarity (%)']:.2f}", 'Remark': f"{result['Remark']:.2f}"})

    correct_image_path_for_highlight = correct_image_paths[0]
    highlight_image_path = highlight_image_difference(correct_image_path_for_highlight, student_image_path, output_folder)

    return {'highlight_image_path': highlight_image_path}

def calculate_similarity_by_SIFT(image1_path, image2_path):
    image1 = cv2.imread(image1_path, cv2.IMREAD_COLOR)
    image2 = cv2.imread(image2_path, cv2.IMREAD_COLOR)
    
    sift = cv2.SIFT_create()
    keypoints1, descriptors1 = sift.detectAndCompute(image1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(image2, None)

    flann = cv2.FlannBasedMatcher_create()
    matches = flann.knnMatch(descriptors1, descriptors2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    similarity = len(good_matches) / max(len(keypoints1), len(keypoints2)) * 100
    return similarity

def resize_image(image, target_width, target_height):
    return cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_AREA)

def calculate_similarity_by_ORB(image1_path, image2_path):
    image1 = cv2.imread(image1_path, cv2.IMREAD_COLOR)
    image2 = cv2.imread(image2_path, cv2.IMREAD_COLOR)
    target_width = 700
    target_height = 550
    
    image1_resized = resize_image(image1, target_width, target_height)
    image2_resized = resize_image(image2, target_width, target_height)
    
    orb = cv2.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(image1_resized, None)
    keypoints2, descriptors2 = orb.detectAndCompute(image2_resized, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)

    similarity = len(matches) / max(len(keypoints1), len(keypoints2)) * 100
    return similarity

# New function for preprocessing images for OCR
def preprocess_for_ocr(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresholded = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
    return thresholded

def compare_text(correct_image_path, student_image_path):
    correct_image = cv2.imread(correct_image_path)
    student_image = cv2.imread(student_image_path)
    
    correct_image_preprocessed = preprocess_for_ocr(correct_image)
    student_image_preprocessed = preprocess_for_ocr(student_image)

    correct_image_pil = Image.fromarray(correct_image_preprocessed)
    student_image_pil = Image.fromarray(student_image_preprocessed)

    correct_text = pytesseract.image_to_string(correct_image_pil)
    student_text = pytesseract.image_to_string(student_image_pil)

    if correct_text != student_text:
        return 'Text is different'
    else:
        return 'Text matches'

def compare_button_text(correct_image_path, student_image_path, button_coords):
    correct_image = cv2.imread(correct_image_path)
    student_image = cv2.imread(student_image_path)
    
    x, y, w, h = button_coords

    correct_button_area = crop_button_area(correct_image, x, y, w, h)
    student_button_area = crop_button_area(student_image, x, y, w, h)

    correct_button_preprocessed = preprocess_for_ocr(correct_button_area)
    student_button_preprocessed = preprocess_for_ocr(student_button_area)

    correct_button_pil = Image.fromarray(correct_button_preprocessed)
    student_button_pil = Image.fromarray(student_button_preprocessed)

    correct_text = pytesseract.image_to_string(correct_button_pil)
    student_text = pytesseract.image_to_string(student_button_pil)

    if correct_text != student_text:
        return 'Button text is different'
    else:
        return 'Button text matches'

def crop_button_area(image, x, y, w, h):
    return image[y:y+h, x:x+w]

def compare_color(image1_path, image2_path):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)
    
    hist1 = cv2.calcHist([image1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist2 = cv2.calcHist([image2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    
    hist1 = cv2.normalize(hist1, hist1).flatten()
    hist2 = cv2.normalize(hist2, hist2).flatten()
    
    color_similarity = dist.euclidean(hist1, hist2)
    
    if color_similarity > 0.2:
        return 'Color is different'
    else:
        return 'Color matches'

def highlight_image_difference(image1_path, image2_path, output_folder):
    border_width = 10  # Border width in pixels

    correct_image = cv2.imread(image1_path)
    student_image = cv2.imread(image2_path)

    if correct_image.shape == student_image.shape:
        difference = cv2.absdiff(correct_image, student_image)
    else:
        target_width = 700
        target_height = 550
        
        correct_image_resized = resize_image(correct_image, target_width, target_height)
        student_image_resized = resize_image(student_image, target_width, target_height)
        
        difference = cv2.absdiff(correct_image_resized, student_image_resized)

    gray_difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray_difference, 30, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    result_copy = student_image.copy()
    label_count = 1

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(result_copy, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Position the label text to the right of the rectangle
        text_x = x + w + 10  # Position the text 10 pixels to the right of the rectangle
        text_y = y + h // 2  # Vertically center the text with the box

        # Display larger and bolder label text
        cv2.putText(result_copy, f'Diff-{label_count}', (text_x, text_y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3, cv2.LINE_AA)
        label_count += 1

    output_path_name = os.path.join(output_folder, os.path.basename(image2_path))

    if os.path.exists(output_path_name):
        os.remove(output_path_name)
        
    cv2.imwrite(output_path_name, result_copy)
    
    return output_path_name

