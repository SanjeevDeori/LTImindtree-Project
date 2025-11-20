from pathlib import Path
import argparse

from services.loader import load_students_from_csv
from services.analyzer import (
    SimpleAverageStrategy,
    WeightedExamHeavyStrategy,
    apply_grading,
)
from services.reporter import (
    save_results_as_json,
    print_summary,
    print_top_students,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Student grading system using CSV input."
    )

    parser.add_argument(
        "-i", "--input",
        type=str,
        default="data/students.csv",
        help="Path to input CSV file (default: data/students.csv)",
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default="data/results.json",
        help="Path to output JSON file (default: data/results.json)",
    )

    parser.add_argument(
        "-s", "--strategy",
        choices=["simple", "weighted"],
        default="simple",
        help="Grading strategy to use: simple | weighted (default: simple)",
    )

    return parser.parse_args()


def choose_strategy(name: str):
    if name == "weighted":
        return WeightedExamHeavyStrategy()
    return SimpleAverageStrategy()


def main():
    args = parse_args()

    csv_path = Path(args.input)
    json_path = Path(args.output)

    print(f"[app] Loading data from: {csv_path}")
    students = load_students_from_csv(csv_path)

    if not students:
        print("[app] No students loaded. Exiting.")
        return

    strategy = choose_strategy(args.strategy)
    print(f"[app] Using grading strategy: {args.strategy}")
    apply_grading(students, strategy)

    save_results_as_json(students, json_path)
    print_summary(students)
    print_top_students(students, top_n=3)

    print(f"\n[app] Final JSON saved to: {json_path.resolve()}")


if __name__ == "__main__":
    main()
