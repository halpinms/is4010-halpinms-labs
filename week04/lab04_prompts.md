## Prompt 1:

Your Persona: You are an expert-level Python developer.

Your Task: I am going to share some scripts with you. I want you to proof read them and then make necessary alterations of my code. Your primary purpose is to recommend and determine the most efficient data structure to use in my script. However, please make any other changes for efficiency or standardized developer syntax.

Please also list reasons why alterations were made and data types chosen.

Thank you.

## Prompt 1 Response with Reasonings:

#### Problem 1: Finding common items (large product ID lists)
Best data structure

Use a set for membership checks and intersection.

Time: O(n + m) average (build set + scan/lookup)

Memory: O(min(n, m)) if you build a set from the smaller list

Implementation

```python 
from collections.abc import Iterable
from typing import TypeVar, List


T = TypeVar("T")


def find_common_elements(list1: Iterable[T], list2: Iterable[T]) -> List[T]:
    """
    Return a list of elements present in both iterables (order not guaranteed).
    Deduplicates common elements (set semantics).
    """
    # Convert the smaller input to a set to minimize memory.
    # If you truly only have lists, len() works; if not, fall back to building one set.
    try:
        if len(list1) <= len(list2):  # type: ignore[arg-type]
            small, large = list1, list2
        else:
            small, large = list2, list1
        s = set(small)
        return [x for x in large if x in s]
    except TypeError:
        # Handles iterables without __len__ (generators, etc.)
        s = set(list1)
        return [x for x in list2 if x in s]
```

#### Why these alterations

set membership is average O(1) vs list membership O(n).

Building the set from the smaller input reduces memory.

List comprehension is faster and more idiomatic than manual loops.

Note: This returns duplicates from the “large” list if it contains duplicates. If you want unique common IDs only:

```python
def find_common_elements_unique(list1, list2):
    return list(set(list1).intersection(list2))
```
#### Problem 2: User profile lookup (frequent username → profile)
Best data structure

Use a dict keyed by username ({name: profile}).

Lookup time: O(1) average per query vs O(n) scanning a list.

Implementation options
A) Fast repeated lookups: build an index once
from typing import Dict, Optional, Any, Iterable

```python
User = Dict[str, Any]
UserIndex = Dict[str, User]


def build_user_index(users: Iterable[User]) -> UserIndex:
    """
    Build a username -> user dict for O(1) lookups.
    If duplicate names exist, the last one wins (can be changed).
    """
    index: UserIndex = {}
    for u in users:
        # Fail fast if schema is wrong; remove if you prefer permissive behavior.
        name = u["name"]
        index[name] = u
    return index


def find_user_by_name(user_index: UserIndex, name: str) -> Optional[User]:
    """O(1) average lookup by username."""
    return user_index.get(name)
```
Usage:

```python

user_index = build_user_index(users)   # do this once after loading
profile = find_user_by_name(user_index, "maxwell")
B) If you must keep the original function signature

```
You can still do it, but avoid rebuilding the dict on every call by caching (simple and effective):

from typing import List

```python
def find_user_by_name(users: List[User], name: str) -> Optional[User]:
    """
    If called repeatedly with the same 'users' list, caches an index to avoid O(n)
    scans on every call.
    """
    # Cache stored on the function object (works in-process).
    cache = getattr(find_user_by_name, "_cache", None)
    if cache is None:
        cache = {}
        setattr(find_user_by_name, "_cache", cache)


    users_id = id(users)
    index = cache.get(users_id)
    if index is None:
        index = {u["name"]: u for u in users}
        cache[users_id] = index


    return index.get(name)
```
Why these alterations

Replacing list scans with dict lookups converts a hot path from O(n) to O(1) average.

Building the index once is the standard approach for performance-critical key-based retrieval.

.get() is idiomatic and avoids KeyError.

If duplicates are possible: decide policy:

raise an error, keep first, keep last, or store a list of profiles per name (defaultdict(list)).

##### Problem 3: Listing even numbers in order (must preserve order)
Best data structure

A list is already optimal because:

You need ordered output.

You’re filtering and returning a new sequence.

Implementation
```python
from typing import Iterable, List


def get_list_of_even_numbers(numbers: Iterable[int]) -> List[int]:
    """Return even numbers in the same order they appear."""
    return [n for n in numbers if n % 2 == 0]
```
Why these alterations

List comprehension is fast, clear, and preserves order naturally.

No benefit to set here because sets lose order and would remove duplicates.

#### Summary of data structure choices

Problem 1: set for fast membership / intersection (order irrelevant).

Problem 2: dict index keyed by username for constant-time lookup.

Problem 3: list (filtering while preserving order).

If you tell me approximate sizes (e.g., list1 5M IDs, list2 2M IDs; users 200k), I can tune further (e.g., memory-aware strategies, handling duplicates, streaming iterables, or using array('I')/NumPy when IDs are numeric).

## Prompt 2
can you give me everything in one code block, if you need some clarifying answers from me, feel free to ask them first

## Prompt Response 2

```python
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
```