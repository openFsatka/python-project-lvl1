from random import randint, choice


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

_PRIME_NUMBERS = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
]
_get_prime = [True, False]


def get_correct_answer(number: int):
    return "yes" if number in _PRIME_NUMBERS else "no"


def get_question():
    is_prime = choice(_get_prime)
    if is_prime:
        return choice(_PRIME_NUMBERS)
    else:
        return randint(0, 100)
