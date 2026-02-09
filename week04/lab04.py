"""
Lab 04 - Efficient data-structure-centric solutions

Fix for your failing tests:
- The autograder calls: find_user_by_name(sample_users, "alice")
  where sample_users is a LIST of dicts, not a prebuilt index.
- So find_user_by_name MUST accept the list and handle lookup efficiently.

We keep the fast path by building a dict index (name -> user) on demand.
Optionally, we cache the index keyed by id(users) to make repeated calls O(1)
*as long as the list object isn't mutated in place*.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Any, Dict, Hashable, List, Optional, TypeVar, cast

T = TypeVar("T", bound=Hashable)

User = Dict[str, Any]
UserIndex = Dict[str, User]


# -----------------------------
# Problem 1: Finding common items
# -----------------------------
def find_common_elements(list1: Iterable[T], list2: Iterable[T]) -> List[T]:
    """
    Return elements present in BOTH inputs.

    Data structure choice:
    - set for O(1) average membership checks

    Notes:
    - Order of result does not matter (per prompt/tests).
    - This version preserves duplicates from the "scanned" side.
      If you want unique common elements only, see find_common_elements_unique().
    """
    if isinstance(list1, Sequence) and isinstance(list2, Sequence):
        small, large = (list1, list2) if len(list1) <= len(list2) else (list2, list1)
        s = set(small)
        return [x for x in large if x in s]

    s = set(list1)
    return [x for x in list2 if x in s]


def find_common_elements_unique(list1: Iterable[T], list2: Iterable[T]) -> List[T]:
    """Unique common elements (set semantics). Order not guaranteed."""
    return list(set(list1).intersection(list2))


# -----------------------------
# Problem 2: User profile lookup
# -----------------------------
def _build_user_index(users: List[User]) -> UserIndex:
    """
    Build {name: user_dict}.

    Data structure choice:
    - dict for O(1) average lookup by key.

    Duplicate names:
    - last one wins (standard dict overwrite behavior).
    """
    # Fast, idiomatic comprehension
    return {u["name"]: u for u in users}


def find_user_by_name(users: List[User], name: str) -> Optional[User]:
    """
    Find a user's profile by name from a list of user data.

    REQUIRED by tests:
    - 'users' is a list of dicts (not a prebuilt index).
    - Return the dict if found; else None.

    Efficiency strategy:
    - Convert list -> dict index for O(1) lookup.
    - Cache the index by id(users) to make repeated calls very fast.

    Important caveat:
    - If you mutate 'users' in place after caching (append/remove/edit dicts),
      the cache can become stale. If your app mutates users, remove caching.
    """
    # Function-level cache: { id(users_list) : {name: user_dict} }
    cache: Dict[int, UserIndex] = getattr(find_user_by_name, "_cache", {})
    setattr(find_user_by_name, "_cache", cache)

    users_id = id(users)
    index = cache.get(users_id)
    if index is None:
        # Build once, then reuse for subsequent lookups with the same list object
        index = _build_user_index(users)
        cache[users_id] = index

    return index.get(name)


# ----------------------------------------------
# Problem 3: Listing even numbers in order
# ----------------------------------------------
def get_list_of_even_numbers(numbers: Iterable[int]) -> List[int]:
    """
    Return a new list containing only the even integers from the input iterable,
    preserving the original order.

    Data structure choice:
    - list is the correct output type and preserves order naturally.
    """
    return [n for n in numbers if n % 2 == 0]


# -----------------------------
# Why these changes (brief)
# -----------------------------
REASONS = """
Problem 1:
- Switched to set membership/intersection because list membership is O(n) and
  becomes a bottleneck for large inputs; set membership is O(1) average.

Problem 2:
- Tests pass a list, so using user_index.get(...) failed (list has no .get).
- Built a dict index (name -> profile) because username is a unique key and
  dict lookup is O(1) average vs O(n) list scan.
- Added caching keyed by id(users) to avoid rebuilding the index on every call
  in workloads with repeated lookups.

Problem 3:
- Used list comprehension for speed + clarity; preserves order by construction.
""".strip()