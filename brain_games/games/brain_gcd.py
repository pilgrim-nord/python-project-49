from random import randint
from brain_games.games.structure import fire


def rules():
	print('Find the greatest common divisor of given numbers.')


def task_and_right_answer():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f"Question: {number1} {number2}"
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    right_answer = number1 + number2
    return question, right_answer


def run():
	fire(rules, task_and_right_answer)
