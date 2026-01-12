# Week 04: Data structures

**Due**: End of week (Sunday at 11:59 PM)
**Points**: 10

## Overview

This week explores Python's powerful data structures: lists, dictionaries, sets, and tuples. You'll learn to manipulate data effectively and apply these skills to real-world problems.

## Materials

- 📋 **Lab instructions**: [lab04.md](./lab04.md)
- 📓 **Interactive exercises**: [notebook.ipynb](./notebook.ipynb)
- 🧪 **Automated tests**: `tests/test_lab04.py` (provided)

## Quick start

1. **Read the lab instructions**: [lab04.md](./lab04.md)
2. **Work through the notebook**: Open `notebook.ipynb` in Jupyter or VS Code
3. **Write your solution**: Create `lab04.py` with your code
4. **Run tests locally**: Verify your solution before pushing

```bash
# From week04 folder
cd week04/

# Run tests
pytest tests/ -v

# Expected output:
# tests/test_lab04.py::test_find_common_elements_with_common_items PASSED
# tests/test_lab04.py::test_find_user_by_name_existing PASSED
# ======================== all tests passed ========================
```

5. **Commit and push**: Submit your work to GitHub

```bash
git add week04/
git commit -m "Complete Week 04 lab"
git push origin main
```

6. **Verify CI/CD**: Check GitHub Actions shows a green checkmark ✅

## Testing locally

All labs include automated tests to verify your solution before submission.

### Running tests

```bash
# From repository root
pytest week04/tests/ -v

# From week04 folder
cd week04/
pytest tests/ -v
```

### Understanding test output

- **PASSED** ✅ - Test succeeded, your code is correct
- **FAILED** ❌ - Test failed, check the error message
- **ERROR** ⚠️ - Syntax error or import problem in your code

### Common issues

**ImportError: No module named 'lab04'**
- Make sure `lab04.py` exists in the `week04/` folder
- Check your file name matches exactly: `lab04.py` (not `Lab04.py` or `lab4.py`)

**All tests fail**
- Read the test file: `tests/test_lab04.py`
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
│       ├── week03.yml        # Week 3 CI/CD
│       └── week04.yml        # Week 4 CI/CD (if provided)
├── week01/
│   ├── README.md
│   └── lab01.md
├── week02/
│   ├── README.md
│   ├── lab02.md
│   ├── lab02.py
│   └── lab02_prompts.md
├── week03/
│   ├── README.md
│   ├── lab03.md
│   ├── notebook.ipynb
│   ├── lab03.py
│   └── tests/
│       └── test_lab03.py
├── week04/
│   ├── README.md             # This file
│   ├── lab04.md              # Lab instructions
│   ├── notebook.ipynb        # Interactive exercises
│   ├── lab04.py              # Your solution ✅
│   └── tests/
│       └── test_lab04.py     # Automated tests (provided)
└── README.md
```

## Need help?

1. Read [lab04.md](./lab04.md) thoroughly
2. Check the [troubleshooting guide](../resources/TROUBLESHOOTING.md)
3. Review test expectations in `tests/test_lab04.py`
4. Ask on Microsoft Teams discussion board
5. Attend office hours
