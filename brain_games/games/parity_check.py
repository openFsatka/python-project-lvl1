import prompt

from random import randint

from brain_games.cli import welcome_user
from brain_games.games_config import ROUNDS_COUNT


GAME_RULES = 'Answer "yes" if number even otherwise answer "no".'
INCORRECT_ANSWER = "'{0}' is wrong answer ;(. Correct answer was '{1}'."


def get_correct_answer(number: int):
    return "yes" if (number % 2) == 0 else "no"


def run_parity_check():
    user_name = welcome_user(GAME_RULES)
    game_round = 0
    while game_round < ROUNDS_COUNT:
        number = randint(0, 10**6)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        correct_answer = get_correct_answer(number)
        if answer == correct_answer:
            print("Correct!")
            game_round += 1
        else:
            print(INCORRECT_ANSWER.format(answer, correct_answer))
            print(f"Let's try again, {user_name}!")
    print(f"Congratulations, {user_name}!")
