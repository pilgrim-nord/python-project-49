from random import randint

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def create_task_and_right_answer():
    random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = f'Question: {random_number}'

    if is_even(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return question, right_answer
