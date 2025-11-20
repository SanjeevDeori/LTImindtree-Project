from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Student:
    student_id: str
    name: str
    assignment_score: float
    quiz_score: float
    exam_score: float

    final_score: Optional[float] = field(default=None)
    letter_grade: Optional[str] = field(default=None)
