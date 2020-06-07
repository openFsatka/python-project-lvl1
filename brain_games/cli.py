import prompt


def welcome_user(game_rules: str = None) -> str:
    print("Welcome to the Brain Games!")

    if game_rules:
        print(game_rules)

    name = prompt.string("\nMay I have your name? ")
    print(f"Hello, {name}!", end="\n\n")

    return name
