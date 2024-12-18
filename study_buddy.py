from question_manager import QuestionManager
from question_statistics import QuestionStatistics
from practice_test_manager import PracticeTestManager
from question_storage import QuestionStorage
from colorama import Fore
from enum import Enum
from utils.helpers import get_number_input

class MenuOption(Enum):
    ADD_QUESTIONS = "Add Questions"
    VIEW_STATISTICS = "View Statistics"
    MANAGE_QUESTIONS = "Manage Questions (Enable/Disable)"
    PRACTICE_MODE = "Practice Mode"
    TEST_MODE = "Test Mode"
    EXIT = "Exit"

class StudyBuddy:
    def __init__(self):
        question_storage = QuestionStorage(
            file_path=QuestionManager.FILE_PATH,
            fieldnames=QuestionManager.FIELDNAMES
        )
        
        self.question_manager = QuestionManager(question_storage)
        self.questions_statistics = QuestionStatistics(self.question_manager)
        self.practice_test_manager = PracticeTestManager(self.question_manager)
        self.menu_options = {
            MenuOption.ADD_QUESTIONS: self._handle_add_questions,
            MenuOption.VIEW_STATISTICS: self._handle_statistics,
            MenuOption.MANAGE_QUESTIONS: self._handle_manage_questions,
            MenuOption.PRACTICE_MODE: lambda: self._handle_mode("practice"),
            MenuOption.TEST_MODE: lambda: self._handle_mode("test"),
            MenuOption.EXIT: self._handle_exit
        }
        

    def main_menu(self):
        while True:
            self._display_menu()
            choice = get_number_input("Choose an option (1-6): ", 1, len(MenuOption))
            try:
                selected_option = list(MenuOption)[choice - 1]
                if self.menu_options[selected_option]() is False:
                    break
            except (IndexError, ValueError):
                print("Invalid option. Please enter option 1-6.")


    def _display_menu(self):
        print(f"{Fore.YELLOW}\n=== STUDY BUDDY ==={Fore.RESET}")
        for index, option in enumerate(MenuOption, start=1):
            print(f"{index}. {option.value}")
        print()
        
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
