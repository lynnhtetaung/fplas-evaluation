import os
import shutil

# Moodle Directory
base_dir = "/home/lynnhtetaung/Desktop/StudentAnswerFiles_June12/情報化社会と技術 (2025098682)-Exercise4-1760790"
# YOLO or Image Processing Student Files
destination_dir = "/home/lynnhtetaung/Documents/develop/plas/fplas-evaluation/static/dart_files"

# Change destination path for your folder
extracted_dir = os.path.join(destination_dir, "p4")
os.makedirs(extracted_dir, exist_ok=True)

# Traverse each subfolder
for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            if os.path.isfile(file_path):
                dest_path = os.path.join(extracted_dir, f"{file_name}")
                shutil.copy2(file_path, dest_path)
                print(f"Copied: {file_path} → {dest_path}")

