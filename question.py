from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Question:
    id: int
    type: str
    text: str
    is_active: bool
    times_shown: int
    times_correct: int
    options: Optional[List]
    correct_option: Optional[int] 
    correct_answer: Optional[str]
