import random
from question_manager import QuestionManager
from utils.helpers import get_text_input, get_number_input

class PracticeTestManager:
    def __init__(self, question_manager:QuestionManager):
        self.question_manager = question_manager

    def calculate_weights(self, questions):
        weights = []
        min_weight = 0.1

        for question in questions:
            weight = max(min_weight, (question.times_shown - question.times_correct + 1) / (question.times_shown + 1))
            weights.append(weight)
            # print(f"Weight for {question.text}: {weight}")

        return weights
    
    def select_weighted_question(self, last_question=None):
        active_questions = [q for q in self.question_manager.questions if q.is_active]
        if not active_questions:
            return None 
        
        weights = self.calculate_weights(active_questions)
        total_weight = sum(weights)
        if total_weight == 0:
            return None
        probabilities = [w / total_weight for w in weights]
        selected_question = random.choices(active_questions, probabilities, k=1)[0]
        if selected_question == last_question and len(active_questions) > 1:
            selected_question = random.choices(active_questions, probabilities, k=1)[0]
        return selected_question
    
    def practice_mode(self):
        print("\n=== PRACTICE MODE ===")
        last_question = None
        while True:
            question = self.select_weighted_question(last_question)
            if not question:
                print("No questions available for practice.")
                break

            print(f"\nQuestion: {question.text}")
            if question.type == "quiz":
                for i, option in enumerate(question.options, 1):
                    print(f"{i}. {option}")
                answer = get_number_input(f"\nYour answer (or 'q' to quit): ", 1, len(question.options), allow_exit=True)
                if answer is None:
                    print("Exiting practice mode.")
                    break
                if answer == question.correct_option:
                    print("Correct!")
                    question.times_correct += 1
                else:
                    print(f"Incorrect! The correct option was {question.correct_option}.")
            else:
                answer = get_text_input("Your answer (or 'q' to quit): ")
                if answer.lower() == 'q':
                    print("Exiting practice mode.")
                    break
                if answer.lower() == question.correct_answer.lower():
                    print("Correct!")
                    question.times_correct += 1
                else:
                    print(f"Incorrect! The correct answer was {question.correct_answer}.")

            question.times_shown += 1
            self.question_manager.update_questions(self.question_manager.questions)

            # Debugging: Print the current state of the question
            # print(f"Updated Question: {question.text}, Times Shown: {question.times_shown}, Times Correct: {question.times_correct}")

            # Update last_question to the current one
            last_question = question
