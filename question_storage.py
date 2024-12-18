import csv
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
                        question = Quiz.fromCsvRow(row)
                    else:
                        question = Freeform.fromCsvRow(row)
                    questions.append(question)
        except ValueError as e:
            print(f"ValueError: Incorrect data format in file. {e}")
        except KeyError as e:
            print(f"KeyError: Missing expected key in data. {e}")
        except SyntaxError as e:
            print(f"SyntaxError: Syntax issue in data parsing. {e}")
        except FileNotFoundError:
            print("FileNotFoundError: The specified file was not found.")
        return questions

    def save_questions(self, questions: List[Quiz | Freeform]):
        with open(self.file_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for question in questions:
                writer.writerow(question.to_dict())

    def add_question(self, question: Quiz | Freeform):
        if not os.path.isfile(self.file_path) or os.path.getsize(self.file_path) == 0:
            with open(self.file_path, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
        
        with open(self.file_path, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerow(question.to_dict())