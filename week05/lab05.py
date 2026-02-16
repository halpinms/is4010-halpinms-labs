"""
# Messy script to be refactored
users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]

# Calculate total age and count users for average
total_age = 0
user_count_for_age = 0
for user in users:
    if isinstance(user.get("age"), int):
        total_age += user["age"]
        user_count_for_age += 1
average_age = total_age / user_count_for_age
print(f"average user age: {average_age:.2f}")

# Get a list of all active user emails
active_user_emails = []
for user in users:
    if user.get("is_active") and user.get("email"):
        active_user_emails.append(user["email"])
print(f"active user emails: {active_user_emails}")

"""

"""
lab05.py

Refactored user-processing script with defensive input handling.
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, List


users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False},
]


def calculate_average_age(users: Iterable[Dict[str, Any]]) -> float:
    """
    Calculate the average age across users with a valid integer `age`.

    Parameters
    ----------
    users : iterable of dict
        User records. Each record may contain an ``age`` key.

    Returns
    -------
    float
        Average age across users with valid integer ages. Returns 0.0 if no
        valid ages exist.

    Notes
    -----
    - Skips non-dict items.
    - Counts only *pure* ints as valid ages (excludes booleans).
    """
    total_age = 0
    count = 0

    for user in users:
        if not isinstance(user, dict):
            continue
        age = user.get("age")
        if type(age) is int:  # avoids counting True/False as 1/0
            total_age += age
            count += 1

    return (total_age / count) if count else 0.0


def get_active_user_emails(users: Iterable[Dict[str, Any]]) -> List[str]:
    """
    Return emails for users who are active and have a valid email string.

    Parameters
    ----------
    users : iterable of dict
        User records. Users may contain ``is_active`` and ``email`` keys.

    Returns
    -------
    list of str
        Email addresses for users where ``is_active is True`` and email is a
        non-empty string.

    Notes
    -----
    - Skips non-dict items.
    - Uses strict boolean check for activity to avoid truthiness issues.
    """
    emails: List[str] = []

    for user in users:
        if not isinstance(user, dict):
            continue

        if user.get("is_active") is True:
            email = user.get("email")
            if isinstance(email, str) and email:
                emails.append(email)

    return emails


if __name__ == "__main__":
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")