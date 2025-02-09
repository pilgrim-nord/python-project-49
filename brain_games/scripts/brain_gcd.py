from brain_games.games.brain_gcd \
    import create_task_and_right_answer, GAME_DESCRIPTION
from brain_games.game_engine import fire


def main():
    fire(GAME_DESCRIPTION, create_task_and_right_answer)

    
if __name__ == "__main__":    
    main()