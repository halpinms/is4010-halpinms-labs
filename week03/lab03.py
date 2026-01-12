# lab03.py
# Week 03: Python basics and automated testing
# Author: Sample Solution

import random


def generate_mad_lib(adjective, noun, verb):
    """
    Generates a short story using the provided words.

    This function demonstrates string formatting and function design
    by creating a Mad Libs-style story from user-provided words.

    Parameters
    ----------
    adjective : str
        An adjective to use in the story (e.g., "silly", "brave", "colorful").
    noun : str
        A noun to use in the story (e.g., "cat", "computer", "adventure").
    verb : str
        A past-tense verb to use in the story (e.g., "jumped", "crashed", "danced").

    Returns
    -------
    str
        A formatted story string that incorporates all three input words.

    Examples
    --------
    >>> generate_mad_lib("silly", "cat", "jumped")
    "Once upon a time, a silly cat jumped over the lazy dog and won a medal."

    >>> generate_mad_lib("brave", "knight", "battled")
    "In a land far away, a brave knight battled fierce dragons and became a legend."
    """
    # Create an engaging story using all three parameters
    story = f"Once upon a time, a {adjective} {noun} {verb} over the lazy dog and won a medal."
    return story


def guessing_game():
    """
    Runs an interactive number guessing game.

    The computer picks a random number between 1 and 100, and the player
    tries to guess it. The game provides feedback after each guess.

    This function demonstrates:
    - Using the random module
    - While loops for game logic
    - Input validation
    - Conditional statements

    Parameters
    ----------
    None

    Returns
    -------
    None
        This function prints output directly and doesn't return a value.
    """
    # Generate random number between 1 and 100
    secret_number = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print()

    attempts = 0

    while True:
        # Get user's guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {secret_number}.")
                break

        except ValueError:
            print("Please enter a valid number!")


# If this file is run directly (not imported), run the guessing game
if __name__ == "__main__":
    guessing_game()
