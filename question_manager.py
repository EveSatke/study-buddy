import csv
import os
from question import Question

class QuestionManager(Question):
    file_path = "data/questions.csv"
    def __init__(self):
        question_type = input("Enter the type of question:\n 1. Quiz\n 2. Freeform\n")
        if question_type == "1":
            self.type = "multiple_choice"
            self.text = input("Enter question text: ")
            self.options = input("Enter answer options, seperated by ',' \n").split(",")
            self.correct_option = input("Enter correct option number: ")
        elif question_type == "2":
            self.type = "freeform"
            self.text = input("Enter question text: ")
            self.correct_answer = input("Enter correct answer: ")

    def add_question(self):
        fieldnames = ["id", "type", "text", "is_active", "times_shown", "times_correct", "options", "correct_option", "correct_answer"]
        if not os.path.isfile(self.file_path):
            with open(self.file_path, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
            
        with open(self.file_path, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({
                "id": self._generate_id(),
                "type": self.type,
                "text": self.text, 
                "is_active": True, 
                "times_shown": 0, 
                "times_correct": 0, 
                "options": self.options, 
                "correct_option": self.correct_option,
                "correct_answer": self.correct_answer
                })

    def _generate_id(self):
        try:
            with open(self.file_path, "r") as file:
                return sum(1 for line in file)
        except FileNotFoundError:
            return 0
