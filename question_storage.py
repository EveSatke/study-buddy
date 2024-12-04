import csv
import ast
import os
from typing import List
from question_models import Quiz, Freeform

class QuestionStorage:
    def __init__(self, file_path: str, fieldnames: List[str]):
        self.file_path = file_path
        self.fieldnames = fieldnames

    def load_questions(self) -> List[Quiz | Freeform]:
        questions = []
        try:
            with open(self.file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["type"] == "quiz":
                        question = Quiz(
                            id=int(row["id"]),
                            type=row["type"],
                            text=row["text"],
                            is_active=row["is_active"] == 'True',
                            times_shown=int(row["times_shown"]),
                            times_correct=int(row["times_correct"]),
                            options=ast.literal_eval(row["options"]),
                            correct_option=int(row["correct_option"])
                        )
                    else:
                        question = Freeform(
                            id=int(row["id"]),
                            type=row["type"],
                            text=row["text"],
                            is_active=row["is_active"] == 'True',
                            times_shown=int(row["times_shown"]),
                            times_correct=int(row["times_correct"]),
                            correct_answer=row["correct_answer"]
                        )
                    questions.append(question)
        except (ValueError, KeyError, SyntaxError) as e:
            print(f"Error loading question: {e}")
        except FileNotFoundError:
            pass
        return questions

    def save_questions(self, questions: List[Quiz | Freeform]):
        with open(self.file_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for question in questions:
                writer.writerow(question.to_dict())

    def add_question(self, question: Quiz | Freeform):
        if not os.path.isfile(self.file_path):
            with open(self.file_path, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
        
        with open(self.file_path, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerow(question.to_dict())