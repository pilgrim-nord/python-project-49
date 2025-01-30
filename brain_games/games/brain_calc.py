from random import randint, choice
from brain_games.games.structure import fire


def rules():
    print('What is the result of the expression?')


def task_and_right_answer():
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    sign = choice(['+', '-', '*'])
    question = (f"Question:{number1}{sign}{number2}")
    if sign == '+':
        right_answer = number1 + number2
    elif sign == '-':
        right_answer = number1 - number2
    elif sign == '*':
        right_answer = number1 * number2
    return question, right_answer


def run():
    fire(rules, task_and_right_answer)