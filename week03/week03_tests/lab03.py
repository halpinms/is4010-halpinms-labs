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
    "The silly cat jumped over the lazy dog and laughed."
    
    >>> generate_mad_lib("brave", "knight", "battled") 
    "Once upon a time, a brave knight battled dragons and saved the kingdom."
    """
    # TODO: Replace this with your creative story implementation
    # Must use f-string formatting and include all three parameters
    story = f"The {adjective} {noun} {verb} through the snow down I-75 in their four wheel drive." 
    return story
print(generate_mad_lib("funky", "monkey", "drove"))      

import random

def guessing_game():
    """
    Plays a number guessing game with the user.
    
    This interactive game demonstrates while loops, conditionals, and user input
    handling. The user attempts to guess a randomly generated number between
    1 and 100, receiving feedback after each guess.

    Game Flow:
    1. Generate a random secret number between 1 and 100 (inclusive)
    2. Prompt the user with clear instructions
    3. Use a while loop to continue until the user guesses correctly
    4. For each guess:
       - Convert user input to integer
       - Compare guess to secret number
       - Provide feedback: "Too high!", "Too low!", or success
       - Count attempts
    5. When correct, congratulate user and show number of attempts
    6. Exit the game

    Input Validation:
    - Assume user will enter valid integers (error handling not required)
    
    Example Game Session:
    --------
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    Enter your guess: 50
    Too high! Try again.
    Enter your guess: 25
    Too low! Try again.
    Enter your guess: 37
    Congratulations! You guessed it in 3 attempts!
    """

secret = random.randint(1, 100)
attempts = 0
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")        

while True:  # Continue until user guesses correctly
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break  # Exit the loop when correct

# Run the game (uncomment to play)
guessing_game()

if __name__ == '__main__':
    guessing_game()