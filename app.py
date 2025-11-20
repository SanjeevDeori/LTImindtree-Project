from pathlib import Path

from services.loader import load_students_from_csv
from services.analyzer import SimpleAverageStrategy, apply_grading
from services.reporter import save_results_as_json, print_summary

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "data"   # you can choose a different folder if you want


def main():
    csv_path = DATA_DIR / "students.csv"
    json_path = OUTPUT_DIR / "results.json"

    print(f"Loading data from: {csv_path}")
    students = load_students_from_csv(csv_path)

    if not students:
        print("No students loaded. Check your CSV file.")
        return

    # Choose a grading strategy (polymorphism idea)
    strategy = SimpleAverageStrategy()
    apply_grading(students, strategy)

    # Reporting
    save_results_as_json(students, json_path)
    print_summary(students)
    print(f"\nFinal JSON saved to: {json_path}")


if __name__ == "__main__":
    main()
