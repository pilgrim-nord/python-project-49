from random import randint, choice

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 20

GAME_DESCRIPTION = 'What is the result of the expression?'


def create_task_and_right_answer():
    random_number1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_number2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operation = choice(['+', '-', '*'])
    question = (f'Question: {random_number1} {operation} {random_number2}')

    if operation == '+':
        right_answer = random_number1 + random_number2
    elif operation == '-':
        right_answer = random_number1 - random_number2
    elif operation == '*':
        right_answer = random_number1 * random_number2

    return question, right_answer
