from question_manager import QuestionManager
from question_statistics import QuestionStatistics

class StudyBuddy:
    def __init__(self):
        self.question_manager = QuestionManager()
        self.questions_statistics = QuestionStatistics(self.question_manager)
        self.menu_options = {
            "1": self._handle_add_questions,
            "2": self._handle_statistics,
            "3": self._handle_manage_questions,
            "4": self._handle_practice_mode,
            "5": self._handle_practice_mode,
            "6": self._handle_exit
        }
        

    def main_menu(self):
        while True:
            self._display_menu()
            choice = input("Choose an option (1-6): ")

            if choice in self.menu_options:
                if self.menu_options[choice]() is False:
                    break
            else:
                print("Invalid option. Please enter option 1-6.")


    def _display_menu(self):
        print(
            "\n=== STUDY BUDDY ===\n"
            "1. Add Questions\n"
            "2. View Statistics\n"
            "3. Manage Questions (Enable/Disable)\n"
            "4. Practice Mode\n"
            "5. Test Mode\n"
            "6. Exit\n"
            )
        
    def _handle_add_questions(self):
        self.question_manager.add_questions()
        return True

    def _handle_statistics(self):
        if self._check_questions_exist():
            self.questions_statistics.print_statistics()
        return True
    
    def _handle_manage_questions(self):
        if self._check_questions_exist():
            self.question_manager.manage_question_status()
        return True
    
    def _handle_practice_mode(self):
        if not self.question_manager.has_minimum_questions():
            print(f"\nYou need at least {self.question_manager.MIN_QUESTIONS} questions before starting Practice/Test mode.")
            print(f"Please add {self.question_manager.MIN_QUESTIONS - self.question_manager.get_question_count()} more questions.")
            self.question_manager.add_questions()
        return True
    
    def _handle_exit(self):
        print("Exiting...")
        return False
    
    def _check_questions_exist(self):
        if self.question_manager.get_question_count() == 0:
            print("There are no questions. Please add at least 1 question.")
            self.question_manager.add_questions()
            return False
        return True
