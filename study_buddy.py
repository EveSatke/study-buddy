from question_manager import QuestionManager
from question_statistics import QuestionStatistics
from practice_test_manager import PracticeTestManager
from colorama import Fore

class StudyBuddy:
    def __init__(self):
        self.question_manager = QuestionManager()
        self.questions_statistics = QuestionStatistics(self.question_manager)
        self.practice_test_manager = PracticeTestManager(self.question_manager)
        self.menu_options = {
            "1": self._handle_add_questions,
            "2": self._handle_statistics,
            "3": self._handle_manage_questions,
            "4": lambda:self._handle_mode("practice"),
            "5": lambda:self._handle_mode("test"),
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
            f"{Fore.YELLOW}\n=== STUDY BUDDY ===\n{Fore.RESET}"
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
    
    def _handle_mode(self, mode):
        if not self.question_manager.has_minimum_questions():
            print(f"\n{Fore.RED}You need at least {self.question_manager.MIN_QUESTIONS} questions before starting Practice/Test mode.{Fore.RESET}")
            print(f"{Fore.RED}Please add {self.question_manager.MIN_QUESTIONS - len(self.question_manager.questions)} more questions.{Fore.RESET}")
            self.question_manager.add_questions()
        else:
            if mode == "practice":
                self.practice_test_manager.practice_mode()
            elif mode == "test":
                self.practice_test_manager.test_mode()
        return True
    
    def _handle_exit(self):
        print(f"{Fore.YELLOW}Exiting...{Fore.RESET}")
        return False
    
    def _check_questions_exist(self):
        if len(self.question_manager.questions) == 0:
            print(f"{Fore.RED}There are no questions. Please add at least 1 question.{Fore.RESET}")
            self.question_manager.add_questions()
            return False
        return True
