import prompt

from brain_games.games_config import ROUNDS_COUNT


INCORRECT_ANSWER = "'{0}' is wrong answer ;(. Correct answer was '{1}'."


def welcome_user(game_rules: str = None) -> str:
    print("Welcome to the Brain Games!")

    if game_rules:
        print(game_rules)

    name = prompt.string("\nMay I have your name? ")
    print(f"Hello, {name}!", end="\n\n")

    return name


def run_game(
        game_rules: str,
        game_question: callable,
        game_correct_answer: callable
):
    user_name = welcome_user(game_rules)
    game_round = 0
    while game_round < ROUNDS_COUNT:
        question = game_question()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        correct_answer = game_correct_answer(question)
        if answer == correct_answer:
            print("Correct!")
            game_round += 1
        else:
            print(INCORRECT_ANSWER.format(answer, correct_answer))
            print(f"Let's try again, {user_name}!")
    print(f"Congratulations, {user_name}!")
