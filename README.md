# Study Buddy

Study Buddy is an interactive application designed to help users create, manage, and practice questions for study purposes. It supports both quiz-type and freeform questions, allowing users to test their knowledge and track their progress over time.

## Features

- **Add Questions**: Create new quiz or freeform questions and store them in a CSV file.
- **Manage Questions**: Enable or disable questions to control which ones are active for practice or tests.
- **Practice Mode**: Practice questions with weighted selection based on past performance.
- **Test Mode**: Take a test with a specified number of questions and receive a score.
- **View Statistics**: See detailed statistics about your questions, including success rates and activity status.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/study-buddy.git
   ```
2. Navigate to the project directory:
   ```bash
   cd study-buddy
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main program:
   ```bash
   python main.py
   ```
2. Follow the on-screen instructions to navigate through the menu options.

## Code Structure

- **main.py**: Entry point of the application.
- **study_buddy.py**: Contains the main menu and handles user interactions.
- **question_manager.py**: Manages question creation, storage, and status.
- **practice_test_manager.py**: Handles practice and test modes.
- **question_models.py**: Defines the data models for questions.
- **question_storage.py**: Manages loading and saving questions to a CSV file.
- **question_statistics.py**: Provides statistics about the questions.
- **utils/helpers.py**: Contains utility functions for user input.

## Testing

Tests are written using `pytest`. To run the tests, execute:

```bash
pytest test_studybuddy.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
