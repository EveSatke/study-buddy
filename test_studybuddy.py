import pytest
from unittest.mock import patch, MagicMock
from question_manager import QuestionManager
from question_models import Quiz, Freeform
from utils.helpers import get_number_input
from practice_test_manager import PracticeTestManager

@pytest.fixture
def question_manager():
    return QuestionManager()

def test_generate_id(question_manager):
    with patch('builtins.open', new_callable=MagicMock) as mock_open:
        mock_open.return_value.__enter__.return_value = iter(["header\n", "1\n", "2\n"])
        assert question_manager._generate_id() == 3

@patch('question_manager.get_text_input', side_effect=["Sample Question", "Option 1", "Option 2"])
@patch('question_manager.get_number_input', side_effect=[2, 1])
def test_form_quiz_question(mock_get_number_input, mock_get_text_input, question_manager):
    quiz_question = question_manager.form_quiz_question()
    assert isinstance(quiz_question, Quiz)
    assert quiz_question.text == "Sample Question"
    assert quiz_question.options == ["Option 1", "Option 2"]
    assert quiz_question.correct_option == 1

@patch('question_manager.get_text_input', side_effect=["Sample Question", "Correct Answer"])
def test_form_freeform_question(mock_get_text_input, question_manager):
    freeform_question = question_manager.form_freeform_question()
    assert isinstance(freeform_question, Freeform)
    assert freeform_question.text == "Sample Question"
    assert freeform_question.correct_answer == "Correct Answer"

def test_get_number_input_invalid():
    with patch('builtins.input', side_effect=["invalid", "5"]):
        result = get_number_input("Enter a number: ", 1, 10)
        assert result == 5

def test_get_number_input_out_of_range():
    with patch('builtins.input', side_effect=["15", "5"]):
        result = get_number_input("Enter a number: ", 1, 10)
        assert result == 5

@pytest.fixture
def mock_question_manager():
    qm = MagicMock(spec=QuestionManager)
    qm.questions = [
        Quiz(id=1, type="quiz", text="Sample Quiz Question", is_active=True, times_shown=0, times_correct=0, options=["Option 1", "Option 2"], correct_option=1),
        Freeform(id=2, type="freeform", text="Sample Freeform Question", is_active=True, times_shown=0, times_correct=0, correct_answer="Answer")
    ]
    return qm

@pytest.fixture
def practice_test_manager(mock_question_manager):
    return PracticeTestManager(mock_question_manager)

def test_load_active_questions(practice_test_manager):
    active_questions = practice_test_manager.load_active_questions()
    assert len(active_questions) == 2  # Assuming both questions are active

def test_calculate_weights(practice_test_manager):
    questions = practice_test_manager.load_active_questions()
    weights = practice_test_manager.calculate_weights(questions)
    assert len(weights) == len(questions)
    assert all(weight > 0 for weight in weights)

@patch('practice_test_manager.get_number_input', side_effect=[1])
def test_ask_quiz_question_correct(mock_get_number_input, practice_test_manager):
    question = practice_test_manager.question_manager.questions[0] 
    score = practice_test_manager.ask_question(question)
    assert score == 1  

@patch('practice_test_manager.get_text_input', side_effect=["Answer"])
def test_ask_freeform_question_correct(mock_get_text_input, practice_test_manager):
    question = practice_test_manager.question_manager.questions[1]  
    score = practice_test_manager.ask_question(question)
    assert score == 1 
    