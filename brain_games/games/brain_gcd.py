from random import randint
from math import gcd
from brain_games.games.structure import fire


def rules():
	print('Find the greatest common divisor of given numbers.')


def task_and_right_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f"Question: {num1} {num2}"
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    right_answer = num1 + num2
    return question, right_answer


def run():
	fire(rules, task_and_right_answer)
