from random import randint


GAME_RULES = 'Answer "yes" if number even otherwise answer "no".'
_MAX_AVAILABLE_NUMBER_IN_QUESTION = 10 ** 6


def get_correct_answer(number: int):
    return "yes" if (number % 2) == 0 else "no"


def get_question():
    return randint(0, _MAX_AVAILABLE_NUMBER_IN_QUESTION)
