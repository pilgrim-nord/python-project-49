import prompt

GAMES_COUNT = 3


def fire(game_rules, create_task_and_right_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_rules)

    for _ in range(GAMES_COUNT):
        question, right_answer = create_task_and_right_answer()
        print(question)
        user_answer = prompt.string('Your answer: ')

        if user_answer.lower() != str(right_answer):
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{right_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        else:
            print('Correct!')
        print(f'Congratulations, {name}!')