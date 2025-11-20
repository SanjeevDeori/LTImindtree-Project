import json
from pathlib import Path
from collections import Counter
from typing import List

from models import Student


def save_results_as_json(students: List[Student], output_path: Path) -> None:
    """Saves final JSON using json.dump."""
    data = [
        {
            "id": s.student_id,
            "name": s.name,
            "assignment": s.assignment_score,
            "quiz": s.quiz_score,
            "exam": s.exam_score,
            "final_score": s.final_score,
            "letter_grade": s.letter_grade,
        }
        for s in students
    ]

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"[reporter] Saved {len(students)} records to {output_path}")


def print_summary(students: List[Student]) -> None:
    """Prints on-screen summary."""
    print("\n===== Grade Summary =====")
    if not students:
        print("No data.")
        return

    grades = [s.letter_grade for s in students if s.letter_grade is not None]
    counts = Counter(grades)

    for grade in sorted(counts.keys()):
        print(f"Grade {grade}: {counts[grade]} student(s)")

    avg_final = sum(s.final_score for s in students if s.final_score is not None) / len(
        students
    )
    print(f"\nAverage final score: {avg_final:.2f}")
