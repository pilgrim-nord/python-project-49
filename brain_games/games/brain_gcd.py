import math
from random import randint
from brain_games.game_engine import fire


def rules():
	print('Find the greatest common divisor of given numbers.')


def task_and_right_answer():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    question = f"Question: {random_number1} {random_number2}"
    right_answer = math.gcd(random_number1, random_number2)
    
    return question, right_answer


def run():
	fire(rules, task_and_right_answer)
