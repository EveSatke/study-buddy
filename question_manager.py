import csv
import os
import ast
from typing import List
from question_models import Quiz, Freeform
from utils.helpers import get_text_input, get_number_input
from question_storage import QuestionStorage

class QuestionManager():
    FILE_PATH = "data/questions.csv"
    FIELDNAMES = ["id", "type", "text", "is_active", "times_shown", "times_correct", "options", "correct_option", "correct_answer"]
    MIN_QUESTIONS = 5

    def __init__(self):
        self.storage = QuestionStorage(self.FILE_PATH, self.FIELDNAMES)
        self.questions = self.storage.load_questions()

    def __str__(self):
        return f"questions: {[q.text for q in self.questions]}"

    def get_question_type(self):
        print(
            "\n=== ADD QUESTIONS ===\n"
            "Select question type:\n"
            "1. Quiz\n" 
            "2. Free-form\n"
            "3. Back to Main Menu\n"
            )
        return input("Choose type (1-3): ")
      

    def _generate_id(self):
        try:
            with open(self.FILE_PATH, "r") as file:
                return sum(1 for line in file)
        except FileNotFoundError:
            return 1

    def form_quiz_question(self):
        text = get_text_input("Enter question text: ")
        options_number = get_number_input("Enter number of options: ", 2, 6, allow_exit=False)

        options = []
        for num in range(options_number):
            option = get_text_input(f"Enter option {num + 1}: ")
            options.append(option)
        correct_option = get_number_input(
            f"Enter correct option number (1-{options_number}): ", 
            1, 
            options_number,
            allow_exit = False
            )
        
        return Quiz(
            id=self._generate_id(),
            type="quiz",
            text=text,
            is_active=True,
            times_shown=0,
            times_correct=0,
            options=options,
            correct_option=correct_option,
        )
    
    def form_freeform_question(self):
        text = get_text_input("Enter question text: ")
        correct_answer = get_text_input("Enter correct answer: ")

        return Freeform(
            id=self._generate_id(),
            type="freeform",
            text=text,
            is_active=True,
            times_shown=0,
            times_correct=0,
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
                    formed_question = self.form_quiz_question()
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
            

    def add_question(self, question_data: Quiz | Freeform):
        self.storage.add_question(question_data)
        self.questions.append(question_data)
        print("\n✅Question added successfully!\n")
    

    def has_minimum_questions(self):
        return self.get_question_count() >= self.MIN_QUESTIONS
    
    def add_questions(self):
        remaining = max((self.MIN_QUESTIONS - self.get_question_count()), 1)

        while remaining > 0:
            if self.create_question():
                remaining -= 1
            else:
                break

    def display_questions_status(self):
        questions = self.questions
        print("\n=== ENABLE/DISABLE QUESTIONS ===\n")

        print("Current Questions:")
        print(f"{'ID':<4} {'Status':<10} {'Type':<10} {'Question Preview':<50}")
        print("-" * 74)

        for question in questions:
            status = "[ACTIVE]" if question.is_active else "[INACTIVE]"
            preview = question.text[:40] + "..." if len(question.text) > 40 else question.text
            print(f"{question.id:<4} {status:<10} {question.type:<10} {preview:<50}")

        return questions
    
    def get_question_details(self, questions):
        question_id = get_number_input("\nEnter question ID to toggle status (or 'q' to quit): ", 1, self.get_question_count(), allow_exit=True)
        if question_id == "q":
            return None
            
        for q in questions:
            if int(q.id) == question_id:
                print(
                    "Question Details:\n"
                    "----------------\n"
                    f"ID: {q.id}\n"
                    f"Type: {q.type}\n"
                    f"Status: {"[ACTIVE]" if q.is_active else "[INACTIVE]"}\n"
                    f"Text: {q.text}"
                )
                if q.type == "quiz":
                    print("Options:")
                    for i, option in enumerate(q.options, 1):
                        print(f"{i}. {option}")
                    print(f"Correct option: {q.correct_option}")
                else:
                    print(f"Correct answer: {q.correct_answer}")
                return q
                
        print(f"\nNo question found with ID {question_id}")
        return None
    
                    
    def manage_question_status(self):
        while True:
            questions = self.display_questions_status()
            selected_question = self.get_question_details(questions)
            if selected_question is None:
                break
            action = "disable" if selected_question.is_active else "enable"
            user_input = get_text_input(f"\nDo you want to {action} this question? (y/n): ")
            if user_input.lower() == "y":
                selected_question.is_active = not selected_question.is_active
                for i, q in enumerate(self.questions):
                    if q.id == selected_question.id:
                        self.questions[i] = selected_question
                        break
                self.update_questions(self.questions)

    def update_questions(self, questions_data: List[Quiz | Freeform]):
        self.storage.save_questions(questions_data)