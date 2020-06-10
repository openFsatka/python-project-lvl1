from brain_games.cli import run_game
from brain_games.games.gcd import (
    get_correct_answer,
    get_question,
    GAME_RULES
)


def main():
    run_game(GAME_RULES, get_question, get_correct_answer)


if __name__ == "__main__":
    main()
