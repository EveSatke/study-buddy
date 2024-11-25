from question_manager import QuestionManager

"""
=== STUDY BUDDY ===
1. Add Questions
2. View Statistics
3. Manage Questions (Enable/Disable)
4. Practice Mode
5. Test Mode
6. Exit
"""

class StudyBuddy:
    def __init__(self):
        self.question_manager = QuestionManager()

    def run(self):
        self.question_manager.add_question()

study_buddy = StudyBuddy()
study_buddy.run()
