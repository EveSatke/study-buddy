import csv
from question_manager import QuestionManager

class Statistics:
    FILE_PATH = "data/questions.csv"
    def __init__(self):
        self.question_manager = QuestionManager()

    def print_statistics(self):
        active_count = 0
        success_rate_sum = 0
        print("\n=== QUESTIONS LIST ===\n")
        try:
            with open(self.FILE_PATH, "r") as file:
                reader = csv.DictReader(file)
                for line in reader:
                    if line["is_active"] == 'True':
                        status = "Active ✓"
                        active_count +=1
                    else:
                        status = "Inactive ✗"
                    
                    if line["times_correct"] == "0":
                        success_rate = "N/A"  
                    else:
                        success_rate = f"{line["times_correct"]}%"
                        success_rate_sum += int(line["times_correct"])

                    print(
                    f"ID: {line["id"]}\n"
                    f"Status: {status}\n"
                    f"Question: {line["text"]}\n"
                    f"Times shown: {line["times_shown"]}\n"
                    f"Success rate: {success_rate}\n"
                    "-------------------\n")
                print(
                f"Total Questions: {self.question_manager.get_question_count()}\n"
                f"Active Questions: {active_count}\n"
                f"Average Success Rate: {success_rate_sum/self.question_manager.get_question_count()}%\n")
                input("Press Enter to return to main menu...")
                
        except Exception as e:
            print(f"Error: {e}")