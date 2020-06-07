import prompt


def welcome_user():
    print("Welcome to the Brain Games!", end="\n\n")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
