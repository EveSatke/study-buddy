from colorama import Fore

def get_number_input(prompt, min_value, max_value, allow_exit=False):
    while True:
        user_input = input(prompt).strip()

        if allow_exit and user_input.lower() == "q":
            return user_input
        
        try:
            number = int(user_input)
            if min_value <= number <= max_value:
                return number
            print(f"{Fore.RED}Please enter a number between {min_value} to {max_value}{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a number.{Fore.RESET}")

def get_text_input(prompt):
    while True:
        text = input(prompt).strip()
        
        if text:
            return text
        print(f"{Fore.RED}Input cannot be empty. Please try again.{Fore.RESET}")

def get_continue_input(prompt):
    while True:
        user_input = input(prompt).lower().strip()

        if user_input == "":
            return None
        elif user_input == "q":
            return user_input
        else:
            print(f"{Fore.RED}Invalid input. Please try again.{Fore.RESET}")

