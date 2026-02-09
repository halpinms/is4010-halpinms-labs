"""
Optimized solutions for:
1) Finding common items between two large supplier product ID lists
2) Fast user profile lookup by username
3) Filtering even numbers while preserving input order

Notes:
- Problem 1 uses a set for O(1) average membership checks.
- Problem 2 builds a dict index for O(1) average lookups; prefer building once.
- Problem 3 uses a list comprehension (fast + preserves order).
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Any, Dict, Hashable, List, Optional, TypeVar

T = TypeVar("T", bound=Hashable)  # needed for set/dict keys

User = Dict[str, Any]
UserIndex = Dict[str, User]


# -----------------------------
# Problem 1: Common product IDs
# -----------------------------
def find_common_elements(list1: Iterable[T], list2: Iterable[T]) -> List[T]:
    """
    Find elements present in BOTH inputs.

    Efficiency:
    - Builds a set from the smaller input when lengths are known (minimizes memory).
    - Membership checks are O(1) average.

    Behavior:
    - Order of result is NOT guaranteed.
    - Duplicates in the "scanned" iterable WILL be preserved (multiset-like),
      e.g., if list2 contains the same common ID twice, it will appear twice.

    If you need UNIQUE common IDs, use: find_common_elements_unique().
    """
    # If both inputs are sequences, we can choose the smaller to set-ify.
    if isinstance(list1, Sequence) and isinstance(list2, Sequence):
        small, large = (list1, list2) if len(list1) <= len(list2) else (list2, list1)
        s = set(small)
        return [x for x in large if x in s]

    # Fallback for non-sized iterables (generators, etc.)
    s = set(list1)
    return [x for x in list2 if x in s]


def find_common_elements_unique(list1: Iterable[T], list2: Iterable[T]) -> List[T]:
    """
    Return UNIQUE elements present in both inputs (set semantics).
    Order is not guaranteed.
    """
    return list(set(list1).intersection(list2))


# -----------------------------------------
# Problem 2: User profile lookup by username
# -----------------------------------------
def build_user_index(users: Iterable[User]) -> UserIndex:
    """
    Build a username -> user profile index for fast repeated lookups.

    Efficiency:
    - One-time O(n) build
    - O(1) average lookup thereafter

    Assumptions:
    - Each user dict contains at least: 'name', 'age', 'email'
    - Username ('name') is unique. If duplicates exist, the LAST one wins.
      (If you want different behavior, see clarifying questions below.)
    """
    index: UserIndex = {}
    for u in users:
        name = u["name"]  # KeyError here is intentional (fail fast on bad schema)
        index[name] = u
    return index


def find_user_by_name(user_index: UserIndex, name: str) -> Optional[User]:
    """
    O(1) average lookup by username using a prebuilt index.
    """
    return user_index.get(name)


# If you *must* keep signature (users: list[dict]) and you call it repeatedly,
# this cached variant avoids rebuilding the index every call.
# NOTE: Cache is in-process and keyed by id(users) (list identity).
def find_user_by_name_cached(users: List[User], name: str) -> Optional[User]:
    """
    Faster repeated lookups without changing your calling code.
    Builds and caches a dict index the first time it's called for a given users list.

    Tradeoff:
    - Slight memory overhead to store the index in a cache.
    - Cache invalidation: if you mutate 'users' in place, the cached index can become stale.
      (If 'users' is immutable after load, this is safe and very fast.)
    """
    cache: Dict[int, UserIndex] = getattr(find_user_by_name_cached, "_cache", {})
    setattr(find_user_by_name_cached, "_cache", cache)

    users_id = id(users)
    index = cache.get(users_id)
    if index is None:
        index = {u["name"]: u for u in users}
        cache[users_id] = index

    return index.get(name)


# ----------------------------------------------
# Problem 3: Even numbers preserving input order
# ----------------------------------------------
def get_list_of_even_numbers(numbers: Iterable[int]) -> List[int]:
    """
    Return even numbers in the same order as the input.
    """
    return [n for n in numbers if n % 2 == 0]


# -----------------------------
# Clarifying questions (optional)
# -----------------------------
CLARIFYING_QUESTIONS = """
Answering these lets me lock in the "right" behavior (not just fast behavior):

Problem 1:
1) Should the output contain duplicates if the same product ID appears multiple times
   across the supplier lists? (Current: preserves duplicates from the scanned side.)
2) Are product IDs always hashable (e.g., int/str)? If IDs can be dict/list, we need a different approach.

Problem 2:
3) Is 'name' guaranteed unique? If duplicates exist, should we keep first, last, or return all matches?
4) Do you mutate the users list after load? If yes, avoid caching-by-id or rebuild index on changes.

Problem 3:
5) Numbers always int? If floats can appear, should 2.0 count as even? (Current assumes int.)
""".strip()