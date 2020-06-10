import math

from random import randint


GAME_RULES = 'Find the greatest common divisor of given numbers.'
_MAX_AVAILABLE_NUMBER_IN_QUESTION = 50


def get_correct_answer(numbers: str):
    a, b = map(int, numbers.split())
    return str(math.gcd(a, b))


def get_question():
    a = randint(0, _MAX_AVAILABLE_NUMBER_IN_QUESTION)
    b = randint(0, _MAX_AVAILABLE_NUMBER_IN_QUESTION)
    return f"{a} {b}"
