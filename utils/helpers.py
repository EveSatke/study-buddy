def get_number_input(prompt, min_value, max_value, allow_exit=False):
    while True:
        user_input = input(prompt).strip()

        if allow_exit and user_input.lower() == "q":
            return None
        
        try:
            number = int(user_input)
            if min_value <= number <= max_value:
                return number
            print(f"Please enter a number between {min_value} to {max_value}")
        except ValueError:
            print("Invalid input. Please enter a number.")
            pass

def get_text_input(prompt, allow_exit=False):
    while True:
        text = input(prompt).strip()

        if allow_exit and text.lower() == "q":
            return None
        
        if text:
            return text
        print("Input cannot be empty. Please try again.")