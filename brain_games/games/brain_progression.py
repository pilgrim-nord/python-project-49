from random import randint, choice
from brain_games.games.structure import fire


def rules():
    print('What number is missing in the progression?')


def task_and_right_answer():
    first_number = randint(1, 15)
    step = randint(2, 9)
    task_string = []
    current_number = first_number
    for i in range(10):
        task_string.append(current_number)
        current_number += step
    right_answer = choice(task_string)
    question = ''
    for i in task_string:
        if i != right_answer:
            question += str(i) + ' '
        else:
            question += '.. '
    return question, right_answer


def run():
    fire(rules, task_and_right_answer)
