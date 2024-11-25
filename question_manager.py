import csv
import os
from question import Question

class QuestionManager(Question):
    file_path = "data/questions.csv"
    def __init__(self):
        self.options = []
        self.type = None
        self.text = None
        self.correct_option = None
        self.correct_answer = None
        
        print("=== ADD QUESTIONS ===")
        print("Select question type:\n 1. Quiz\n 2. Free-form Text\n 3. Back to Main Menu\n")
        question_type = input("Choose type (1-3): ")
        if question_type == "1":
            self.type = "multiple_choice"
            self.text = input("Enter question text: ")
            self.options_number = int(input("Enter number of options: "))
            for num in range(self.options_number):
                self.option = input(f"Enter option {num + 1}: ")
                self.options.append(self.option)
            self.correct_option = int(input(f"Enter correct option number (1-{self.options_number}): "))
            print()
            print("Question added successfully!")
            print()

        elif question_type == "2":
            self.type = "freeform"
            self.text = input("Enter question text: ")
            self.correct_answer = input("Enter correct answer: ")
            print()
            print("Question added successfully!")
            print()
        elif question_type == "3":
            print()
            return

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
