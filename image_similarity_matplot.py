import os
import csv
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
from pytesseract import Output


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

    correct_image_path_for_highlight = correct_image_paths[0]  # You may choose the correct image to highlight differences
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

def highlight_image_difference(image1_path, image2_path, output_folder):
    # Load both images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Convert both images to grayscale for better OCR results
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Step 1: Highlight color differences
    color_difference = cv2.absdiff(image1, image2)
    gray_difference = cv2.cvtColor(color_difference, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray_difference, 30, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Step 2: Use OCR to detect text differences (font/word differences)
    text_image1 = pytesseract.image_to_data(gray_image1, output_type=Output.DICT)
    text_image2 = pytesseract.image_to_data(gray_image2, output_type=Output.DICT)

    # Highlight the OCR-detected text differences between the two images
    highlighted_image = image2.copy()

    # Iterate over words in image1
    for i in range(len(text_image1['text'])):
        if text_image1['text'][i].strip() == '':
            continue  # Skip empty OCR results
        x1, y1, w1, h1 = text_image1['left'][i], text_image1['top'][i], text_image1['width'][i], text_image1['height'][i]

        # Check if the word is different in image2
        found_difference = True
        for j in range(len(text_image2['text'])):
            x2, y2, w2, h2 = text_image2['left'][j], text_image2['top'][j], text_image2['width'][j], text_image2['height'][j]
            if abs(x1 - x2) < 5 and abs(y1 - y2) < 5:  # Overlapping regions
                if text_image1['text'][i].strip() == text_image2['text'][j].strip():  # Text matches
                    found_difference = False
                break

        # If a difference is found, highlight the word in the second image
        if found_difference:
            cv2.rectangle(highlighted_image, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)  # Red box for word difference

    # Step 3: Combine color and text differences
    highlighted_image[mask != 0] = [0, 255, 0]  # Highlight color differences in green

    # Use matplotlib to save the result under the output folder
    output_path_name = os.path.join(output_folder, os.path.basename(image2_path))

    plt.figure(figsize=(10, 8))
    plt.imshow(cv2.cvtColor(highlighted_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for proper coloring in matplotlib
    plt.axis('off')  # Turn off axis display

    # Save the image using matplotlib
    plt.savefig(output_path_name, bbox_inches='tight', pad_inches=0)
    plt.close()  # Close the figure after saving

    return output_path_name
    
    original_image1 = cv2.imread(image1_path)
    student_image = Image.open(image2_path)
    student_width, student_height = student_image.size

    if (student_width, student_height) == (correct_width, correct_height):
        image2 = cv2.imread(image2_path)
        difference = cv2.absdiff(original_image1, image2)
    else:
        image1 = cv2.imread(org_img, cv2.IMREAD_COLOR)
        image2 = cv2.imread(image2_path, cv2.IMREAD_COLOR)
        target_width = 700
        target_height = 550
        
        resize_image1 = resize_image(image1, target_width, target_height)
        resize_image2 = resize_image(image2, target_width, target_height)
        cv2.imwrite(image2_path, resize_image2)
        
        image2 = cv2.imread(image2_path)
        difference = cv2.absdiff(resize_image1, image2)

    gray_difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray_difference, 30, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5,5), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=2)

    highlighted_image = image2.copy()
    highlighted_image[mask != 0] = [0, 0, 255]  # Highlight the differences in red

    alpha = 0.3
    result = cv2.addWeighted(image2, 1-alpha, highlighted_image, alpha, 0)

    # Plotting the image with matplotlib
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # No axis for clean image display

    # Generate the filename as per your logic or use the custom save path if provided
    output_path_name = custom_save_path if custom_save_path else os.path.join(output_folder, os.path.basename(image2_path))

    # Save the image using Matplotlib
    plt.savefig(output_path_name, bbox_inches='tight', pad_inches=0)
    plt.close()  # Close the plot to avoid memory leaks

    return output_path_name