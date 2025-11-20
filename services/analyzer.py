from abc import ABC, abstractmethod
from typing import List

from models import Student
from utils import to_letter_grade


class GradingStrategy(ABC):
    """Base class – allows polymorphic grading strategies."""

    @abstractmethod
    def compute_final_score(self, student: Student) -> float:
        ...


class SimpleAverageStrategy(GradingStrategy):
    """Simple average: all components have equal weight."""

    def compute_final_score(self, student: Student) -> float:
        return (student.assignment_score +
                student.quiz_score +
                student.exam_score) / 3.0


class WeightedExamHeavyStrategy(GradingStrategy):
    """Example of another strategy: exam is 60%, others 20% each."""

    def compute_final_score(self, student: Student) -> float:
        return (
            0.2 * student.assignment_score +
            0.2 * student.quiz_score +
            0.6 * student.exam_score
        )


def apply_grading(students: List[Student], strategy: GradingStrategy) -> None:
    """
    Implements grading strategy and fills each student with
    final_score + letter_grade.
    """
    for s in students:
        final = strategy.compute_final_score(s)
        s.final_score = round(final, 2)
        s.letter_grade = to_letter_grade(final)
