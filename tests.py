import pytest
from model import Question

@pytest.fixture
def multiple_choices_question(): 
    question = Question(title = 'q1')
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)
    question.add_choice('d', False)
    return question

# test of a private method only because of its primary importance to the subject
def test_just_one_correct_choice_in_multiple_choices_question(multiple_choices_question): 
    correct_choices = multiple_choices_question._find_correct_choice_ids()
    assert len(correct_choices) == 1

def test_max_selections_in_multiple_choices_question(multiple_choices_question): 
    assert multiple_choices_question.max_selections == 1

def test_correct_multiple_choices_question(multiple_choices_question): 
    correct_selected_choice = multiple_choices_question.correct_selected_choices([2])
    assert correct_selected_choice == [2]
    correct_selected_choice = multiple_choices_question.correct_selected_choices([1])
    assert correct_selected_choice == []    

def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_multiple_selections(): 
    question = Question(title = 'q1', max_selections = 2)
    assert question.max_selections == 2

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_title(): 
    question = Question(title = 'q1')
    assert question.title == 'q1'
    question = Question(title = 'testing_title')
    assert question.title == 'testing_title'

def test_create_question_with_invalid_points():
    with pytest.raises(Exception):  
        Question(title = 'q1', points = 0)
    with pytest.raises(Exception):  
        Question(title = 'q1', points = 1000)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_remove_choice(): 
    question = Question(title='q1')
    question.add_choice('a', False)
    assert len(question.choices) == 1

    question.remove_choice_by_id(1)
    assert len(question.choices) == 0

def test_remove_all_choices(): 
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.add_choice('d', True)
    assert len(question.choices) == 4

    question.remove_all_choices()
    assert len(question.choices) == 0

def test_remove_invalid_choice(): 
    question = Question(title = 'q1')
    with pytest.raises(Exception): 
        question.remove_choice_by_id(1)
    
def test_set_correct_choices(): 
    question = Question(title = 'q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.add_choice('d', True)

    question.set_correct_choices([1,2,3,4])

    for choice in question.choices: 
        assert choice.is_correct

def test_set_correct_choices_with_zero_choices(): 
    question = Question(title = 'q1')

    with pytest.raises(Exception):
        question.set_correct_choices([1,2,3,4])
    
def test_correct_selected_choices(): 
    question = Question(title = 'q1')
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)
    question.add_choice('d', True)

    correct_selected_choices = question.correct_selected_choices([1])
    assert correct_selected_choices == []
    correct_selected_choices = question.correct_selected_choices([4])
    assert correct_selected_choices == [4]

def test_correct_more_than_one_selected_choice(): 
    question = Question(title = 'q1')
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)
    question.add_choice('d', True) 

    with pytest.raises(Exception): 
        question.correct_selected_choices([2, 4])

