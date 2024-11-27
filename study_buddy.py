from question_manager import QuestionManager

class StudyBuddy:
    def __init__(self):
        self.question_manager = QuestionManager()
        

    def main_menu(self):
        while True:
            print(
            "\n=== STUDY BUDDY ===\n"
            "1. Add Questions\n"
            "2. View Statistics\n"
            "3. Manage Questions (Enable/Disable)\n"
            "4. Practice Mode\n"
            "5. Test Mode\n"
            "6. Exit\n")

            choice = input("Choose an option (1-6): ")
            if choice == "1":
                self.add_questions()
            elif choice == "4" or choice == "5":
                if not self.question_manager.has_minimum_questions():
                    print(f"\nYou need at least {self.question_manager.MIN_QUESTIONS} questions before starting Practice/Test mode.")
                    print(f"Please add {self.question_manager.MIN_QUESTIONS - self.question_manager.get_question_count()} more questions.")
                    self.add_questions()
            elif choice == "6":
                print("Exiting...")
                break

    def add_questions(self):
        remaining = max((self.question_manager.MIN_QUESTIONS - self.question_manager.get_question_count()), 1)

        while remaining > 0:
            if self.question_manager.create_question():
                remaining -= 1
            else:
                break

    
