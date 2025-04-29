from random import randint
from math import sqrt

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100

GAME_DESCRIPTION = 'Answer "yes" if given number is prime.'\
    ' Otherwise answer "no".'


def is_prime(number):

    if number < 2:
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def create_task_and_right_answer():
    random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = f'Question: {random_number}'
    right_answer = 'yes'

    if is_prime(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return question, right_answer
