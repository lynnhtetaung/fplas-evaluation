import os
import csv
from PIL import Image
import cv2
import numpy as np
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
    kp1, des1 = sift.detectAndCompute(image1, None)
    kp2, des2 = sift.detectAndCompute(image2, None)
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])
    similarity = len(good) / max(len(kp1), len(kp2)) * 100 if max(len(kp1), len(kp2)) > 0 else 0
    return similarity

def calculate_similarity_by_ORB(image1_path, image2_path):
    image1 = cv2.imread(image1_path, cv2.IMREAD_COLOR)
    image2 = cv2.imread(image2_path, cv2.IMREAD_COLOR)
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(image1, None)
    kp2, des2 = orb.detectAndCompute(image2, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    similarity = len(matches) / max(len(kp1), len(kp2)) * 100 if max(len(kp1), len(kp2)) > 0 else 0
    return similarity

def highlight_image_difference(correct_image_path, student_image_path, output_folder):
    # Dummy implementation for highlight, replace with your logic
    return None
