# Lab 02: Prompt Engineering Solutions

## Problem #1: Debugging

**My Prompt:**
Context: The following Python function is supposed to calculate the sum of all even numbers in a list, but it contains a logic error.
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total
```
Persona: You are a senior Python developer and an expert in debugging.
Task: Your task is to identify and fix the bug in the provided `sum_of_evens` function so that it correctly calculates the sum of all even numbers in a list.
Format:
1.  Provide the complete, corrected Python code in a single code block.
2.  In a separate "Explanation of Changes" section, briefly describe the bug and the fix you implemented.

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Fixed the bug: now checks for even numbers
            total += num
    return total
```
**Explanation of Changes:**
The primary bug was in the conditional statement `if num % 2 == 1:`. This condition incorrectly checked if a number was *odd*. To correctly sum *even* numbers, the condition was changed to `if num % 2 == 0:`.

## Problem 2: Refactoring

**My Prompt:**
Context: The following Python function `get_names_of_adults` works, but it uses a `for` loop with `range(len(users))` which is not idiomatic.
```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
```
Persona: You are a senior Python developer who specializes in writing clean, efficient code.
Task: Refactor the provided code to be more clear, concise, and idiomatic Python.
Format: Provide the refactored code in a Python code block and briefly explain why the new version is better.

**AI's Corrected Code:**
```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    return [user['name'] for user in users if user['age'] >= 18]
```
This version is more Pythonic and concise. It uses a list comprehension, which is a common and efficient way to create a new list by filtering and transforming items from an existing iterable. This avoids the manual index-based iteration (`for i in range(len(users))`) and makes the code more readable by expressing the logic in a single, declarative line.

## Problem 3: Documenting a function

**My Prompt:**
Context:
```python
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```
Persona: You are a senior Python developer who specializes in writing clean, efficient code.
Task: Using the context of the provided code, please write a professional NumPy-style docstring for this function.
Format: Respond with the format we have been using.

**AI's Corrected Code:**
```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Parameters
    ----------
    length : int or float
        The length of the rectangle. Must be a positive number.
    width : int or float
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    int or float
        The area of the rectangle (length * width).

    Raises
    ------
    ValueError
        If length or width are not positive numbers.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```
**Explanation of Changes:**
I've added a comprehensive NumPy-style docstring to the `calculate_area` function. This docstring includes:
*   A concise summary of the function's purpose.
*   A `Parameters` section detailing `length` and `width`, including their types, descriptions, and constraints.
*   A `Returns` section specifying the return type and what the function returns.
*   A `Raises` section to document the `ValueError` that can be raised, explaining the condition under which it occurs.
This structured docstring enhances readability, maintainability, and allows for automatic documentation generation.

**What I learned:** I learned that Gemini/LLMs can be a useful tool for fixing my illogical, overcomplicated, or confusing code. I also learned how to use Node to complete installations using my terminal. Additionally, I learned how to utilize CLI in order to maximize the automation process of making AI edits to my files.
