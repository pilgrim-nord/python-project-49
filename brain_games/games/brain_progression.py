from random import randint, choice
from brain_games.game_engine import fire

MIN_START_PROGRESSION = 1
MAX_START_PROGRESSION = 15

MIN_STEP_PROGRESSION = 2
MAX_STEP_PROGRESSION = 9

PROGRESSION_LENGTH = 10

GAME_DESCRIPTION = 'What number is missing in the progression?'


def create_task_and_right_answer():
    first_number = randint(MIN_START_PROGRESSION, MAX_START_PROGRESSION)
    step = randint(MIN_STEP_PROGRESSION, MAX_STEP_PROGRESSION)
    task_string = []
    current_number = first_number
    for _ in range(PROGRESSION_LENGTH):
        task_string.append(current_number)
        current_number += step
    
    right_answer = choice(task_string)
    question = ''
    for i in task_string:
        if i != right_answer:
            question += str(i) + ' '
        else:
            question += '.. '
    question = (f"Question: {question}")
    return question, right_answer