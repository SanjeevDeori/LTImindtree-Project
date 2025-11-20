import json
from pathlib import Path
from collections import Counter
from typing import List

from models import Student


def save_results_as_json(students: List[Student], output_path: Path) -> None:
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

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"[reporter] Saved {len(students)} records to {output_path}")


def print_summary(students: List[Student]) -> None:
    print("\n===== Grade Summary =====")

    if not students:
        print("No data.")
        return

    graded = [s for s in students if s.final_score is not None]
    grades = [s.letter_grade for s in graded if s.letter_grade is not None]
    counts = Counter(grades)

    for grade in sorted(counts.keys()):
        print(f"Grade {grade}: {counts[grade]} student(s)")

    avg_final = sum(s.final_score for s in graded) / len(graded)
    print(f"\nAverage final score: {avg_final:.2f}")

    passed = [s for s in graded if s.letter_grade not in ("F", None)]
    failed = [s for s in graded if s.letter_grade == "F"]

    pass_rate = (len(passed) / len(graded)) * 100
    print(f"Pass rate: {pass_rate:.1f}%  ({len(passed)} / {len(graded)})")
    print(f"Failed students: {len(failed)}")


def print_top_students(students: List[Student], top_n: int = 3) -> None:
    print(f"\nTop {top_n} students (by final score):")

    graded = [s for s in students if s.final_score is not None]
    if not graded:
        print("No graded students.")
        return

    ranked = sorted(graded, key=lambda s: s.final_score, reverse=True)[:top_n]

    for idx, s in enumerate(ranked, start=1):
        print(f"{idx}. {s.name} (ID: {s.student_id}) - {s.final_score} [{s.letter_grade}]")
