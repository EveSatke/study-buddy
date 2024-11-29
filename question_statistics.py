import csv
from question_manager import QuestionManager

class QuestionStatistics:
    FILE_PATH = "data/questions.csv"
    def __init__(self):
        self.question_manager = QuestionManager()

    def print_statistics(self):
        questions = self.question_manager.questions
        self.active_count = sum(1 for q in questions if q.is_active)
        self.success_rate_sum = sum(int(q.times_correct) for q in questions)

        print("\n=== QUESTIONS LIST ===\n")
        for question in questions:
            status = "Active ✓" if question.is_active else "Inactive ✗"
            success_rate = "N/A" if question.times_correct == 0 else f"{question.times_correct}%"
            
            print(
                f"ID: {question.id}\n"
                f"Status: {status}\n"
                f"Question: {question.text}\n"
                f"Times shown: {question.times_shown}\n"
                f"Success rate: {success_rate}\n"
                "-------------------\n"
            )
        stat = self.get_total_statistics()
        print(
            f"Total questions: {stat['total']}\n"
            f"Active questions: {stat['active']}\n"
            f"Average success rate: {stat['avg_success']}%\n"
            )

        input("Press Enter to continue...")

    def get_total_statistics(self):
        return {
            "total": self.question_manager.get_question_count(),
            "active": self.active_count,
            "avg_success": round(self.success_rate_sum/self.question_manager.get_question_count())
        }