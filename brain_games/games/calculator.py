from random import choice, randint

GAME_RULES = 'What is the result of the expression?'

_MAX_AVAILABLE_NUMBER_IN_QUESTION = 10
_OPERATIONS = ['+', '-', '*']

_apply_operation = {
    '+': lambda a, b: a+b,
    '-': lambda a, b: a-b,
    '*': lambda a, b: a*b
}


def get_correct_answer(expression: str):
    operation = _get_operation(expression)
    a, b = map(int, expression.split(operation))
    return str(_apply_operation[operation](a, b))


def get_question():
    a = randint(0, _MAX_AVAILABLE_NUMBER_IN_QUESTION)
    b = randint(0, _MAX_AVAILABLE_NUMBER_IN_QUESTION)
    operation = choice(_OPERATIONS)
    return f"{a} {operation} {b}"


def _get_operation(expression: str):
    for operation in _OPERATIONS:
        if operation in expression:
            return operation
