# Lab 08: Weather CLI Application

**Due**: End of week (Sunday at 11:59 PM)
**Points**: 10 points
**Chapter**: Chapter 8 - Python CLI Applications

---

## Objective

Build a complete command-line weather application that integrates all the Python concepts you've learned: functions, classes, file I/O, API integration, and error handling. This lab demonstrates how to create a professional CLI tool using `argparse` with multiple subcommands.

**What you'll learn:**
- Building CLI applications with argparse and subcommands
- Integrating external APIs (weather data)
- JSON file persistence for user preferences
- Object-oriented design for real-world applications  
- Comprehensive error handling and user experience
- Professional project structure and testing

---

## Background

[Command-line interfaces (CLIs)](https://en.wikipedia.org/wiki/Command-line_interface) are powerful tools used by developers, system administrators, and power users every day. Modern CLIs use [subcommands](https://docs.python.org/3/library/argparse.html#sub-commands) (like `git add`, `git commit`) to organize functionality. You'll build a weather CLI that fetches current conditions and forecasts while managing a list of favorite locations.

**Real-world applications:**
- [AWS CLI](https://aws.amazon.com/cli/), [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/) - manage cloud resources
- [git](https://git-scm.com/), [npm](https://www.npmjs.com/), [cargo](https://doc.rust-lang.org/cargo/) - development tools
- [kubectl](https://kubernetes.io/docs/reference/kubectl/) - Kubernetes management
- [heroku](https://devcenter.heroku.com/articles/heroku-cli) - application deployment

**Key concepts applied:**
- **Functions** (Lab 5): Organize API calls and data processing
- **Classes** (Lab 6): Weather and Location objects with methods
- **[File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)** (Lab 7): [JSON persistence](https://docs.python.org/3/library/json.html) for favorites
- **APIs** (Lab 7): Fetch live weather data with [requests](https://requests.readthedocs.io/)
- **[argparse](https://docs.python.org/3/library/argparse.html)**: Professional CLI argument parsing

**Documentation & Resources:**
- [argparse documentation](https://docs.python.org/3/library/argparse.html)
- [argparse tutorial](https://docs.python.org/3/howto/argparse.html)
- [argparse add_subparsers](https://docs.python.org/3/library/argparse.html#sub-commands)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [WeatherAPI.com](https://www.weatherapi.com/) (alternative, free tier)
- [requests library](https://requests.readthedocs.io/)
- [requests.get()](https://requests.readthedocs.io/en/latest/api/#requests.get)
- [response.json()](https://requests.readthedocs.io/en/latest/api/#requests.Response.json)
- [JSON in Python](https://docs.python.org/3/library/json.html)
- [PEP 8 Style Guide](https://pep8.org/)

---

## Prerequisites

Before starting this lab, ensure you have:
- [ ] Completed Labs 01-07 (functions, classes, file I/O, APIs)
- [ ] Python 3.10+ installed
- [ ] `requests` library installed: `pip install requests`
- [ ] A free API key from [WeatherAPI.com](https://www.weatherapi.com/signup.aspx)

### Getting your API key

1. Go to [WeatherAPI.com](https://www.weatherapi.com/signup.aspx)
2. Sign up for a free account (no credit card required)
3. Copy your API key from the dashboard
4. **Free tier**: 1 million calls/month - more than enough for this lab

**Security note**: Never commit API keys to GitHub! We'll use environment variables or a local config file (add to .gitignore).

---

## Part 1: Project Structure Setup

Create the following structure in your `lab08/` folder:

\`\`\`
lab08/
├── weather.py          # Main CLI application
├── weather_api.py      # API client class
├── favorites.py        # Favorites manager class
├── config.py           # Configuration (API key)
├── .gitignore          # Ignore config file
└── tests/
    └── test_weather.py # Unit tests
\`\`\`

### Step 1: Create .gitignore

Create `lab08/.gitignore`:

\`\`\`gitignore
# API key configuration
config.py

# Python
__pycache__/
*.pyc
.pytest_cache/

# Weather data cache
weather_cache.json
favorites.json
\`\`\`

### Step 2: Create config template

Create `lab08/config.example.py` (this WILL be committed):

\`\`\`python
"""
Configuration template for Weather CLI.

To use:
1. Copy this file to config.py
2. Replace YOUR_API_KEY_HERE with your actual WeatherAPI.com key
3. Never commit config.py to GitHub (it's in .gitignore)
"""

WEATHER_API_KEY = "YOUR_API_KEY_HERE"
WEATHER_API_BASE_URL = "http://api.weatherapi.com/v1"
\`\`\`

### Step 3: Create your actual config file

\`\`\`bash
# Copy the template
cp lab08/config.example.py lab08/config.py

# Edit config.py and add your real API key
# This file is in .gitignore and won't be committed
\`\`\`

---

## Part 2: API Client Class

Create `lab08/weather_api.py` with the WeatherAPI class for fetching weather data. This class should:
- Initialize with an API key
- Have `get_current_weather(location)` method
- Have `get_forecast(location, days=3)` method
- Handle all requests.exceptions gracefully
- Return None on errors

You'll also need helper functions:
- `format_current_weather(data)` - formats current weather for display
- `format_forecast(data)` - formats 3-day forecast for display

---

## Part 3: Favorites Manager Class

Create `lab08/favorites.py` with the FavoritesManager class for managing favorite locations. This class should:
- Load favorites from JSON file on initialization
- Save favorites to JSON file
- `add(name, location)` - add a favorite (return False if exists)
- `remove(name)` - remove a favorite (return False if not found)
- `list_all()` - return all favorites
- `get_location(name)` - get location string for a favorite name
- Case-insensitive lookups

---

## Part 4: Main CLI Application

Create `lab08/weather.py` with the main CLI using argparse. Your CLI should support these commands:

\`\`\`bash
# Current weather
python weather.py current <location>

# Forecast (1-3 days)
python weather.py forecast <location> [--days 1-3]

# Manage favorites
python weather.py favorites add <name> <location>
python weather.py favorites list
python weather.py favorites remove <name>

# Use favorites in commands
python weather.py current home     # if 'home' is a favorite
\`\`\`

**Requirements:**
- Use argparse with subparsers
- Implement command handler functions
- Support favorite names as location arguments
- Provide helpful --help messages

---

## Part 5: Testing

Create `lab08/tests/test_weather.py` with comprehensive tests for the FavoritesManager class:
- Test adding favorites
- Test adding duplicates (should return False)
- Test removing favorites
- Test removing non-existent favorites
- Test listing all favorites
- Test get_location by name
- Test case-insensitive lookups
- Test persistence across manager instances
- Test loading corrupted JSON file
- Test loading non-existent file

**Use pytest fixtures** for temp file management.

---

## Usage Examples

Test your CLI application with these commands:

\`\`\`bash
# Get current weather
python lab08/weather.py current London
python lab08/weather.py current "New York"
python lab08/weather.py current "Cincinnati, OH"

# Get forecast
python lab08/weather.py forecast London
python lab08/weather.py forecast "Paris" --days 2

# Add favorites
python lab08/weather.py favorites add home "Cincinnati, OH"
python lab08/weather.py favorites add work "Columbus, OH"

# List favorites
python lab08/weather.py favorites list

# Use favorite in commands
python lab08/weather.py current home
python lab08/weather.py forecast home

# Remove favorite
python lab08/weather.py favorites remove work

# Help
python lab08/weather.py --help
python lab08/weather.py current --help
\`\`\`

---

## Expected Output

### Current Weather
\`\`\`
==================================================
Current Weather for London, United Kingdom
==================================================
Condition: Partly cloudy
Temperature: 54.0°F (12.0°C)
Feels Like: 52.0°F (11.0°C)
Humidity: 76%
Wind: 8.0 mph W
Last Updated: 2025-01-15 14:30
==================================================
\`\`\`

---

## Expected Repository Structure

Your repository should now contain all 8 Python labs:

```
is4010-labs-yourname/
├── lab01/                    # Development toolkit setup
├── lab02/                    # AI-assisted development
├── lab03/                    # Python basics + testing
├── lab04/                    # Data structures
├── lab05/                    # Functions and error handling
├── lab06/                    # Object-oriented programming
├── lab07/                    # Data and APIs
└── lab08/                    # Python CLI application ✓
    ├── weather.py
    ├── weather_api.py
    ├── favorites.py
    ├── config.example.py
    ├── .gitignore
    └── tests/
        └── test_weather.py
```

This organized structure demonstrates your progression through the Python track, culminating in a complete CLI application that integrates all previous concepts.

---

## 🚨 Troubleshooting

**Common issues?** See the [Common Troubleshooting Guide](../resources/TROUBLESHOOTING.md) for general Python, testing, and GitHub Actions problems.

**Lab 08-specific issues:**

### **Problem: "ModuleNotFoundError: No module named 'config'"**
- **Cause**: Haven't created config.py from template
- **Solution**:
  \`\`\`bash
  cp lab08/config.example.py lab08/config.py
  # Edit config.py and add your API key
  \`\`\`

### **Problem: "Invalid API key" error**
- **Cause**: API key not configured correctly
- **Solution**:
  - Make sure you signed up at WeatherAPI.com
  - Copy the exact API key from dashboard
  - Paste into config.py (replace YOUR_API_KEY_HERE with your actual key)
  - Check for extra spaces before/after the key

### **Problem: "403 Forbidden" from API**
- **Cause**: API key is invalid or account suspended
- **Solution**:
  - Verify API key is correct in config.py
  - Check your WeatherAPI.com account status
  - Free tier has limits - check if you exceeded them
  - Try generating a new API key

### **Problem: "argparse error: unrecognized arguments"**
- **Cause**: Incorrect command syntax
- **Solution**:
  - Location names with spaces need quotes: `"New York"`
  - Check command structure: `python weather.py <command> <args>`
  - Use `--help` to see correct syntax

### **Problem: "favorites.json: Permission denied"**
- **Cause**: File permissions or directory doesn't exist
- **Solution**:
  - Make sure you're running from repository root
  - Check lab08/ directory exists
  - On Linux/Mac, check permissions: `ls -la lab08/`

### **Problem: Tests fail with "No module named 'weather_api'"**
- **Cause**: Running tests from wrong directory
- **Solution**:
  - Run from repository root: `pytest lab08/tests/`
  - Or add lab08 to PYTHONPATH: `PYTHONPATH=lab08 pytest lab08/tests/`

### **Problem: "Connection timeout" when fetching weather**
- **Cause**: Network issues or firewall blocking requests
- **Solution**:
  - Check internet connection
  - Try from different network (home vs campus)
  - Some firewalls block weather APIs
  - Verify the API endpoint is correct

### **Problem: Favorites not persisting after restart**
- **Cause**: favorites.json not being saved or wrong location
- **Solution**:
  - Check if favorites.json exists in lab08/
  - Verify save() method is called after add/remove
  - Check for IOError messages when saving
  - Make sure lab08/ folder has write permissions

---

## 🤖 AI Assistance Strategy

This lab is perfect for AI-assisted development! Here's how to use AI tools effectively for building CLI applications:

### When to Use AI

1. **Designing CLI structure**: Ask AI to help design your argument parser and subcommand hierarchy
2. **Debugging argparse errors**: AI excels at explaining argparse syntax and fixing parser issues
3. **API integration patterns**: Get help structuring API clients and handling responses
4. **Test case development**: Generate comprehensive test cases for your CLI functions

### Example Prompts

1. **For argparse setup**:
   ```
   "I'm building a weather CLI with subcommands 'current', 'forecast', and 'favorites'. Show me how to set up argparse with subparsers for these commands."
   ```

2. **For API client design**:
   ```
   "I need to create a WeatherAPI client class in Python. It should have methods for get_current_weather() and get_forecast(). Include error handling for network failures."
   ```

3. **For JSON persistence**:
   ```
   "How do I create a FavoritesManager class that saves/loads favorites to a JSON file with proper error handling for FileNotFoundError?"
   ```

4. **For debugging CLI issues**:
   ```
   "My argparse subcommand isn't working. Here's my code: [paste code]. When I run 'python weather.py current London', I get: [paste error]. How do I fix it?"
   ```

5. **For testing strategies**:
   ```
   "I need pytest test cases for a FavoritesManager class that adds/removes/lists favorites stored in JSON. Include tests for edge cases like duplicate adds and missing favorites."
   ```

6. **For improving code quality**:
   ```
   "Review my weather CLI code for PEP 8 compliance and suggest improvements: [paste code]"
   ```

### Conversation Example: Debugging Argparse

**You**: "My weather CLI with argparse subcommands isn't recognizing the 'current' subcommand. Here's my code:

```python
parser = argparse.ArgumentParser()
parser.add_argument('current')
parser.add_argument('location')
```

When I run `python weather.py current London`, it fails. What's wrong?"

**AI**: "The issue is you're using `add_argument` instead of subparsers. Here's the correct approach:

```python
parser = argparse.ArgumentParser(description='Weather CLI')
subparsers = parser.add_subparsers(dest='command')

current_parser = subparsers.add_parser('current', help='Get current weather')
current_parser.add_argument('location', help='City name')
```

This creates a proper subcommand structure where 'current' is a subcommand and 'location' is its argument."

**You**: "Perfect! How do I add the 'forecast' subcommand with an optional --days flag?"

**AI**: "Add it to the subparsers:

```python
forecast_parser = subparsers.add_parser('forecast', help='Get weather forecast')
forecast_parser.add_argument('location', help='City name')
forecast_parser.add_argument('--days', type=int, default=3, help='Number of days (1-3)')
```

The `--days` flag is optional and defaults to 3."

### Recommended Tools

- **[ChatGPT](https://chat.openai.com/)** - Excellent for explaining argparse patterns and CLI design
- **[Claude](https://claude.ai/)** - Great for debugging complex argument parser setups
- **[Gemini](https://gemini.google.com/)** - Helpful for API integration and error handling patterns
- **[GitHub Copilot](https://github.com/features/copilot)** - In-editor assistance for writing test cases

### When to Debug Yourself

- Simple syntax errors (missing colons, parentheses)
- Typos in variable names
- Basic pytest assertion failures
- File path issues

**Pro tip**: Before asking AI for help, try running your code and carefully reading the error message. Python's error messages are usually very informative!

---

## Submission

### Step 1: Run Tests Locally

\`\`\`bash
# From repository root
pytest lab08/tests/ -v

# All tests should pass ✓
\`\`\`

### Step 2: Test CLI Functionality

\`\`\`bash
# Test all subcommands
python lab08/weather.py current London
python lab08/weather.py forecast "Paris"
python lab08/weather.py favorites add test "London"
python lab08/weather.py favorites list
python lab08/weather.py favorites remove test
\`\`\`

### Step 3: Commit and Push

**IMPORTANT**: Don't commit your config.py file (contains API key)!

\`\`\`bash
# Verify config.py is in .gitignore
cat lab08/.gitignore

# Add only the correct files
git add lab08/weather.py lab08/weather_api.py lab08/favorites.py
git add lab08/config.example.py lab08/.gitignore
git add lab08/tests/test_weather.py

# Verify you're NOT committing config.py
git status

# Commit
git commit -m "Complete Lab 08: Weather CLI Application"

# Push
git push origin main
\`\`\`

### Step 4: Verify CI/CD

1. Go to your repository on GitHub
2. Click **Actions** tab
3. Find **Lab 08** workflow
4. Verify it shows a **green checkmark ✓**

**Note**: GitHub Actions will use a mock API key for testing.

---

## Success Criteria

Your lab is complete when:
- [ ] All required files created (weather.py, weather_api.py, favorites.py, config.example.py)
- [ ] .gitignore properly excludes config.py
- [ ] All CLI commands work (current, forecast, favorites)
- [ ] Tests pass locally (\`pytest lab08/tests/\`)
- [ ] GitHub Actions shows green checkmark
- [ ] Code follows PEP 8 style guidelines
- [ ] Functions have NumPy-style docstrings
- [ ] No API key committed to GitHub

**Grading**:
- ✅ **10 points**: All tests pass in GitHub Actions
- ❌ **0 points**: Any tests failing in GitHub Actions

---

## Optional Challenges

Want to go further? Try these extensions:

1. **Add caching**: Cache API responses for 10 minutes to reduce API calls
2. **Add search**: Search for locations by partial name
3. **Add units flag**: `--units metric` or `--units imperial`
4. **Add alerts**: Display weather alerts if available
5. **Add colors**: Use `colorama` library for colored output

These are **not required** for full credit but are great practice!

---

## 📚 Additional Resources

- **argparse Tutorial**: https://docs.python.org/3/howto/argparse.html
- **WeatherAPI Docs**: https://www.weatherapi.com/docs/
- **requests Documentation**: https://requests.readthedocs.io/
- **CLI Best Practices**: https://clig.dev/

---

**Need Help?**
- Review Chapters 5-8 in the textbook
- Check the troubleshooting section above
- See [Common Troubleshooting Guide](../resources/TROUBLESHOOTING.md)
- Use AI assistants (Copilot, Gemini CLI, ChatGPT)
- Ask on the course discussion board
- Attend office hours
