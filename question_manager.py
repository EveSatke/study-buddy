import csv
import os
from dataclasses import asdict
from question import Question

class QuestionManager():
    FILE_PATH = "data/questions.csv"
    MIN_QUESTIONS = 5

    def __init__(self):
        self.questions = []
        self.options = []
        self.type = None
        self.text = None
        self.correct_option = None
        self.correct_answer = None
        self.load_questions()


    def __str__(self):
        return f"questions: {self._questions}"

    @property
    def questions(self):
        return self._questions
        
    @questions.setter
    def questions(self, value):
        self._questions = value
    
    def load_questions(self):
        try:
            with open(self.FILE_PATH, "r") as file:
                reader = csv.DictReader(file)
                self._questions = [Question(**row) for row in reader]
        except FileNotFoundError:
            self._questions = []

    def get_question_type(self):
        print(
            "\n=== ADD QUESTIONS ===\n"
            "Select question type:\n"
            "1. Quiz\n" 
            "2. Free-form\n"
            "3. Back to Main Menu\n"
            )
        return input("Choose type (1-3): ")
      
    def get_text_input(self, prompt):
        while True:
            text = input(prompt).strip()
            if text:
                return text
            print("Input cannot be empty. Please try again.")

    def get_number_input(self, prompt, min_value, max_value):
        while True:
            try:
                number = int(input(prompt))
                if min_value <= number <= max_value:
                    return number
                print(f"Please enter a number between {min_value} to {max_value}")
            except ValueError:
                print("Invalid input. Please enter a number.")
                pass

    def generate_id(self):
        try:
            with open(self.FILE_PATH, "r") as file:
                return sum(1 for line in file)
        except FileNotFoundError:
            return 0

    def form_multiple_question(self):
        text = self.get_text_input("Enter question text: ")
        options_number = self.get_number_input("Enter number of options: ", 2, 6)

        options = []
        for num in range(options_number):
            option = self.get_text_input(f"Enter option {num + 1}: ")
            options.append(option)
        correct_option = self.get_number_input(
            f"Enter correct option number (1-{options_number}): ", 
            1, 
            options_number
            )
        
        return Question(
            id=self.generate_id(),
            type="quiz",
            text=text,
            is_active=True,
            times_shown=0,
            times_correct=0,
            options=options,
            correct_option=correct_option,
            correct_answer=None
        )
    
    def form_freeform_question(self):
        text = self.get_text_input("Enter question text: ")
        correct_answer = self.get_text_input("Enter correct answer: ")

        return Question(
            id=self.generate_id(),
            type="freeform",
            text=text,
            is_active=True,
            times_shown=0,
            times_correct=0,
            options=None,
            correct_option=None,
            correct_answer=correct_answer
        )

    def get_question_count(self):
        try:
            with open(self.FILE_PATH, "r") as file:
                return sum(1 for line in file) - 1
        except FileNotFoundError:
            return 0

    def create_question(self):
        while True:
            question_type = self.get_question_type()
            try:
                if question_type == "1":
                    print(f"\nQuestion {self.get_question_count() + 1}")
                    formed_question = self.form_multiple_question()
                elif question_type == "2":
                    print(f"\nQuestion {self.get_question_count() + 1}")
                    formed_question = self.form_freeform_question()
                elif question_type == "3":
                    return False
                else:
                    print("Invalid choice. Please try again.")
                    continue
                self.add_question(formed_question)
                return True

            except Exception as e:
                print(f"Error creating question: {e}")
                continue
            

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
    

    def has_minimum_questions(self):
        return self.get_question_count() >= self.MIN_QUESTIONS
    
    def add_questions(self):
        remaining = max((self.MIN_QUESTIONS - self.get_question_count()), 1)

        while remaining > 0:
            if self.create_question():
                remaining -= 1
            else:
                break