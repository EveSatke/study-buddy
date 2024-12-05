from colorama import init
from study_buddy import StudyBuddy

def main():
    init(autoreset=True)
    study_buddy = StudyBuddy()
    study_buddy.main_menu()

if __name__ == "__main__":
    main()

"""
War card game GitHub public repository:
https://github.com/EveSatke/war-card-game.git
"""