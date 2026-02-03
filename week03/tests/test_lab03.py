import random
from unittest.mock import patch
from week03.lab03 import generate_mad_lib, guessing_game


def test_generate_mad_lib():
    adj = "silly"
    noun = "cat"
    verb = "jumped"

    story = generate_mad_lib(adj, noun, verb)

    assert isinstance(story, str)
    assert adj in story
    assert noun in story
    assert verb in story


def test_guessing_game():
    with patch('week03.lab03.random.randint', return_value=50):
        with patch('builtins.input', side_effect=['75', '25', '50']):
            with patch('builtins.print') as mock_print:
                guessing_game()
                assert mock_print.called
