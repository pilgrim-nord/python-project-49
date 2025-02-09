from random import randint
from math import sqrt
from brain_games.game_engine import fire


def rules():
	print('Answer "yes" if given number is prime. Otherwise answer "no".')

def is_prime(num):
    if number < 2:
        return False
    else:
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                return False
    return True


def task_and_right_answer():
    number = randint(1, 100)
    question = f"Question: {number}"
    right_answer = 'yes'
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer


def run():
	fire(rules, task_and_right_answer)