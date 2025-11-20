"""
services package

This package contains all service modules responsible for:
- Loading CSV data (loader.py)
- Applying grading strategy using polymorphism (analyzer.py)
- Reporting results to JSON and console (reporter.py)
"""

from .loader import load_students_from_csv
from .analyzer import GradingStrategy, SimpleAverageStrategy, WeightedExamHeavyStrategy, apply_grading
from .reporter import save_results_as_json, print_summary

__all__ = [
    "load_students_from_csv",
    "GradingStrategy",
    "SimpleAverageStrategy",
    "WeightedExamHeavyStrategy",
    "apply_grading",
    "save_results_as_json",
    "print_summary",
]
