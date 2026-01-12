# Lab 07: Working with External Data

**Due**: End of week (Sunday at 11:59 PM)
**Points**: 10 points
**Chapter**: Chapter 7 - Data and APIs

## Objective

This lab is designed to give you hands-on practice with the two main ways applications interact with data: persisting it locally to files and fetching it from the web. You will build a simple contact book that saves its data to a JSON file and a separate script that consumes a live web API.

---

## Background

Modern applications rely on two fundamental data operations: **local persistence** and **remote data fetching**. [JSON (JavaScript Object Notation)](https://www.json.org/) is the universal format for both, used everywhere from [configuration files](https://docs.python.org/3/library/json.html) to [REST APIs](https://restfulapi.net/).

**Real-world applications:**
- **File I/O**: Save user preferences, cache data, store application state
- **APIs**: Fetch weather data, integrate payment systems, access social media
- **JSON**: Configuration files, data exchange between services, API responses
- **Error handling**: Gracefully handle network failures and missing files

**Key concepts applied:**
- **[File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)**: Reading and writing files with [context managers](https://docs.python.org/3/reference/compound_stmts.html#with)
- **[JSON](https://docs.python.org/3/library/json.html)**: [json.dump()](https://docs.python.org/3/library/json.html#json.dump) for writing, [json.load()](https://docs.python.org/3/library/json.html#json.load) for reading
- **[HTTP requests](https://requests.readthedocs.io/)**: Making [GET requests](https://requests.readthedocs.io/en/latest/api/#requests.get) with the [requests library](https://requests.readthedocs.io/)
- **[Exception handling](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)**: [FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError), [requests.exceptions](https://requests.readthedocs.io/en/latest/api/#exceptions)

**Documentation & Resources:**
- [Python JSON module](https://docs.python.org/3/library/json.html)
- [json.dump() documentation](https://docs.python.org/3/library/json.html#json.dump)
- [json.load() documentation](https://docs.python.org/3/library/json.html#json.load)
- [requests library](https://requests.readthedocs.io/)
- [requests.get()](https://requests.readthedocs.io/en/latest/api/#requests.get)
- [response.json()](https://requests.readthedocs.io/en/latest/api/#requests.Response.json)
- [response.raise_for_status()](https://requests.readthedocs.io/en/latest/api/#requests.Response.raise_for_status)
- [File I/O tutorial](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Context managers (with statement)](https://docs.python.org/3/reference/compound_stmts.html#with)
- [Exception handling](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
- [PokeAPI documentation](https://pokeapi.co/docs/v2)
- [REST API principles](https://restfulapi.net/)

---

## Prerequisites

For part 2 of this lab, you will need to install the `requests` library, which is the standard for making HTTP requests in python. Open your terminal and run the following command:
`pip install requests`

-----

## Part 1: the JSON contact book

### Your task

You will complete two functions to handle saving and loading a list of contacts using the JSON format.

1.  In your forked repository, navigate to the `lab07/` folder and create a new file named `lab07_contact_book.py`.
2.  Copy all the python code from the "contact book code" section below into this new file.
3.  Complete the `save_contacts_to_json` and `load_contacts_from_json` functions according to their docstrings. The `load` function must handle a `FileNotFoundError` gracefully.

### Contact book code

```python
import json

def save_contacts_to_json(contacts, filename):
    """
    Saves a list of contacts (dictionaries) to a file in JSON format.

    Parameters
    ----------
    contacts : list
        A list of contact dictionaries.
    filename : str
        The name of the file to save the contacts to.
    """
    # Use with open(...) and json.dump() to write the contacts list
    # to the specified file. Use an indent of 4 for readability.
    pass

def load_contacts_from_json(filename):
    """
    Loads a list of contacts from a JSON file.

    Parameters
    ----------
    filename : str
        The name of the file to load contacts from.

    Returns
    -------
    list
        A list of contact dictionaries. Returns an empty list if the
        file does not exist.
    """
    # Use a try...except block to handle the FileNotFoundError.
    # If the file exists, use with open(...) and json.load() to read
    # and return the contacts.
    # If the file does not exist, return an empty list.
    pass

if __name__ == '__main__':
    # Main execution block to test the functions
    contacts_file = 'contacts.json'

    # Try to load existing contacts
    my_contacts = load_contacts_from_json(contacts_file)
    print(f"Loaded {len(my_contacts)} contact(s).")

    # Add a new contact (as a dictionary)
    new_contact = {"name": "Charles Babbage", "email": "charles@computers.org"}
    my_contacts.append(new_contact)
    print(f"Added a new contact for {new_contact['name']}.")

    # Save the updated list of contacts
    save_contacts_to_json(my_contacts, contacts_file)
    print("Saved contacts to disk.")
```

-----

## Part 2: the API client

### Your task

For this part, you will write a script that fetches live data from a public web API and displays it.

1.  In the `lab07/` folder of your forked repository, create a new file named `lab07_api_client.py`.
2.  Choose a public API to work with. Here are some simple options that don't require an API key:
      * **Pokémon API**: `https://pokeapi.co/api/v2/pokemon/ditto`
      * **Open Trivia DB**: `https://opentdb.com/api.php?amount=1`
      * **Public APIs List**: `https://api.publicapis.org/random`
3.  Copy the python code from the "API client code" section below into your new file.
4.  Complete the `get_api_data` function. It should use the `requests` library to fetch data from the provided URL and return the parsed JSON. It must handle potential errors.

### API client code

```python
import requests

def get_api_data(url):
    """
    Fetches and parses JSON data from a given API url.

    Parameters
    ----------
    url : str
        The URL of the API endpoint.

    Returns
    -------
    dict or None
        A dictionary containing the parsed JSON data, or None if
        the request fails or the response is not valid JSON.
    """
    # Use a try...except block to handle potential requests.exceptions.RequestException
    try:
        # Make a GET request to the URL
        response = requests.get(url)
        
        # Raise an HTTPError if the response was an error
        response.raise_for_status()

        # Parse and return the JSON data
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None
    except requests.exceptions.JSONDecodeError:
        print("Error: Failed to decode JSON from response.")
        return None


if __name__ == '__main__':
    # Example using the Pokémon API
    pokemon_url = "https://pokeapi.co/api/v2/pokemon/snorlax"
    
    # Get the data from the API
    pokemon_data = get_api_data(pokemon_url)

    # If data was successfully fetched, display some of it
    if pokemon_data:
        print(f"Successfully fetched data for: {pokemon_data['name'].title()}")
        print(f"Weight: {pokemon_data['weight']} hectograms")
        print("Abilities:")
        for ability in pokemon_data['abilities']:
            print(f"  - {ability['ability']['name']}")

```

-----

## Part 3: Testing Your Code

Good news! Part 2 (`lab07_api_client.py`) doesn't require automated tests since it depends on external APIs. However, you should manually test it to ensure it works correctly.

**For Part 1 (Contact Book)**, create a test file to verify your JSON functions work correctly.

### Instructions

1. In the `lab07/` folder, create a file named `test_lab07.py`
2. Copy the test code below into your new file

### Test code

```python
import pytest
import json
import os
from lab07_contact_book import save_contacts_to_json, load_contacts_from_json

def test_save_contacts_creates_file():
    """Test that save_contacts_to_json creates a JSON file."""
    test_file = 'test_contacts.json'
    test_contacts = [{"name": "Alice", "email": "alice@test.com"}]

    # Clean up if file exists
    if os.path.exists(test_file):
        os.remove(test_file)

    save_contacts_to_json(test_contacts, test_file)
    assert os.path.exists(test_file), "File was not created"

    # Clean up
    os.remove(test_file)

def test_save_and_load_contacts():
    """Test saving and loading contacts returns the same data."""
    test_file = 'test_contacts.json'
    test_contacts = [
        {"name": "Bob", "email": "bob@test.com"},
        {"name": "Charlie", "email": "charlie@test.com"}
    ]

    save_contacts_to_json(test_contacts, test_file)
    loaded_contacts = load_contacts_from_json(test_file)

    assert loaded_contacts == test_contacts

    # Clean up
    os.remove(test_file)

def test_load_nonexistent_file_returns_empty_list():
    """Test that loading a non-existent file returns an empty list."""
    result = load_contacts_from_json('nonexistent_file.json')
    assert result == [], "Should return empty list for non-existent file"

def test_save_empty_list():
    """Test saving an empty contact list."""
    test_file = 'test_empty.json'
    save_contacts_to_json([], test_file)

    with open(test_file, 'r') as f:
        data = json.load(f)

    assert data == []
    os.remove(test_file)

def test_save_contact_with_multiple_fields():
    """Test saving contacts with various fields."""
    test_file = 'test_complex.json'
    contacts = [
        {
            "name": "Eve",
            "email": "eve@test.com",
            "phone": "555-1234",
            "company": "TechCorp"
        }
    ]

    save_contacts_to_json(contacts, test_file)
    loaded = load_contacts_from_json(test_file)

    assert loaded == contacts
    assert loaded[0]["phone"] == "555-1234"

    os.remove(test_file)

def test_json_file_is_formatted():
    """Test that saved JSON file has proper formatting (indentation)."""
    test_file = 'test_format.json'
    contacts = [{"name": "Test", "email": "test@test.com"}]

    save_contacts_to_json(contacts, test_file)

    with open(test_file, 'r') as f:
        content = f.read()

    # Check for indentation (should have newlines and spaces)
    assert '\n' in content, "JSON should be formatted with newlines"
    assert '    ' in content, "JSON should have indentation"

    os.remove(test_file)
```

### Running tests

```bash
# Navigate to repository root
cd /path/to/your/repository

# Run Lab 07 tests
pytest lab07/test_lab07.py -v

# Run all tests
pytest
```

-----

## 🚨 Troubleshooting

**Common issues?** See the [Common Troubleshooting Guide](../resources/TROUBLESHOOTING.md) for general Python, testing, and GitHub Actions problems.

**Lab 07-specific issues:**

### **Problem: "ModuleNotFoundError: No module named 'requests'"**
- **Cause**: requests library not installed
- **Solution**:
  - Activate your virtual environment first
  - Install: `pip install requests`
  - Verify: `pip list | grep requests`
  - Make sure you're installing in the correct environment

### **Problem: "requests.exceptions.ConnectionError" when running API client**
- **Cause**: Network issues or API endpoint down
- **Solution**:
  - Check your internet connection
  - Try a different API endpoint
  - Some networks block certain websites - try from home if on campus WiFi
  - API might be temporarily down - try again later

### **Problem: "FileNotFoundError" when trying to load contacts**
- **Cause**: `load_contacts_from_json()` not handling missing file gracefully
- **Solution**:
  - Wrap `json.load()` in try/except block:
    ```python
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    ```

### **Problem: "JSONDecodeError: Expecting value"**
- **Cause**: JSON file is empty or corrupted
- **Solution**:
  - Delete the JSON file and let the program create a new one
  - Make sure you're using `json.dump()` with proper syntax
  - Check that file has valid JSON: `[{"name": "test"}]`

### **Problem: "PermissionError: [Errno 13] Permission denied"**
- **Cause**: File is open in another program or wrong permissions
- **Solution**:
  - Close the JSON file if it's open in an editor
  - Make sure you have write permissions in the directory
  - Try saving to a different filename

### **Problem: "TypeError: the JSON object must be str, bytes or bytearray, not list"**
- **Cause**: Using `json.load()` instead of `json.dump()` or vice versa
- **Solution**:
  - Use `json.dump(data, file)` for writing (save function)
  - Use `json.load(file)` for reading (load function)
  - Remember: dump = write, load = read

### **Problem: "API returns 404 Not Found"**
- **Cause**: URL is incorrect or resource doesn't exist
- **Solution**:
  - Check the URL for typos
  - Test the URL in your web browser first
  - Make sure Pokemon name (or resource) exists
  - Use lowercase for Pokemon names: "snorlax" not "Snorlax"

### **Problem: "KeyError: 'name'" when accessing API data**
- **Cause**: API response structure different than expected
- **Solution**:
  - Print the full response to see structure: `print(pokemon_data)`
  - Use `.get()` method for safe access: `pokemon_data.get('name', 'Unknown')`
  - Check the API documentation for correct field names

### **Problem: "Test files created during testing aren't cleaned up"**
- **Cause**: Test failed before cleanup code ran
- **Solution**:
  - Manually delete test JSON files: `test_contacts.json`, etc.
  - Use pytest fixtures for more reliable cleanup:
    ```python
    import pytest

    @pytest.fixture
    def test_file():
        filename = 'test_temp.json'
        yield filename
        if os.path.exists(filename):
            os.remove(filename)
    ```

### **Problem: "My contact book creates a file but it's not readable"**
- **Cause**: Not using `indent` parameter in `json.dump()`
- **Solution**:
  - Use: `json.dump(contacts, f, indent=4)`
  - The `indent=4` makes the JSON human-readable
  - Without it, everything is on one line

-----

## Expected Repository Structure

Your repository should now contain all 7 labs completed so far:

```
is4010-labs-yourname/
├── lab01/                    # Development toolkit setup
├── lab02/                    # AI-assisted development
├── lab03/                    # Python basics + testing
├── lab04/                    # Data structures
├── lab05/                    # Functions and error handling
├── lab06/                    # Object-oriented programming
└── lab07/                    # Data and APIs ✓
    ├── lab07_contact_book.py
    ├── lab07_api_client.py
    ├── test_lab07.py
    └── contacts.json (created when you run the program)
```

This demonstrates your progression through Python fundamentals, from basic syntax to working with external data sources.

-----

## 🤖 AI Assistance Strategy

This lab introduces new concepts (JSON and APIs) - AI tools can accelerate your learning:

### When to Use AI

1. **Understanding JSON operations**: Ask AI to explain json.dump() vs json.load()
2. **Debugging JSON errors**: Get help with JSONDecodeError and malformed JSON
3. **API integration**: AI excels at explaining HTTP requests and response handling
4. **Writing test cases**: Generate test scenarios for file I/O and API calls

### Example Prompts

1. **For JSON file operations**:
   ```
   "Show me how to save a list of Python dictionaries to a JSON file with proper formatting using json.dump(). Include error handling for file write errors."
   ```

2. **For loading JSON safely**:
   ```
   "I need to load contacts from a JSON file. If the file doesn't exist, return an empty list. Show me how to handle FileNotFoundError properly."
   ```

3. **For API requests**:
   ```
   "Using the requests library, show me how to fetch data from https://pokeapi.co/api/v2/pokemon/pikachu and parse the JSON response. Include error handling for network failures."
   ```

4. **For debugging JSON errors**:
   ```
   "I'm getting 'JSONDecodeError: Expecting value' when loading my contacts.json file. Here's my code: [paste code]. What's wrong?"
   ```

5. **For test writing**:
   ```
   "Write pytest test cases for save_contacts_to_json() and load_contacts_from_json(). Test normal operation, empty lists, and file not found scenarios."
   ```

6. **For API error handling**:
   ```
   "What exceptions should I catch when making HTTP requests with the requests library? Show me a try-except block that handles network errors gracefully."
   ```

### Conversation Example: JSON File I/O

**You**: "I need to save a list of contact dictionaries to a JSON file. How do I do this in Python?"

**AI**: "Use `json.dump()` with a file opened in write mode:

```python
import json

contacts = [
    {\"name\": \"Alice\", \"email\": \"alice@example.com\"},
    {\"name\": \"Bob\", \"email\": \"bob@example.com\"}
]

with open('contacts.json', 'w') as f:
    json.dump(contacts, f, indent=4)
```

The `indent=4` makes the JSON file human-readable with proper formatting."

**You**: "How do I load it back?"

**AI**: "Use `json.load()` with error handling:

```python
try:
    with open('contacts.json', 'r') as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = []  # File doesn't exist yet
```

This returns an empty list if the file hasn't been created yet."

### Conversation Example: API Integration

**You**: "I want to fetch Pokemon data from PokeAPI. How do I make the request and handle errors?"

**AI**: "Here's a robust approach with full error handling:

```python
import requests

def get_pokemon_data(name):
    url = f\"https://pokeapi.co/api/v2/pokemon/{name}\"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad status
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f\"HTTP error: {e}\")
        return None
    except requests.exceptions.RequestException as e:
        print(f\"Network error: {e}\")
        return None
```

This handles both HTTP errors (404, 500) and network issues (timeout, no internet)."

**You**: "What if the response isn't valid JSON?"

**AI**: "Add JSONDecodeError handling:

```python
except requests.exceptions.JSONDecodeError:
    print(\"Error: Response is not valid JSON\")
    return None
```

This catches cases where the server returns non-JSON data."

### Recommended Tools

- **[ChatGPT](https://chat.openai.com/)** - Excellent for explaining JSON and API concepts
- **[Claude](https://claude.ai/)** - Great for debugging JSON errors and test writing
- **[Gemini](https://gemini.google.com/)** - Helpful for requests library usage patterns
- **[GitHub Copilot](https://github.com/features/copilot)** - In-editor assistance for writing test cases

### When to Debug Yourself

- Simple syntax errors (missing commas in JSON, unclosed braces)
- File path issues (check your working directory)
- Import errors (make sure requests is installed)
- Reading Python error messages (they're usually very clear)

**Pro tip**: When working with APIs, test the URL in your browser first to see the raw JSON response!

-----

## Submission

When you are finished, commit and push your lab files to your forked GitHub repository:

```bash
git add lab07/
git commit -m "Complete Lab 07: Working with External Data"
git push origin main
```

### Verification

1. Go to your repository on GitHub
2. Click the **Actions** tab
3. Find the **Lab 07** workflow
4. Verify it shows a **green checkmark ✓**

**Grading**: Your lab is graded based on GitHub Actions CI/CD status. All tests must pass (green checkmark ✓) to receive full credit (10 points).

-----

## 📚 Additional Resources

- **Python JSON module**: https://docs.python.org/3/library/json.html
- **Requests library**: https://requests.readthedocs.io/
- **File I/O in Python**: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- **Public APIs**: https://github.com/public-apis/public-apis
- **PokeAPI Documentation**: https://pokeapi.co/docs/v2

-----

**Need Help?**
- Review Chapter 7 in the textbook
- Check the troubleshooting section above
- See [Common Troubleshooting Guide](../resources/TROUBLESHOOTING.md)
- Use AI assistants (Copilot, Gemini CLI, ChatGPT)
- Ask on the course discussion board
- Attend office hours