from question_manager import QuestionManager

class StudyBuddy:
    def __init__(self):
        ...

    def main_menu(self):
        while True:
            print("=== STUDY BUDDY ===")
            print("1. Add Questions")
            print("2. View Statistics")
            print("3. Manage Questions (Enable/Disable)")
            print("4. Practice Mode")
            print("5. Test Mode")
            print("6. Exit")
            print()
            choice = input("Choose an option (1-6): ")
            print()

            if choice == "1":
                question_manager = QuestionManager()
                MIN_QUESTIONS = 5
                for n in range(MIN_QUESTIONS):
                    question_manager.add_question()
            elif choice == "6":
                print("Exiting...")
                break

