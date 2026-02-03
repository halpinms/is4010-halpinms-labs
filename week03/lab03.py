import random

def generate_mad_lib(adjective, noun, verb):
    story = f"The {adjective} {noun} {verb} through the snow down I-75 in their four wheel drive."
    return story


def guessing_game():
    secret = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break


if __name__ == "__main__":
    print(generate_mad_lib("funky", "monkey", "drove"))
    guessing_game()
