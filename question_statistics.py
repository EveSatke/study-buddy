import csv
from question_manager import QuestionManager

class QuestionStatistics:
    FILE_PATH = "data/questions.csv"
    def __init__(self, question_manager):
        self.question_manager = question_manager

    def print_statistics(self):
        questions = self.question_manager.questions
        total_questions = len(questions)
      
        self.active_count = sum(1 for q in questions if q.is_active)
        self.success_rate_sum = sum(int(q.times_correct) for q in questions)
        self.times_shown_sum = sum(int(q.times_shown) for q in questions)

        print("\n=== QUESTIONS LIST ===\n")
        for question in questions:
            status = "Active ✓" if question.is_active else "Inactive ✗"
            success_rate = "N/A" if question.times_correct == 0 else f"{round((question.times_correct/question.times_shown) * 100)}%"
            
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
        print(
            f"Total questions: {total_questions}",
            f"\nActive questions: {self.active_count}",
            f"\nAverage success rate: {round((self.success_rate_sum/self.times_shown_sum) * 100)}%\n"
            )