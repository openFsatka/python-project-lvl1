from random import randint


GAME_RULES = 'What number is missing in the progression?'
_MAX_AVAILABLE_NUMBER_IN_QUESTION = 100
_PROGRESSION_LENGTH = 10


def get_correct_answer(sequence: str):
    sequence = sequence.split()
    index = sequence.index("...")
    if index > 1:
        first_element = int(sequence[0])
        difference = int(sequence[1]) - first_element
        return str(first_element + difference*index)
    else:
        element = int(sequence[index+1])
        difference = int(sequence[index+2]) - element
        return str(element - difference)


def get_question():
    first_element = randint(0, _MAX_AVAILABLE_NUMBER_IN_QUESTION)
    difference = randint(0, _MAX_AVAILABLE_NUMBER_IN_QUESTION)
    progression = [
        str(first_element + difference*i) for i in range(_PROGRESSION_LENGTH)
    ]
    index_delete = randint(0, _PROGRESSION_LENGTH-1)
    if index_delete == _PROGRESSION_LENGTH-1:
        return " ".join(progression[:-1]) + " ..."
    elif index_delete == 0:
        return "... " + " ".join(progression[1:])
    head = " ".join(progression[: index_delete])
    tail = " ".join(progression[index_delete+1:])
    return head + " ... " + tail
