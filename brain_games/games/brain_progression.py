from random import randint, choice
from brain_games.games.structure import fire


def rules():
	print('What number is missing in the progression?')


def task_and_right_answer():
	first_symbol = randint(1,15)
	step = randint(2,9)
	list_ = []
	current_symbol = first_symbol
	for i in range(10):
	    list_.append(current_symbol)
	    current_symbol += step
	right_answer = choice(list_)
	question = ''
	for i in list_:
	    if i != right_answer:
	        question += str(i) + ' '
	    else:
	        question += '.. '
	return question, right_answer


def run():
	fire(rules, task_and_right_answer)
