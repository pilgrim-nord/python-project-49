from random import randint, choice

MIN_START_PROGRESSION = 1
MAX_START_PROGRESSION = 15

MIN_STEP_PROGRESSION = 2
MAX_STEP_PROGRESSION = 9

PROGRESSION_LENGTH = 10

GAME_DESCRIPTION = 'What number is missing in the progression?'


def create_task_and_right_answer():
    first_number = randint(MIN_START_PROGRESSION, MAX_START_PROGRESSION)
    step = randint(MIN_STEP_PROGRESSION, MAX_STEP_PROGRESSION)
    progression = []
    current_number = first_number

    for _ in range(PROGRESSION_LENGTH):
        progression.append(current_number)
        current_number += step

    answer_position = randint(1, PROGRESSION_LENGTH - 1)
    right_answer = str(progression[answer_position])
    progression[answer_position] = '..'
    question_line = ' '.join(map(str, progression))
    
    question = (f'Question: {question_line}')
    return question, right_answer
