from random import randint
from brain_games.games.structure import fire


def rules():
	print('Answer "yes" if the number is even, otherwise answer "no".')


def task_and_right_answer():
    random_number = randint(1, 100)
    question = f"Question:{random_number}"
    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer


def run():
	fire(rules, task_and_right_answer)
