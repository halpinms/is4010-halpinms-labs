# Week 03: Python basics and automated testing

**Due**: End of week (Sunday at 11:59 PM)
**Points**: 10

## Overview

This week introduces Python fundamentals and automated testing with pytest. You'll write basic Python functions and verify them with unit tests.

## Materials

- 📋 **Lab instructions**: [lab03.md](./lab03.md)
- 📓 **Interactive exercises**: [notebook.ipynb](./notebook.ipynb)
- 🧪 **Automated tests**: `tests/test_lab03.py` (provided)

## Quick start

1. **Read the lab instructions**: [lab03.md](./lab03.md)
2. **Work through the notebook**: Open `notebook.ipynb` in Jupyter or VS Code
3. **Write your solution**: Create `lab03.py` with your code
4. **Run tests locally**: Verify your solution before pushing

```bash
# From week03 folder
cd week03/

# Run tests
pytest tests/ -v

# Expected output:
# tests/test_lab03.py::test_generate_mad_lib PASSED
# tests/test_lab03.py::test_guessing_game_correct_guess PASSED
# ======================== 2 passed in 0.05s ========================
```

5. **Commit and push**: Submit your work to GitHub

```bash
git add week03/
git commit -m "Complete Week 03 lab"
git push origin main
```

6. **Verify CI/CD**: Check GitHub Actions shows a green checkmark ✅

## Testing locally

All labs include automated tests to verify your solution before submission.

### Running tests

```bash
# From repository root
pytest week03/tests/ -v

# From week03 folder
cd week03/
pytest tests/ -v
```

### Understanding test output

- **PASSED** ✅ - Test succeeded, your code is correct
- **FAILED** ❌ - Test failed, check the error message
- **ERROR** ⚠️ - Syntax error or import problem in your code

### Common issues

**ImportError: No module named 'lab03'**
- Make sure `lab03.py` exists in the `week03/` folder
- Check your file name matches exactly: `lab03.py` (not `Lab03.py` or `lab3.py`)

**All tests fail**
- Read the test file: `tests/test_lab03.py`
- Check function names match exactly what tests expect
- Verify function signatures (parameters) are correct

**Tests pass locally but fail in GitHub Actions**
- Check you committed all required files
- Verify your virtual environment didn't hide missing dependencies
- Review the GitHub Actions log for specific errors

## Expected repository structure

After completing this lab, your repository should look like this:

```
is4010-[your-username]-course/
├── .github/
│   └── workflows/
│       └── week03.yml        # GitHub Actions CI/CD (if provided)
├── week01/
│   ├── README.md
│   └── lab01.md
├── week02/
│   ├── README.md
│   ├── lab02.md
│   ├── lab02.py              # Your week 02 solution
│   └── lab02_prompts.md
├── week03/
│   ├── README.md             # This file
│   ├── lab03.md              # Lab instructions
│   ├── notebook.ipynb        # Interactive exercises
│   ├── lab03.py              # Your solution ✅
│   └── tests/
│       └── test_lab03.py     # Automated tests (provided)
└── README.md
```

## Need help?

1. Read [lab03.md](./lab03.md) thoroughly
2. Check the [troubleshooting guide](../resources/TROUBLESHOOTING.md)
3. Review test expectations in `tests/test_lab03.py`
4. Ask on Microsoft Teams discussion board
5. Attend office hours
