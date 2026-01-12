# test_lab03.py
import random
from unittest.mock import patch
from lab03 import generate_mad_lib, guessing_game

def test_generate_mad_lib():
    """
    Tests the generate_mad_lib function to ensure it uses the inputs correctly.

    This test verifies that:
    1. The function accepts three parameters
    2. All provided words appear in the returned story
    3. The function returns a string (not None or other type)
    """
    # Test case 1: Basic functionality
    adj = "silly"
    noun = "cat"
    verb = "jumped"

    story = generate_mad_lib(adj, noun, verb)

    # Check that it returns a string
    assert isinstance(story, str), "Function must return a string"

    # Check that all three words appear in the story (case-insensitive)
    story_lower = story.lower()
    assert adj.lower() in story_lower, f"Adjective '{adj}' not found in story"
    assert noun.lower() in story_lower, f"Noun '{noun}' not found in story"
    assert verb.lower() in story_lower, f"Verb '{verb}' not found in story"

    # Check that the story isn't empty
    assert len(story) > 0, "Story cannot be empty"

    # Test case 2: Different words
    story2 = generate_mad_lib("brave", "knight", "battled")
    assert isinstance(story2, str)
    assert "brave" in story2.lower()
    assert "knight" in story2.lower()
    assert "battled" in story2.lower()

def test_guessing_game_correct_guess():
    """
    Tests the guessing_game function with a correct guess.

    Uses mocking to control:
    - The random number generated
    - The user's input

    Verifies the function handles a correct guess properly.
    """
    # Mock random.randint in the lab03 module to return a predictable number (50)
    with patch('lab03.random.randint', return_value=50):
        # Mock input to simulate user guessing correctly
        with patch('builtins.input', return_value='50'):
            # Mock print to capture output
            with patch('builtins.print') as mock_print:
                guessing_game()

                # Verify the function printed something
                assert mock_print.called, "Function should print output"

                # Get all print calls
                print_calls = [str(call) for call in mock_print.call_args_list]

                # Check that success message was printed (in some form)
                output_text = ' '.join(print_calls).lower()
                assert 'correct' in output_text or 'right' in output_text or 'won' in output_text or 'yes' in output_text, \
                    "Function should indicate correct guess"

def test_guessing_game_multiple_guesses():
    """
    Tests the guessing_game function with multiple incorrect guesses before correct.

    Simulates:
    - Random number: 42
    - User guesses: 30 (too low), 50 (too high), 42 (correct)
    """
    with patch('lab03.random.randint', return_value=42):
        # Simulate three guesses: 30, 50, 42
        with patch('builtins.input', side_effect=['30', '50', '42']):
            with patch('builtins.print') as mock_print:
                guessing_game()

                # Verify the function printed something
                assert mock_print.called, "Function should print output"

                # Should have called print multiple times (for low, high, and correct)
                assert mock_print.call_count >= 3, \
                    "Function should print feedback for each guess"
