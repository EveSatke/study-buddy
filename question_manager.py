import csv
import os
from dataclasses import asdict
from question import Question

class QuestionManager():
    FILE_PATH = "data/questions.csv"
    MIN_QUESTIONS = 5

    def __init__(self):
        self.options = []
        self.type = None
        self.text = None
        self.correct_option = None
        self.correct_answer = None
        
    def create_question(self):
        while True:
            print(
            "\n=== ADD QUESTIONS ===\n"
            "Select question type:\n"
            "1. Quiz\n" 
            "2. Free-form\n"
            "3. Back to Main Menu\n")

            question_type = input("Choose type (1-3): ")
            print(f"\nQuestion {self.get_question_count() + 1}")
            if question_type == "1":
                self.text = input("Enter question text: ")
                while True:
                    try:
                        self.options_number = int(input("Enter number of options: "))
                        for num in range(self.options_number):
                            self.option = input(f"Enter option {num + 1}: ")
                            self.options.append(self.option)
                        self.correct_option = int(input(f"Enter correct option number (1-{self.options_number}): "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue
                multiple_question = Question(
                    id=self._generate_id(),
                    type="quiz",
                    text=self.text,
                    is_active=True,
                    times_shown=0,
                    times_correct=0,
                    options=self.options,
                    correct_option=self.correct_option,
                    correct_answer=None
                )
                self.add_question(multiple_question)

            elif question_type == "2":
                self.text = input("Enter question text: ")
                self.correct_answer = input("Enter correct answer: ")
                freeform_question = Question(
                    id=self._generate_id(),
                    type="freeform",
                    text=self.text,
                    is_active=True,
                    times_shown=0,
                    times_correct=0,
                    options=None,
                    correct_option=None,
                    correct_answer=self.correct_answer
                )
                self.add_question(freeform_question)
            elif question_type == "3":
                return False
            else:
                print("Invalid choice. Please try again.")
                continue
            return True

    def add_question(self, question_data: Question):
        fieldnames = ["id", "type", "text", "is_active", "times_shown", "times_correct", "options", "correct_option", "correct_answer"]
        if not os.path.isfile(self.FILE_PATH):
            with open(self.FILE_PATH, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
            
        with open(self.FILE_PATH, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(asdict(question_data))
        print("\nQuestion added successfully!\n")
    

    def _generate_id(self):
        try:
            with open(self.FILE_PATH, "r") as file:
                return sum(1 for line in file)
        except FileNotFoundError:
            return 0

    def get_question_count(self):
        try:
            with open(self.FILE_PATH, "r") as file:
                return sum(1 for line in file) - 1
        except FileNotFoundError:
            return 0

    def has_minimum_questions(self):
        return self.get_question_count() >= self.MIN_QUESTIONS