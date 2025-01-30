from random import randint
from brain_games.games.structure import fire


def rules():
	print('Answer "yes" if the number is even, otherwise answer "no".')


def task_and_right_answer():
    number = randint(1, 100)
    question = f"Question:{number}"
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer


def run():
	fire(rules, task_and_right_answer)
