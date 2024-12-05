import csv
from question_manager import QuestionManager
from colorama import Fore

class QuestionStatistics:
    FILE_PATH = "data/questions.csv"
    def __init__(self, question_manager):
        self.question_manager = question_manager

    def print_statistics(self):
        questions = self.question_manager.questions
        total_questions = len(questions)

        if total_questions == 0:
            print(f"{Fore.RED}No questions available. Please add questions first.{Fore.RESET}")
            return

        self.active_count = sum(1 for q in questions if q.is_active)
        self.success_rate_sum = sum(q.times_correct for q in questions)
        self.times_shown_sum = sum(q.times_shown for q in questions)

        print("\n=== QUESTIONS LIST ===\n")
        for question in questions:
            status = f"{Fore.GREEN}Active ✓{Fore.RESET}" if question.is_active else f"{Fore.RED}Inactive ✗{Fore.RESET}"
            success_rate = f"{Fore.RED}N/A{Fore.RESET}" if question.times_shown == 0 else f"{Fore.CYAN}{round((question.times_correct / question.times_shown) * 100)}%{Fore.RESET}"
            
            print(
                f"ID: {question.id}\n"
                f"Status: {status}\n"
                f"Question: {question.text}\n"
                f"Times shown: {question.times_shown}\n"
                f"Success rate: {success_rate}\n"
                "-------------------\n"
            )
        self.print_total_statistics(total_questions)

        input("Press Enter to continue...")

    def print_total_statistics(self, total_questions):
        if self.times_shown_sum == 0:
            average_success_rate = "N/A"  
        else:
            average_success_rate = (self.success_rate_sum / self.times_shown_sum) * 100
        print(
            f"Total questions: {total_questions}",
            f"\nActive questions: {self.active_count}",
            f"\nAverage success rate: {average_success_rate if isinstance(average_success_rate, str) else round(average_success_rate)}%\n"
        )