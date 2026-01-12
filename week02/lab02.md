# Lab 02: AI-assisted development

**Due**: End of week (Sunday at 11:59 PM)
**Points**: 10 points
**Chapter**: Chapter 2 - The developer's guide to generative AI

---

## Learning Objectives

By the end of this lab, you will be able to:

- Use [GitHub Copilot](https://github.com/features/copilot) to generate code from function stubs and docstrings
- Craft effective prompts for conversational AI models using the CPTF (Context, Persona, Task, Format) framework
- Understand the difference between in-editor AI assistants (Copilot) and conversational AI (ChatGPT, Claude, Gemini)
- Write clear [NumPy-style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html) that communicate intent to AI tools
- Debug, refactor, and document code using AI-powered conversations
- Apply appropriate AI tools for different development tasks

---

## Background

Modern software development increasingly relies on AI-powered tools to enhance productivity. These tools fall into two main categories:

1. **In-editor code assistants** like [GitHub Copilot](https://github.com/features/copilot) excel at generating code in your workflow, suggesting completions as you type, and implementing functions from docstrings.

2. **Conversational AI models** like [ChatGPT](https://chat.openai.com/), [Claude](https://claude.ai/), and [Gemini](https://gemini.google.com/) are powerful partners for debugging, refactoring, explaining complex concepts, and problem-solving through dialogue.

A modern developer knows when to use each tool and how to communicate effectively with both.

### Key Concepts

- **Docstring**: A special comment wrapped in triple quotes (`"""..."""`) that explains what a function or class does
- **NumPy docstring style**: A clean, structured format for documenting Python functions with sections for Parameters, Returns, and more
- **CPTF framework**: A prompt engineering approach using Context, Persona, Task, and Format to get better AI responses
- **Code stub**: A function with a signature and docstring but no implementation (contains `pass`)
- **Refactoring**: Improving code structure and readability without changing its behavior

### Real-World Applications

- **GitHub Copilot** can generate boilerplate code, write tests, and implement algorithms from descriptions, saving hours of typing
- **Conversational AI** helps debug mysterious errors, explain unfamiliar codebases, and suggest better approaches to problems
- **Docstrings** serve as contracts between functions and their users, and guide AI tools to generate correct implementations
- **Prompt engineering** is becoming a critical skill as AI tools become standard in professional development workflows

---

## Prerequisites

For this lab, you need:

- [ ] Completed Lab 01 (development environment set up)
- [ ] GitHub account with [GitHub Student Developer Pack](https://education.github.com/pack) (provides free Copilot)
- [ ] GitHub Copilot installed and activated in VS Code
- [ ] Access to a conversational AI (ChatGPT, Claude, or Gemini - all have free tiers)
- [ ] Your `is4010-[username]-labs` repository cloned locally
- [ ] Approximately **60-90 minutes** to complete both parts

**If you haven't set up GitHub Copilot yet**: See [Section 7 of SETUP_GUIDE.md](../resources/SETUP_GUIDE.md#7-next-steps-github-copilot-setup) for installation instructions.

---

## Instructions

### Part 1: Copilot driving school (30-40 minutes)

In this part, you'll use GitHub Copilot to implement Python functions from docstrings. This demonstrates how AI can generate code when given clear specifications.

#### Create Your Python File

1. **Navigate to your repository**:
   ```bash
   cd ~/is4010/is4010-YOUR-USERNAME-labs
   ```

2. **Ensure module02 folder exists** (it should already exist from the template):
   ```bash
   ls module02/
   ```

3. **Create the Python file**:
   ```bash
   # Using VS Code
   code module02/module02.py

   # Or using touch
   touch module02/module02.py
   ```

#### Implement Functions with Copilot

1. **Copy the function stubs below** into your `module02/module02.py` file

2. **For each function**:
   - Place your cursor inside the function body (after the docstring, on a new line)
   - Wait for GitHub Copilot to suggest an implementation
   - Review the suggestion (does it match the docstring?)
   - Press `Tab` to accept, or press `Alt + ]` / `Option + ]` to see alternatives
   - **Important**: Don't just accept the first suggestion - make sure it looks correct!

3. **Test your functions** after Copilot generates them:
   ```bash
   # Activate your virtual environment
   source venv/bin/activate  # macOS/Linux
   source venv/Scripts/activate  # Windows Git Bash

   # Run Python interactively to test
   python -i module02/module02.py

   # Try your functions:
   >>> factorial(5)
   120
   >>> is_prime(17)
   True
   >>> reverse_string("hello")
   'olleh'
   >>> exit()
   ```

#### Function Stubs

Copy all three functions into `module02/module02.py`:

```python
def factorial(n):
    """Calculate the factorial of a non-negative integer.

    Parameters
    ----------
    n : int
        The non-negative integer to calculate the factorial of.

    Returns
    -------
    int
        The factorial of n. Returns 1 for n = 0.

    Examples
    --------
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    pass


def is_prime(number):
    """Check if a number is a prime number.

    A prime number is a natural number greater than 1 that has no
    positive divisors other than 1 and itself.

    Parameters
    ----------
    number : int
        The integer to check.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.

    Examples
    --------
    >>> is_prime(17)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    pass


def reverse_string(s):
    """Reverse a given string.

    Parameters
    ----------
    s : str
        The string to be reversed.

    Returns
    -------
    str
        The reversed string.

    Examples
    --------
    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("Python")
    'nohtyP'
    """
    pass
```

**Pro tip**: If Copilot isn't suggesting anything, try adding a comment like `# Implementation:` on a new line after the docstring.

---

### Part 2: The prompt engineering challenge (30-40 minutes)

In this part, you'll use conversational AI to solve three common development tasks: debugging, refactoring, and documenting code.

#### Create Your Markdown File

```bash
# Create the prompts file
code module02/module02_prompts.md

# Or using touch
touch module02/module02_prompts.md
```

#### Challenge Structure

For each of the three problems below, you'll:

1. **Craft a high-quality prompt** using the CPTF framework:
   - **Context**: Provide the actual code and explain the situation
   - **Persona**: Tell the AI what role to take (e.g., "You are a senior Python developer")
   - **Task**: Be specific about what you want (debug, refactor, document)
   - **Format**: Specify how you want the response (code block, explanation, step-by-step)

2. **Document your work** in `module02_prompts.md`:
   - A heading for the problem (e.g., `### Problem 1: Debugging`)
   - The exact prompt you used (in a code block or quote block)
   - The final, corrected code the AI provided (in a Python code block)

#### Example Format for module02_prompts.md

```markdown
# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
```
[Your prompt here using CPTF framework]
```

**AI's Corrected Code:**
```python
# AI's fixed version of the code
```

**What I Learned:**
[Brief reflection on what the AI helped you understand]

---

## Problem 2: Refactoring

[Same structure as Problem 1]

---

## Problem 3: Documenting

[Same structure as Problem 1]
```

#### Problem 1: Debugging a buggy function

This function is supposed to calculate the sum of all **even** numbers in a list, but it contains a logical error.

**Your task**: Craft a prompt that asks the AI to find and fix the bug.

**Buggy code**:
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

**Hint**: A good prompt would include the code, explain what it *should* do, mention what it's *actually* doing wrong (if you know), and ask for the fix.

---

#### Problem 2: Refactoring an unreadable function

This function works correctly, but it's written in a confusing, non-[Pythonic](https://peps.python.org/pep-0020/) way.

**Your task**: Craft a prompt that asks the AI to refactor this code to be more clear, concise, and idiomatic.

**Unreadable code**:
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

**Hint**: Ask for Pythonic improvements like list comprehensions, better iteration patterns, and clearer variable names.

---

#### Problem 3: Documenting a function

This function works correctly but has no documentation.

**Your task**: Craft a prompt that asks the AI to write a professional **NumPy-style** docstring for this function.

**Undocumented code**:
```python
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**Hint**: Specify that you want NumPy-style format, and mention that the function raises a ValueError for invalid inputs.

---

## Expected Output

After completing this lab, you should have:

✅ **module02/module02.py** containing:
- Three working functions (no `pass` statements remaining)
- All functions correctly implementing their docstring specifications
- Code generated with GitHub Copilot assistance

✅ **module02/module02_prompts.md** containing:
- Three sections (one per problem)
- Your actual prompts used with conversational AI
- The AI's corrected/refactored/documented code
- Optional reflections on what you learned

### Sample module02/module02.py

```python
def factorial(n):
    """Calculate the factorial of a non-negative integer.
    [docstring as provided above]
    """
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# ... other functions with working implementations
```

### Sample module02_prompts.md Structure

```markdown
# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
> You are a senior Python developer. I have a function that's supposed to sum
> all even numbers in a list, but it's giving wrong results. [code here]
> Can you identify the bug and provide the corrected version?

**AI's Corrected Code:**
[Python code block with fixed function]

---

[Problems 2 and 3 follow same pattern]
```

---

## Troubleshooting

### GitHub Copilot Not Showing Suggestions

**Problem**: Copilot isn't suggesting code when you place your cursor in the function

**Solutions**:
- Verify Copilot extension is installed and activated in VS Code
- Check you're signed into VS Code with your GitHub account
- Confirm your GitHub Student Developer Pack is active
- Try placing cursor on a new line after the docstring and waiting 2-3 seconds
- Press `Alt + \` (Windows) or `Option + \` (Mac) to manually trigger Copilot
- Check VS Code status bar (bottom right) for Copilot icon - should not have an X

### Copilot Suggestions Don't Match Docstring

**Problem**: Copilot's suggestions are wrong or don't match what the function should do

**Solutions**:
- Write more detailed docstrings with examples
- Add a comment describing the algorithm: `# Use a loop from 2 to n`
- Cycle through alternatives: `Alt + ]` (Windows) or `Option + ]` (Mac)
- Reject suggestion with `Esc` and try typing first line yourself
- Sometimes starting the implementation helps Copilot understand: `result = 0`

### Conversational AI Giving Poor Responses

**Problem**: AI isn't understanding your problem or giving unhelpful answers

**Solutions**:
- **Use CPTF framework more explicitly**:
  - Context: Include the actual code
  - Persona: "You are a senior Python developer"
  - Task: Be specific - "Find and fix the logical error"
  - Format: "Provide the corrected code in a Python code block"
- Provide examples of input/output: "For input [2,4,5], it should return 6"
- Ask follow-up questions if response isn't clear
- Try a different AI model - each has strengths

### Can't Access GitHub Copilot

**Problem**: Don't have Copilot access even with GitHub Student Pack

**Solutions**:
- Apply for GitHub Student Developer Pack: [education.github.com/pack](https://education.github.com/pack)
- Verify student status with your .edu email
- Wait 24-48 hours for approval
- **Alternative**: Use Cursor IDE (has free AI features) or continue with conversational AI only
- Document in your lab that you used conversational AI instead of Copilot

### Not Sure if Functions Work Correctly

**Problem**: Unsure if Copilot generated correct code

**Solutions**:
```bash
# Test interactively
python -i module02/module02.py

# Try the examples from the docstrings:
>>> factorial(5)
120  # Should be 120
>>> factorial(0)
1  # Should be 1
>>> is_prime(17)
True  # Should be True
>>> is_prime(4)
False  # Should be False
```

- If results don't match expected output, reject Copilot's suggestion and try again
- Ask conversational AI to verify: "Is this factorial implementation correct?"

### Markdown Formatting Issues

**Problem**: Not sure how to format module02_prompts.md correctly

**Solutions**:
- Use triple backticks for code blocks: ` ```python `
- Use `##` for main headings, `###` for problem headings
- Preview Markdown in VS Code: `Ctrl+Shift+V` or `Cmd+Shift+V`
- Check the example format provided in Part 2 above
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/) for syntax reference

---

## AI Assistance Strategy

This lab is *about* using AI, so you're encouraged to use AI tools throughout! Here's how to approach different challenges:

### Example Prompts for Common Tasks

**Understanding NumPy docstrings**:
> "Explain the NumPy docstring format for Python functions. Show me an example with Parameters, Returns, and Examples sections."

**Improving your prompts**:
> "I'm trying to debug this Python function with AI. Here's my current prompt: [your prompt]. How can I make it more effective using the CPTF framework?"

**Verifying Copilot suggestions**:
> "GitHub Copilot suggested this implementation for factorial: [code]. Is this correct? Are there edge cases it's missing?"

**Learning from AI responses**:
> "Why is the refactored version of this function more Pythonic than the original? Explain the improvements."

**Debugging prompt issues**:
> "The AI keeps giving me incomplete answers when I ask it to debug this function. How should I rephrase my prompt?"

### When to Use Which AI Tool

**Use GitHub Copilot for**:
- Generating function implementations from docstrings
- Writing boilerplate code quickly
- Autocompleting repetitive patterns
- Implementing well-defined algorithms

**Use Conversational AI for**:
- Debugging mysterious errors
- Understanding why code behaves a certain way
- Refactoring and improving code structure
- Learning best practices and idioms
- Crafting better prompts for Copilot

### Real AI Conversation Example

**You**: I'm working on Lab 02 for my class. I need to debug this Python function using AI. Here's my current prompt: "Fix this code: [code block]". Is this a good prompt?

**AI**: That's a start, but it could be much more effective! Here's how to improve it using CPTF:

**Context**: Explain what the code should do: "This function should sum all even numbers in a list, but it's currently returning the wrong result."

**Persona**: Set expertise level: "You are a senior Python developer helping debug code."

**Task**: Be specific: "Identify the logical error in the conditional statement and provide the corrected version."

**Format**: Request structure: "Provide the fixed code in a Python code block with a brief explanation of the bug."

**Improved prompt**:
```
You are a senior Python developer. I have a function that should sum all
even numbers in a list, but it's returning wrong results. Here's the code:

[code block]

Can you identify the logical error in the conditional statement and provide
the corrected version in a Python code block? Please also explain what
the bug was.
```

This prompt is much more likely to get you a helpful, complete response!

---

**You**: GitHub Copilot suggested this implementation for is_prime, but I'm not sure if it handles edge cases correctly. How can I verify it?

**AI**: Great question! Here are several ways to verify:

1. **Test with examples** from your docstring:
```python
python -i module02/module02.py
>>> is_prime(17)  # Should be True
>>> is_prime(1)   # Should be False (1 is not prime by definition)
>>> is_prime(2)   # Should be True (2 is the smallest prime)
```

2. **Test edge cases** not in docstring:
- Negative numbers: `is_prime(-5)` should be `False`
- Zero: `is_prime(0)` should be `False`
- Large primes: `is_prime(97)` should be `True`

3. **Ask Copilot to add tests**: Create a comment above your function:
```python
# Add test cases for is_prime function
```
Copilot might suggest a test suite!

4. **Verify with conversational AI**: Paste the implementation and ask: "Does this correctly identify prime numbers? Are there any edge cases it misses?"

---

## Submission

### What to Submit

Commit and push your completed `module02/` folder to your GitHub repository. No Canvas submission required.

**Your module02/ folder must contain**:
1. `module02.py` - Three working functions (factorial, is_prime, reverse_string)
2. `module02_prompts.md` - Three prompt engineering solutions

### Git Workflow

```bash
# Navigate to repository
cd ~/is4010/is4010-YOUR-USERNAME-labs

# Verify your changes
git status
ls module02/

# Stage your module02 folder
git add module02/

# Commit with descriptive message
git commit -m "Complete Lab 02: AI-assisted development

- Implemented factorial, is_prime, and reverse_string with Copilot
- Completed prompt engineering challenges for debugging, refactoring, documenting
- Practiced CPTF framework for effective AI prompts"

# Push to GitHub
git push origin main
```

### Verification Checklist

Before the due date, verify:

- [ ] Repository is **private**
- [ ] Instructor (`bgreenwell`) added as collaborator
- [ ] `module02/` folder exists in repository root
- [ ] `module02/module02.py` exists with three complete functions (no `pass` statements)
- [ ] `module02/module02_prompts.md` exists with three problem sections
- [ ] Each function in module02.py works correctly (tested interactively)
- [ ] Each problem in prompts.md includes your prompt and AI's solution
- [ ] Changes successfully pushed to GitHub (visible on website)

---

## Success Criteria

Use this checklist to verify completion:

### Part 1: Copilot Functions
- [ ] **factorial function works**: Returns correct values for n=0, n=5, n=10
- [ ] **is_prime function works**: Correctly identifies primes (17, 29) and non-primes (1, 4, 15)
- [ ] **reverse_string function works**: Correctly reverses strings of various lengths
- [ ] **No `pass` statements**: All functions have actual implementations
- [ ] **Code quality**: Functions are readable and follow docstring specifications

### Part 2: Prompt Engineering
- [ ] **Problem 1 completed**: Debugging prompt and corrected code for sum_of_evens
- [ ] **Problem 2 completed**: Refactoring prompt and improved code for get_names_of_adults
- [ ] **Problem 3 completed**: Documentation prompt and NumPy docstring for calculate_area
- [ ] **CPTF framework applied**: Prompts include context, persona, task, and format
- [ ] **Reflections included**: Optional but recommended - what did you learn from each?

### Grading

**This lab is worth 10 points total:**

- ✅ **7 points**: All three functions in module02.py work correctly
  - 2 points per function (factorial, is_prime, reverse_string)
  - +1 bonus point when all three are perfect

- ✅ **3 points**: Prompt engineering file complete and well-structured
  - 1 point per problem (debugging, refactoring, documenting)
  - Each section must include prompt and AI's solution

**Important**: The automated grading system will actually run your functions with test cases. Make sure they work before submitting!

---

## Looking Ahead

In **Lab 03**, you'll build on these AI skills to:
- Write Python code with proper testing using pytest
- Use AI to help generate test cases
- Apply test-driven development (TDD) practices
- Learn when to trust AI suggestions vs. verify them yourself

The AI prompting skills you practiced today will be valuable throughout the course - you'll use them to debug complex code, understand new concepts, and accelerate your learning.

**Pro tip from Lab 02**: Great docstrings are valuable even when you're not using AI. They serve as contracts that explain what your functions do, making code easier to understand and maintain. Get in the habit of writing them for all your functions!
