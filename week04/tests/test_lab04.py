# test_lab04.py
import pytest
from lab04 import find_common_elements, find_user_by_name, get_list_of_even_numbers


# Tests for find_common_elements
def test_find_common_elements_with_common_items():
    l1 = [1, 2, 3, 4, 5]
    l2 = [4, 5, 6, 7, 8]
    # The order does not matter, so we compare sets
    assert set(find_common_elements(l1, l2)) == {4, 5}


def test_find_common_elements_with_no_common_items():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    assert find_common_elements(l1, l2) == []


def test_find_common_elements_with_empty_lists():
    assert find_common_elements([], []) == []
    assert find_common_elements([1, 2, 3], []) == []


# Tests for find_user_by_name
@pytest.fixture
def sample_users():
    return [
        {"name": "alice", "age": 30, "email": "alice@example.com"},
        {"name": "bob", "age": 25, "email": "bob@example.com"},
    ]


def test_find_user_by_name_existing(sample_users):
    assert find_user_by_name(sample_users, "alice") == {
        "name": "alice",
        "age": 30,
        "email": "alice@example.com",
    }


def test_find_user_by_name_not_existing(sample_users):
    assert find_user_by_name(sample_users, "charlie") is None


def test_find_user_by_name_empty_list():
    assert find_user_by_name([], "alice") is None


# Tests for get_list_of_even_numbers
def test_get_list_of_even_numbers_mixed():
    assert get_list_of_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_get_list_of_even_numbers_all_odd():
    assert get_list_of_even_numbers([1, 3, 5, 7]) == []


def test_get_list_of_even_numbers_all_even():
    assert get_list_of_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]


def test_get_list_of_even_numbers_empty():
    assert get_list_of_even_numbers([]) == []
