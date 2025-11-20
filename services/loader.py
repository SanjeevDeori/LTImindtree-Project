import csv
from pathlib import Path
from typing import List

from models import Student


def load_students_from_csv(csv_path: Path) -> List[Student]:
    """
    Validates CSV (basic checks) and loads rows using csv.DictReader.
    Returns a list of Student objects.
    """
    students: List[Student] = []
    if csv_path.is_dir():
        print(f"[loader] Given path is a directory, not a file: {csv_path}")
        return students 

    if not csv_path.exists():
        print(f"[loader] CSV file not found: {csv_path}")
        return students

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        required_cols = {"id", "name", "assignment", "quiz", "exam"}
        if not required_cols.issubset(reader.fieldnames or []):
            print(f"[loader] CSV is missing required columns: {required_cols}")
            return students

        for row in reader:
            try:
                student = Student(
                    student_id=row["id"],
                    name=row["name"],
                    assignment_score=float(row["assignment"]),
                    quiz_score=float(row["quiz"]),
                    exam_score=float(row["exam"]),
                )
                students.append(student)
            except ValueError as e:
                print(f"[loader] Skipping row due to error: {e} | row={row}")

    print(f"[loader] Loaded {len(students)} students")
    return students
