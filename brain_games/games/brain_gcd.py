import math
from random import randint

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def create_task_and_right_answer():
    random_number1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_number2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = f'Question: {random_number1} {random_number2}'
    right_answer = math.gcd(random_number1, random_number2)

    return question, right_answer
