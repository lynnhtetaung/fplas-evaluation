import os
import csv

def _write_csv(csv_path, student_id, exercise, remark):
    file_exists = os.path.exists(csv_path)
    with open(csv_path, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["studentID", "exercise", "remark"])
        writer.writerow([student_id, exercise, remark])
