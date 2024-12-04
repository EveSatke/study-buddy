import random
from datetime import datetime
from question_manager import QuestionManager
from utils.helpers import get_text_input, get_number_input, get_continue_input

class PracticeTestManager:
    RESULTS_PATH = "results.txt"

    def __init__(self, question_manager:QuestionManager):
        self.question_manager = question_manager
        self.active_questions = [q for q in self.question_manager.questions if q.is_active]

    def load_active_questions(self):
        return [q for q in self.question_manager.questions if q.is_active]

    def calculate_weights(self, questions):
        weights = []
        min_weight = 0.1

        for question in questions:
            weight = max(min_weight, (question.times_shown - question.times_correct + 1) / (question.times_shown + 1))
            weights.append(weight)

        return weights
    
    def select_weighted_question(self, last_question=None):
        self.active_questions = self.load_active_questions()
        if not self.active_questions:
            return None 
        
        weights = self.calculate_weights(self.active_questions)
        total_weight = sum(weights)
        if total_weight == 0:
            return None
        probabilities = [w / total_weight for w in weights]
        selected_question = random.choices(self.active_questions, probabilities, k=1)[0]
        if selected_question == last_question and len(self.active_questions) > 1:
            selected_question = random.choices(self.active_questions, probabilities, k=1)[0]
        return selected_question
    
    def ask_question(self, question):
        print(question.text)
        if question.type == "quiz":
            for i, option in enumerate(question.options, 1):
                print(f"{i}. {option}")
            answer = get_number_input(f"\nChoose the correct option (1-{len(question.options)}): ", 1, len(question.options))
            if answer == question.correct_option:
                print("✅Correct!")
                question.times_correct += 1
                score = 1
                return score
            else:
                print(f"❌Incorrect! The correct option was {question.correct_option}.")
                return False
        else:
            answer = get_text_input("Your answer: ")
            if answer.lower() == question.correct_answer.lower():
                print("✅Correct!")
                question.times_correct += 1
                score = 1
                return score
            else:
                print(f"❌Incorrect! The correct answer was {question.correct_answer}.")
                return False

    
    def practice_mode(self):
        print(
            "\n=== PRACTICE MODE ===")
        last_question = None
        while True:
            question = self.select_weighted_question(last_question)
            if not question:
                print("No questions available for practice.")
                break
            print()    
            self.ask_question(question)

            question.times_shown += 1
            self.question_manager.update_questions(self.question_manager.questions)
            last_question = question
            next_question = get_continue_input("\nPress Enter to continue to the next question or 'q' to quit...")
            if next_question == "q":
                print("Exiting...")
                break

    def test_mode(self):
        test_score = 0
        print(
            "\n=== TEST MODE ===\n"
            "You can choose how many questions you'd like to answer.\n"
            "Each question will appear only once."
            )
  
        selected_questions = self.select_random_questions()

        if not selected_questions:
            print("No questions available for test.")
            return False
        
        print("Starting your test...")
        for n, question in enumerate(selected_questions, 1):
            print(f"\nQuestion {n}")
            test_score += self.ask_question(question)
            if n != len(selected_questions):
                next_question = input("\nPress Enter to continue or 'q' to quit...")
                if next_question == "q":
                    print("Exiting...")
                    break
        print(
            "\nCongrats! 🎉 "
            f"\nYou scored {test_score} out of {len(selected_questions)}."
            )
        self.save_score(test_score, len(selected_questions))

        input("\nPress Enter to continue...")
        

    def select_random_questions(self):
        self.active_questions = self.load_active_questions()
        questions_number = get_number_input(
        f"How many questions would you like to answer (from 1 to {len(self.active_questions)})? ", 
            1, 
            len(self.active_questions)
            )  
        return random.sample(self.active_questions, questions_number)
    
    def save_score(self, score, questions_number):
        with open(self.RESULTS_PATH, "a") as file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{current_time} - Score: {score} out of {questions_number}\n")