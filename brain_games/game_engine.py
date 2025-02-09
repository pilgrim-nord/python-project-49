import prompt


def fire(rules, task_and_right_answer):
	game_attempts = 3 
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name}!')
	rules()
	is_correct = True
	for i in range(game_attempts):
		question, right_answer = task_and_right_answer()
		print(question)
		user_answer = prompt.string('Your answer: ')
		if user_answer.lower() != str(right_answer):
			is_correct = False
			break
		else:
			print('Correct!')
	if is_correct:
		print(f'Congratulations, {name}!')
	else:
		print(
			f"'{user_answer}' is wrong answer ;(. "
			f"Correct answer was '{right_answer}'."
		)
		print(f"Let's try again, {name}!")