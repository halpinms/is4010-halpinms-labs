# Lab 01: Development toolkit setup

**Due**: End of week (Sunday at 11:59 PM)
**Points**: 10 points
**Chapter**: Chapter 1 - The modern development toolkit

---

## Learning Objectives

By the end of this lab, you will be able to:

- Install and verify essential development tools: [Git](https://git-scm.com/), [Python](https://www.python.org/), [VS Code](https://code.visualstudio.com/), and the [Rust toolchain](https://www.rust-lang.org/)
- Navigate your filesystem using the [command line](https://en.wikipedia.org/wiki/Command-line_interface) with confidence
- Create your first [GitHub repository](https://docs.github.com/en/repositories) and understand the basics of [version control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
- Set up authentication between your local machine and GitHub using [Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- Fork the IS4010 labs template repository and complete your first commit
- Verify your development environment is ready for the entire semester

---

## Background

Professional software development requires a modern toolkit that enables you to write code efficiently, track changes systematically, and collaborate with others seamlessly. This lab establishes the foundation for all future work in IS4010 by setting up your development environment with industry-standard tools.

The four essential tools you'll install are:

1. **The command line**: A text-based interface for controlling your computer with precision and power
2. **Git**: The version control system used by over 94% of professional developers
3. **GitHub**: The world's largest platform for hosting code and building developer portfolios
4. **VS Code**: A modern, extensible code editor with AI integration capabilities

These tools aren't optional extras—they're the baseline that employers expect when you start your first software development role. By the end of this lab, you'll have the same professional development environment used at companies like Google, Microsoft, Amazon, and thousands of startups worldwide.

### Key Concepts

- **Command line**: Text-based interface for executing commands directly on your operating system
- **Version control**: System for tracking changes to files over time, enabling collaboration and safe experimentation
- **Repository (repo)**: A project folder tracked by Git, containing all files and their complete history
- **Commit**: A snapshot of your project at a specific point in time
- **Fork**: Creating your own copy of someone else's repository
- **SSH key**: A cryptographic authentication method that's more secure than passwords

### Real-World Applications

- **Git** is the universal version control system used in virtually every software company
- **GitHub** serves as both a collaboration platform and a portfolio for showcasing your work to employers
- **Command line proficiency** is required for server administration, DevOps, and professional development workflows
- **VS Code** is one of the most popular code editors, with extensive AI integration capabilities we'll use throughout the course

---

## Prerequisites

For this first lab, you need:

- [ ] A computer running **Windows 10+**, **macOS 10.14+**, or a recent **Linux distribution**
- [ ] Administrator access to install software
- [ ] A stable internet connection for downloading tools (~500 MB total)
- [ ] A personal email address (we recommend using your UC email for GitHub student benefits)
- [ ] Approximately **90-120 minutes** to complete all installation and setup steps

**Important for Windows users**: Follow the [Windows Terminal + Git Bash setup](../resources/SETUP_GUIDE.md#recommendations-for-windows-users) in the SETUP_GUIDE. This ensures consistency with macOS/Linux users and matches industry practices where most servers run Linux.

---

## Instructions

### Part 1: Install required tools (45-60 minutes)

Install all required development tools by following the comprehensive [IS4010 SETUP_GUIDE.md](../resources/SETUP_GUIDE.md).

Complete these sections in order:

1. **[Section 1: Visual Studio Code](../resources/SETUP_GUIDE.md#1-visual-studio-code-vs-code)** - Install VS Code and verify with `code --version`

2. **[Section 2: Git](../resources/SETUP_GUIDE.md#2-git)** - Install Git and verify with `git --version`
   - **Windows users**: Follow the [Windows Terminal + Git Bash recommendations](../resources/SETUP_GUIDE.md#recommendations-for-windows-users)

3. **[Section 3: GitHub Account & Student Benefits](../resources/SETUP_GUIDE.md#3-github-account--student-benefits)** - Create account and apply for [GitHub Student Developer Pack](https://education.github.com/pack)
   - **Note**: If you already have a GitHub account, you can skip account creation and just apply for student benefits

4. **[Section 4: Python](../resources/SETUP_GUIDE.md#4-python)** - Install Python 3.10+ and verify with `python --version` or `python3 --version`

5. **[Section 5: Rust](../resources/SETUP_GUIDE.md#5-rust)** - Install Rust toolchain and verify with `cargo --version`

6. **[Section 8: Recommended VS Code Extensions](../resources/SETUP_GUIDE.md#8-recommended-vs-code-extensions)** - Install Python, rust-analyzer, and other essential extensions

**Verification checkpoint**: After completing installations, verify all tools work:

```bash
# Check VS Code
code --version

# Check Git
git --version

# Check Python
python --version  # or python3 --version

# Check Rust
cargo --version
rustc --version
```

All commands should print version numbers without errors.

---

### Part 2: Configure Git identity (5 minutes)

Tell Git who you are so your commits are properly attributed.

**Note**: If you've already configured Git on your computer, you can verify with `git config --global --list` and skip to Part 3 if your name and email are correct.

```bash
# Set your name (use your real name)
git config --global user.name "Your Full Name"

# Set your email (use the same email as your GitHub account)
git config --global user.email "your-email@example.com"

# Verify configuration
git config --global --list
```

You should see your name and email in the output.

---

### Part 3: Set up GitHub authentication with Personal Access Token (10-15 minutes)

GitHub requires authentication when you push code. You'll create a Personal Access Token (PAT) that acts like a password specifically for Git operations.

#### Why Personal Access Tokens?

- **More secure** than using your GitHub password
- **Scoped permissions** - you control exactly what the token can access
- **Revocable** - you can delete the token without changing your password
- **Easier for beginners** than SSH key setup

#### Create Your Personal Access Token

**Note**: If you already have a GitHub account with an existing Personal Access Token that has `repo` scope, you can skip this section and use your existing token. Just make sure it's saved somewhere you can access it.

1. **Go to GitHub Settings**:
   - Click your profile photo (top-right) → **Settings**
   - Scroll down in left sidebar → **Developer settings**
   - Click **Personal access tokens** → **Tokens (classic)**

2. **Generate new token**:
   - Click **"Generate new token (classic)"**
   - GitHub may ask you to confirm your password

3. **Configure the token**:
   - **Note**: Enter a descriptive name like `IS4010 Course - Spring 2025`
   - **Expiration**: Select **Custom** and choose a date after the semester ends (May 2025), or select **No expiration**
   - **Select scopes**: Check the **`repo`** checkbox
     - This grants full control of private repositories
     - All sub-checkboxes under `repo` should auto-select

4. **Generate and save**:
   - Scroll to bottom and click **"Generate token"**
   - **CRITICAL**: Copy the token immediately!
   - You'll see something like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - **This is the only time you'll see it!**

#### Store Your Token Securely

Choose ONE of these methods:

**Option 1: Password Manager (Recommended)**
- Save in 1Password, LastPass, Bitwarden, etc.
- Label it: "GitHub PAT - IS4010 Course"

**Option 2: Secure Note**
- Create a note in a secure location (not a public file!)
- You'll need this token every time you push to GitHub

**⚠️ NEVER commit your token to a Git repository or share it publicly!**

#### How You'll Use Your Token

You'll use this token as your password when Git prompts you during `git push` (Part 7).

**Good news**: After the first successful push, Git will cache your credentials, so you won't need to paste the token every time. The exact caching behavior depends on your operating system:

- **macOS**: Credentials stored in Keychain (permanent)
- **Windows**: Credentials stored in Credential Manager (permanent)
- **Linux**: May need to configure credential helper (we'll do this if needed)

---

### Part 4: Fork and clone the labs repository (10-15 minutes)

You'll create your own copy of the IS4010 labs template where you'll complete all lab assignments.

#### Fork the Repository

1. Navigate to: `https://github.com/bgreenwell/is4010-course`
   (Your instructor will provide the exact URL in class)

2. Click the **Fork** button in the top-right corner

3. Configure your fork:
   - **Owner**: Your GitHub account
   - **Repository name**: `is4010-[your-username]-labs`
     (Example: `is4010-jsmith-labs`)
   - **Description**: "IS4010 Lab Assignments - Spring 2025"
   - **Visibility**: ✅ **Private** (REQUIRED - keep your work private per academic integrity policy)

4. Click **"Create fork"**

#### Add Instructor as Collaborator

Your instructor needs access to grade your work:

1. In your forked repository, go to **Settings** → **Collaborators**
2. Click **"Add people"**
3. Search for: `bgreenwell` (or the GitHub username your instructor provides)
4. Click **"Add bgreenwell to this repository"**
5. The instructor will receive an invitation email

#### Clone Your Fork Locally

Copy your repository to your computer:

```bash
# Navigate to where you want to store your course work
cd ~
mkdir is4010
cd is4010

# Clone YOUR fork using HTTPS (replace YOUR-USERNAME)
git clone https://github.com/YOUR-USERNAME/is4010-YOUR-USERNAME-labs.git

# Navigate into your repository
cd is4010-YOUR-USERNAME-labs

# Verify you're in the right place
pwd
ls -la
```

You should see folders: `module01/`, `lab02/`, `lab03/`, etc.

---

### Part 5: Set up Python virtual environment (10 minutes)

Virtual environments keep your project dependencies isolated and prevent conflicts.

```bash
# Make sure you're in your labs repository root
cd ~/is4010/is4010-YOUR-USERNAME-labs

# Create virtual environment
python -m venv venv
# Or on macOS/Linux:
python3 -m venv venv

# Activate virtual environment
# macOS/Linux:
source venv/bin/activate

# Windows (Git Bash):
source venv/Scripts/activate

# Your prompt should now show (venv) at the beginning
```

**Install required packages**:

```bash
# Make sure venv is activated (you should see "(venv)" in your prompt)
pip install -r requirements.txt

# Verify pytest is installed
pytest --version
# Should show: pytest 7.4.0 or higher
```

**Important**: You'll need to activate the virtual environment every time you open a new terminal:

```bash
cd ~/is4010/is4010-YOUR-USERNAME-labs

# macOS/Linux:
source venv/bin/activate

# Windows (Git Bash):
source venv/Scripts/activate
```

You'll know it's activated when you see `(venv)` at the start of your prompt.

---

### Part 6: Create your first Python program (10 minutes)

Let's verify everything works by creating a simple program.

#### Create hello.py

1. Open VS Code in your repository:
   ```bash
   code .
   ```

2. In VS Code, navigate to the `module01/` folder in the left sidebar

3. Create a new file: `hello.py`

4. Add this code:

```python
"""
Lab 01: Development Toolkit Setup
Author: Your Name
Date: January 2025

This program demonstrates that your Python environment is correctly configured.
"""


def main():
    """Print a greeting and verify Python installation."""
    print("Hello, IS4010!")
    print("My development environment is ready.")

    import sys
    print(f"\nPython version: {sys.version}")
    print(f"Python executable: {sys.executable}")


if __name__ == "__main__":
    main()
```

#### Run Your Program

**From VS Code**:
- Right-click anywhere in the editor → **"Run Python File in Terminal"**

**From Command Line**:
```bash
# Make sure you're in repository root and venv is activated
cd ~/is4010/is4010-YOUR-USERNAME-labs
source venv/bin/activate

# Run the program
python module01/hello.py
# Or on macOS/Linux:
python3 module01/hello.py
```

#### Expected Output

```
Hello, IS4010!
My development environment is ready.

Python version: 3.11.7 (main, Dec  4 2023, 18:10:11) [Clang 15.0.0 (clang-1500.1.0.2.5)]
Python executable: /Users/username/is4010/is4010-jsmith-labs/venv/bin/python
```

The exact version numbers will vary, but you should see Python 3.10+ and the path should include `venv/`.

---

### Part 7: Commit and push your work (10-15 minutes)

Now you'll use Git to save and upload your work to GitHub.

#### Stage Your Changes

```bash
# Check what changed
git status
# Should show: modified: module01/hello.py (or untracked file)

# Add your file to the staging area
git add module01/hello.py

# Verify it's staged
git status
# Should show "Changes to be committed" in green
```

#### Create Your First Commit

```bash
git commit -m "Complete Lab 01: Add hello.py program

- Created hello.py with environment verification
- Verified Python installation and virtual environment
- Tested development environment setup"
```

**Git commit message format tip**: First line is a summary (50 chars), then a blank line, then bullet points explaining what changed.

#### Push to GitHub

```bash
# Push your changes to GitHub
git push origin main

# Or if your default branch is named 'master':
git push origin master
```

**When prompted for credentials**:
- **Username**: Enter your GitHub username
- **Password**: Paste your Personal Access Token (NOT your GitHub password!)

Git will remember your credentials for future pushes (credential caching).

#### Verify on GitHub

1. Go to your repository: `https://github.com/YOUR-USERNAME/is4010-YOUR-USERNAME-labs`
2. Navigate to the `module01/` folder
3. Click on `hello.py` to view its contents
4. Click on the commit message to see your commit details
5. Verify the commit shows your name and the timestamp

---

## Expected Output

After completing all steps, you should have:

✅ **All tools installed and verified**:
- `code --version` works (VS Code)
- `git --version` shows 2.30.0+
- `python --version` or `python3 --version` shows 3.10+
- `cargo --version` and `rustc --version` both work

✅ **GitHub configured**:
- Account created with professional username
- Personal Access Token generated and securely stored
- Git identity configured (`git config --global --list` shows your name/email)

✅ **Repository ready**:
- Forked `is4010-course` to your account (private)
- Instructor added as collaborator
- Cloned to local machine at `~/is4010/is4010-YOUR-USERNAME-labs/`

✅ **Python environment ready**:
- Virtual environment created (`venv/` folder exists)
- Can activate venv and see `(venv)` in prompt
- `pytest --version` works inside venv

✅ **First commit complete**:
- `hello.py` created in `module01/` folder
- Program runs successfully and shows Python version
- Changes committed and pushed to GitHub
- Commit visible in GitHub web interface

### Sample Terminal Session

```bash
$ cd ~/is4010/is4010-jsmith-labs
$ source venv/bin/activate
(venv) $ python3 module01/hello.py
Hello, IS4010!
My development environment is ready.

Python version: 3.11.7 (main, Dec  4 2023, 18:10:11)
Python executable: /Users/jsmith/is4010/is4010-jsmith-labs/venv/bin/python
(venv) $ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

---

## Troubleshooting

### Command Not Found Errors

**Problem**: `git: command not found`, `python: command not found`, etc.

**Solutions**:
- **Restart your terminal** after installing new software
- **Windows**: Make sure you're using Git Bash (not Command Prompt or PowerShell)
- **macOS Git**: Run `xcode-select --install` to install Command Line Tools
- **Python**: Try `python3` instead of `python`, or vice versa
- **Check PATH**: Run `echo $PATH` to verify installation directories are included
- **Detailed platform-specific help**: See [SETUP_GUIDE.md sections 1-5](../resources/SETUP_GUIDE.md)

### Authentication Failed When Pushing

**Problem**: `Authentication failed` or `invalid credentials` when pushing to GitHub

**Solutions**:
- **Make sure you're using your Personal Access Token** as the password, NOT your GitHub password
- Verify your PAT hasn't expired: Check [GitHub Settings → Personal access tokens](https://github.com/settings/tokens)
- Ensure PAT has `repo` scope selected when you created it
- Copy the token carefully (no extra spaces or characters)
- If you lost your token, generate a new one (you can't view old tokens)
- Clear stored credentials and try again:
  ```bash
  # macOS
  git credential-osxkeychain erase
  # Then re-enter credentials on next push
  ```

### Virtual Environment Not Activating

**Problem**: `(venv)` doesn't appear in terminal prompt after running activate command

**Solutions**:
- **macOS/Linux/Git Bash**: Use `source venv/bin/activate` (not just `activate`)
- **Windows Command Prompt**: Use `venv\Scripts\activate` (backslashes)
- **Permission denied**: Run `chmod +x venv/bin/activate`
- **Wrong directory**: Make sure you're in repository root (`pwd` should show `is4010-YOUR-USERNAME-labs`)
- **Recreate venv**: Delete `venv/` folder and run `python3 -m venv venv` again

### Git Push Rejected

**Problem**: `error: failed to push some refs to...`

**Solutions**:
- Make sure you **forked** the repository (don't push to the original template)
- Verify remote URL points to YOUR fork: `git remote -v` should show YOUR username
- Fix remote URL if wrong:
  ```bash
  git remote set-url origin git@github.com:YOUR-USERNAME/is4010-YOUR-USERNAME-labs.git
  ```
- Pull before pushing: `git pull origin main` then try `git push origin main`
- Check you added instructor as collaborator in GitHub settings

### pytest Command Not Found

**Problem**: `pytest: command not found` even after pip install

**Solutions**:
- Make sure virtual environment is activated (see `(venv)` in prompt)
- Verify you ran `pip install -r requirements.txt` **after** activating venv
- Try `python -m pytest` instead of just `pytest`
- Check installed packages: `pip list | grep pytest`
- Recreate virtual environment if needed

### VS Code Can't Find Python Interpreter

**Problem**: VS Code shows "No Python interpreter" or Python extension errors

**Solutions**:
- Click the Python version indicator in bottom-left of VS Code
- Select your virtual environment: `./venv/bin/python`
- Reload VS Code window: `Ctrl+Shift+P` → "Developer: Reload Window"
- Verify venv is activated in VS Code's integrated terminal
- Install Python extension: Search "Python" in Extensions (`Ctrl+Shift+X`)

### Repository is Public Instead of Private

**Problem**: Your repository is visible to everyone on GitHub

**Solutions**:
- Go to repository **Settings** → **Danger Zone** → **Change visibility**
- Select **"Make private"** → Confirm
- Verify instructor is still added as collaborator
- **Academic integrity**: Repository must be private to protect your work

For additional troubleshooting help, see the [SETUP_GUIDE.md](../resources/SETUP_GUIDE.md) or ask in the course Teams channel.

---

## AI Assistance Strategy

This lab involves installation and configuration, where AI tools excel at explaining concepts and troubleshooting errors. Here's how to use AI effectively:

### Example Prompts for Common Tasks

**Understanding commands**:
> "Explain what this Git command does: `git config --global user.name 'John Smith'`"

**Debugging errors**:
> "I'm getting 'Permission denied (publickey)' when I run `git push`. What does this mean and how do I fix it?"

**Installation verification**:
> "What's the difference between `python` and `python3` commands? Which should I use?"

**Personal Access Token concepts**:
> "What is a GitHub Personal Access Token and why is it more secure than using my password?"

**Git workflow**:
> "Walk me through the process of forking a GitHub repository and cloning it to my local machine."

**Command line navigation**:
> "What's the difference between `cd ..` and `cd ~`? When would I use each?"

**Virtual environments**:
> "Why do I need to activate a Python virtual environment? What does it actually do?"

**Troubleshooting platforms**:
> "I'm on Windows and `python3` doesn't work but `python` does. Is this normal?"

### Real AI Conversation Example

**You**: When I try `git push`, it asks for my password. Should I use my GitHub account password?

**AI**: No! GitHub no longer accepts account passwords for Git operations. You need to use your **Personal Access Token** instead.

Here's what to do:

1. **Use your PAT as the password**: When Git prompts for a password, paste your Personal Access Token (the one you saved in Part 3)
2. **Don't type your GitHub password**: That won't work for Git operations

Example of what you'll see:
```bash
$ git push origin main
Username for 'https://github.com': your-username
Password for 'https://your-username@github.com': [paste your PAT here]
```

**Pro tip**: Git will remember your credentials after the first successful push (credential caching), so you won't have to paste the token every time.

**If you lost your PAT**: Generate a new one at GitHub Settings → Developer settings → Personal access tokens (classic)

---

**You**: I got an error: "Authentication failed for 'https://github.com/myuser/myrepo.git'"

**AI**: This usually means one of these issues:

1. **You used your GitHub password instead of your PAT**: Remember, you need to paste your Personal Access Token, not your account password
2. **Your PAT expired**: Check if it's still valid at [github.com/settings/tokens](https://github.com/settings/tokens)
3. **Your PAT doesn't have the right permissions**: Make sure you selected the `repo` scope when creating it

**To fix it**:
```bash
# Try pushing again and carefully paste your PAT when prompted
git push origin main

# If it still fails, generate a new PAT:
# 1. Go to: GitHub Settings → Developer settings → Personal access tokens
# 2. Click "Generate new token (classic)"
# 3. Check the "repo" scope
# 4. Copy the new token and try pushing again
```

---

### When to Use AI vs. Official Documentation

**Use AI for**:
- Explaining error messages in plain English
- Understanding what commands do before running them
- Comparing different approaches (SSH vs HTTPS, `python` vs `python3`)
- Troubleshooting platform-specific issues (Windows vs macOS vs Linux)
- Step-by-step walkthroughs of processes

**Use official docs for**:
- Authoritative installation instructions (always follow official guides)
- Complete command reference and all available options
- Security best practices and recommendations
- Latest version compatibility and system requirements

**Best practice**: Use AI to understand concepts and troubleshoot, then verify critical steps (especially security-related) with official documentation.

---

## Submission

Follow these steps to submit Lab 01:

### 1. Verify Local Completion

Run this verification script to check all requirements:

```bash
# Navigate to repository
cd ~/is4010/is4010-YOUR-USERNAME-labs

# Verify all tools installed
echo "=== Tool Verification ==="
code --version && echo "✓ VS Code installed"
git --version && echo "✓ Git installed"

# Check Python (try python3 first, fallback to python)
if command -v python3 &> /dev/null; then
    python3 --version && echo "✓ Python installed"
    PYTHON_CMD="python3"
else
    python --version && echo "✓ Python installed"
    PYTHON_CMD="python"
fi

cargo --version && echo "✓ Rust installed"

# Verify Python environment
echo -e "\n=== Python Environment ==="
# Activate venv (use correct path for your OS)
if [ -d "venv/bin" ]; then
    source venv/bin/activate  # macOS/Linux
else
    source venv/Scripts/activate  # Windows Git Bash
fi
pytest --version && echo "✓ pytest installed"

# Verify hello.py exists and runs
echo -e "\n=== Lab 01 Program ==="
$PYTHON_CMD module01/hello.py
```

If all checks pass with checkmarks (✓), you're ready to submit!

### 2. Final Commit and Push

```bash
# Check status
git status

# If you made any changes, stage and commit
git add module01/
git commit -m "Final submission: Lab 01"

# Push to GitHub
git push origin main
```

### 3. Verify on GitHub

1. Go to: `https://github.com/YOUR-USERNAME/is4010-YOUR-USERNAME-labs`
2. Verify the repository is **private** (🔒 lock icon)
3. Verify **bgreenwell** is listed under Settings → Collaborators
4. Navigate to `module01/` folder
5. Click on `hello.py` and verify contents are correct
6. Check recent commits show your work

### 4. Submit on Canvas

1. Go to **Canvas** → **IS4010** → **Assignments** → **Lab 01**
2. Submit the **URL to your repository**:
   ```
   https://github.com/YOUR-USERNAME/is4010-YOUR-USERNAME-labs
   ```
3. In the comment box, add:
   ```
   Latest commit: [paste output of: git log -1 --oneline]
   All tools verified: ✓
   ```

**Note**: There is no automated GitHub Actions workflow for Lab 01 since it's primarily setup and configuration. Starting with Lab 03, you'll verify that tests pass in GitHub Actions before submitting.

---

## Success Criteria

Use this checklist to verify you've completed everything:

### Installation & Configuration
- [ ] **VS Code installed**: `code --version` works
- [ ] **Git installed**: `git --version` shows 2.30.0+
- [ ] **Git identity configured**: `git config --global --list` shows your name and email
- [ ] **Python installed**: `python --version` or `python3 --version` shows 3.10+
- [ ] **Rust installed**: Both `rustc --version` and `cargo --version` work
- [ ] **VS Code extensions**: Python, rust-analyzer, and recommended extensions installed

### GitHub & Repository
- [ ] **GitHub account created**: Professional username, email verified
- [ ] **Personal Access Token generated**: Saved securely with `repo` scope
- [ ] **Repository forked**: Private fork of `is4010-course` exists under your account
- [ ] **Instructor added**: `bgreenwell` appears as collaborator in repo settings
- [ ] **Repository cloned**: Local copy at `~/is4010/is4010-YOUR-USERNAME-labs/`

### Python Environment
- [ ] **Virtual environment created**: `venv/` folder exists in repository root
- [ ] **Virtual environment works**: `source venv/bin/activate` shows `(venv)` in prompt
- [ ] **Dependencies installed**: `pytest --version` works inside activated venv

### Lab Deliverable
- [ ] **hello.py created**: File exists at `module01/hello.py`
- [ ] **hello.py runs successfully**: Outputs greeting and Python version info
- [ ] **Changes committed**: `git log` shows your commit with descriptive message
- [ ] **Changes pushed**: `hello.py` visible on GitHub in your repository
- [ ] **Canvas submission**: Repository URL submitted on Canvas

### Grading

**This lab is graded as complete/incomplete (10 points total):**

- ✅ **10 points**: All tools installed and verified, repository properly configured (private, instructor added), `hello.py` committed and pushed successfully
- ❌ **0 points**: Missing required tools, repository misconfigured, or `hello.py` not pushed

**Important**: Your instructor will manually verify your repository setup and hello.py file. Make sure your repository is **private** with **bgreenwell added as a collaborator** so the instructor can access it for grading.

---

## Looking Ahead

Congratulations! You now have a professional development environment. In **Lab 02**, you'll learn:
- How to use AI coding assistants strategically
- Setting up context files (like `AGENTS.md`) for better AI assistance
- Crafting effective prompts for different coding tasks
- Understanding when AI helps vs. when to think independently

The tools you set up today are foundational. Every professional developer uses Git, GitHub, a modern editor, and the command line daily. You've just built the same toolkit used by developers at major tech companies.

**Pro tip**: Create an alias to quickly activate your environment. Add this to `~/.bashrc` or `~/.zshrc`:

```bash
# macOS/Linux:
alias is4010='cd ~/is4010/is4010-YOUR-USERNAME-labs && source venv/bin/activate'

# Windows (Git Bash) - add to ~/.bashrc:
alias is4010='cd ~/is4010/is4010-YOUR-USERNAME-labs && source venv/Scripts/activate'
```

Then just type `is4010` in any terminal to jump to your repository and activate the virtual environment!

**Getting help**: If you encounter issues that the troubleshooting section doesn't solve:
1. Check the comprehensive [SETUP_GUIDE.md](../resources/SETUP_GUIDE.md)
2. Search for the error message (copy exact text into search)
3. Ask an AI assistant for explanation and solutions
4. Post in the course Teams channel with details about your platform and the error
5. Attend office hours for hands-on help

Don't struggle alone - getting your environment working is critical for the entire course!
