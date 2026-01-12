# test_lab05.py
import pytest
from lab05 import calculate_average_age, get_active_user_emails


@pytest.fixture
def sample_users():
    return [
        {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
        {"name": "bob", "age": 25, "is_active": False},
        {
            "name": "charlie",
            "age": 35,
            "is_active": True,
            "email": "charlie@example.com",
        },
        {"name": "david", "age": "unknown", "is_active": False},
        {"name": "eve", "is_active": True, "email": "eve@example.com"},
    ]


# Tests for calculate_average_age
def test_calculate_average_age_normal(sample_users):
    # (30 + 25 + 35) / 3 = 30.0
    assert calculate_average_age(sample_users) == 30.0


def test_calculate_average_age_empty_list():
    # Should handle the error and return a default value
    assert calculate_average_age([]) == 0.0


# Tests for get_active_user_emails
def test_get_active_user_emails_normal(sample_users):
    expected_emails = ["alice@example.com", "charlie@example.com", "eve@example.com"]
    assert set(get_active_user_emails(sample_users)) == set(expected_emails)


def test_get_active_user_emails_no_active_users():
    users = [{"name": "bob", "age": 25, "is_active": False}]
    assert get_active_user_emails(users) == []


def test_get_active_user_emails_empty_list():
    assert get_active_user_emails([]) == []
