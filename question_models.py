from abc import ABC, abstractmethod
from typing import List
import ast

class Question(ABC):
    def __init__(self, id, type, text, is_active, times_shown, times_correct):
        self.id = id
        self.type = type
        self.text = text
        self.is_active = is_active
        self.times_shown = times_shown
        self.times_correct = times_correct

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer")
        self._id = value

    @property
    def type(self) -> str:
        return self._type   
    
    @type.setter
    def type(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Type must be a string")
        self._type = value

    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Text must be a string")
        self._text = value

    @property
    def is_active(self) -> bool:
        return self._is_active
    
    @is_active.setter
    def is_active(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("Is active must be a boolean")
        self._is_active = value

    @property
    def times_shown(self) -> int:
        return self._times_shown
    
    @times_shown.setter
    def times_shown(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Times shown must be an integer")
        self._times_shown = value

    @property
    def times_correct(self) -> int:
        return self._times_correct
    @times_correct.setter
    def times_correct(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Times correct must be an integer")
        self._times_correct = value

    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def fromCsvRow(row):
        pass


class Quiz(Question):
    def __init__(self, id, type, text, is_active, times_shown, times_correct, options, correct_option):
        super().__init__(id, type, text, is_active, times_shown, times_correct)
        self.options = options
        self.correct_option = correct_option

    @staticmethod
    def fromCsvRow(row):
        return Quiz(
            id=int(row["id"]),
            type=row["type"],
            text=row["text"],
            is_active=row["is_active"] == 'True',
            times_shown=int(row["times_shown"]),
            times_correct=int(row["times_correct"]),
            options=ast.literal_eval(row["options"]),
            correct_option=int(row["correct_option"])
        )

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "text": self.text,
            "is_active": self.is_active,
            "times_shown": self.times_shown,
            "times_correct": self.times_correct,
            "options": self.options,
            "correct_option": self.correct_option
        }
    
    
    @property
    def options(self) -> List[str]:
        return self._options
    
    @options.setter
    def options(self, value: List[str]):
        if not isinstance(value, List):
            raise ValueError("Options must be a list")
        self._options = value

    @property
    def correct_option(self) -> int:
        return self._correct_option
    
    @correct_option.setter
    def correct_option(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Correct option must be an integer")
        self._correct_option = value


class Freeform(Question):
    def __init__(self, id, type, text, is_active, times_shown, times_correct, correct_answer):
        super().__init__(id, type, text, is_active, times_shown, times_correct)
        self.correct_answer = correct_answer

    @staticmethod
    def fromCsvRow(row):
        return Freeform(
            id=int(row["id"]),
            type=row["type"],
            text=row["text"],
            is_active=row["is_active"] == 'True',
            times_shown=int(row["times_shown"]),
            times_correct=int(row["times_correct"]),
            correct_answer=row["correct_answer"]
        )

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "text": self.text,
            "is_active": self.is_active,
            "times_shown": self.times_shown,
            "times_correct": self.times_correct,
            "correct_answer": self.correct_answer
        }

    @property
    def correct_answer(self) -> str:
        return self._correct_answer
    
    @correct_answer.setter
    def correct_answer(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Correct answer must be a string")
        self._correct_answer = value
