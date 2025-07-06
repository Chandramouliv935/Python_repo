from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess,answer,turns):
    if guess<answer:
        print("Too low")
        return turns - 1
    elif guess>answer:
        print("Too high")
        return turns - 1
    else:
        print("yayy..that's correct")


def difficulty_settings():
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL

    else:
        return HARD_LEVEL


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = difficulty_settings()
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining")
        guess = int(input("make a guess"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("you ran out of attempts")
            return 
        else:
            print("Guess again")


game()


