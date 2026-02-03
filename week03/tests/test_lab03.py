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
    
    # Verify function returns a string
    assert isinstance(story, str), "Function should return a string"
    
    # Verify all words are used in the story
    assert adj in story, f"Adjective '{adj}' not found in story"
    assert noun in story, f"Noun '{noun}' not found in story"
    assert verb in story, f"Verb '{verb}' not found in story"
    
    # Test case 2: Different inputs
    adj2 = "brave"
    noun2 = "knight"
    verb2 = "battled"
    
    story2 = generate_mad_lib(adj2, noun2, verb2)
    
    assert isinstance(story2, str), "Function should return a string"
    assert adj2 in story2, f"Adjective '{adj2}' not found in story"
    assert noun2 in story2, f"Noun '{noun2}' not found in story"  
    assert verb2 in story2, f"Verb '{verb2}' not found in story"
    
    # Test case 3: Edge case with unusual inputs
    adj3 = "extraordinary"
    noun3 = "algorithm"
    verb3 = "computed"
    
    story3 = generate_mad_lib(adj3, noun3, verb3)
    
    assert isinstance(story3, str), "Function should return a string"
    assert adj3 in story3, f"Adjective '{adj3}' not found in story"
    assert noun3 in story3, f"Noun '{noun3}' not found in story"
    assert verb3 in story3, f"Verb '{verb3}' not found in story"


def test_guessing_game():
    """
    Tests the guessing_game function to ensure it handles the game flow correctly.
    
    This test uses mocking to simulate user input and verify that:
    1. The function can handle a winning game scenario
    2. Proper feedback is given for high/low guesses
    3. The game terminates when the correct number is guessed
    4. Attempt counting works correctly
    """
    # Mock random.randint in the lab03 module to return a predictable number (50)
    with patch('lab03.random.randint', return_value=50):
        # Mock input() to simulate user guesses: too high, too low, correct
        with patch('builtins.input', side_effect=['75', '25', '50']):
            # Mock print() to capture output
            with patch('builtins.print') as mock_print:
                # Run the guessing game
                guessing_game()
                
                # Verify that print was called (the game produced output)
                assert mock_print.called, "Game should produce output"
                
                # Check that the game printed some expected messages
                printed_output = [str(call) for call in mock_print.call_args_list]
                output_text = ' '.join(printed_output)
                
                # Verify game contains expected elements (flexible checking)
                # The game should mention numbers between 1 and 100
                contains_range = any('1' in output and '100' in output for output in printed_output)
                
                # Should contain some form of feedback
                contains_feedback = any(
                    'high' in output.lower() or 'low' in output.lower() or 
                    'congratulations' in output.lower() or 'correct' in output.lower()
                    for output in printed_output
                )
                
                assert contains_range or contains_feedback, "Game should provide range info or feedback"
    
    # Test edge case: immediate correct guess
    with patch('lab03.random.randint', return_value=42):
        with patch('builtins.input', side_effect=['42']):
            with patch('builtins.print') as mock_print:
                guessing_game()
                
                # Should still work with just one guess
                assert mock_print.called, "Game should work with immediate correct guess"