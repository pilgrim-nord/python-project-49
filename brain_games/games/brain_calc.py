from random import randint, choice
from brain_games.game_engine import fire


def rules():
    print('What is the result of the expression?')


def task_and_right_answer():
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    operation = choice(['+', '-', '*'])
    question = (f"Question: {number1} {operation} {number2}")
    if operation == '+':
        right_answer = number1 + number2
    elif operation == '-':
        right_answer = number1 - number2
    elif operation == '*':
        right_answer = number1 * number2
    return question, right_answer


def run():
    fire(rules, task_and_right_answer)