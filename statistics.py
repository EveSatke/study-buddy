import csv

class Statistics:
    FILE_PATH = "data/questions.csv"
    def __init__(self):
        try:
            self.print_statistics()
        except Exception as e:
            print(f"Error: {e}")
            

    def print_statistics(self):
        print("\n=== QUESTIONS LIST ===")
        with open(self.FILE_PATH, "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                status = "Active ✓" if line["is_active"] == 'True' else "Inactive ✗"
                success_rate = "N/A" if line["times_correct"] == "0" else f"{line["times_correct"]}%"
                print(
                f"ID: {line["id"]}\n"
                f"Status: {status}\n"
                f"Question: {line["text"]}\n"
                f"Times shown: {line["times_shown"]}\n"
                f"Success rate: {success_rate}\n"
                "-------------------\n")