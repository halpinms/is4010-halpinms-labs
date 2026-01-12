# Week 09: Rust basics

**Due**: End of week (Sunday at 11:59 PM)
**Points**: 10

## Overview

Welcome to Rust! This week introduces Rust fundamentals: installing the toolchain, creating Cargo projects, and writing basic Rust code with variables, functions, and tests.

## Materials

- 📋 **Lab instructions**: [lab09.md](./lab09.md)
- 📓 **Interactive exercises**: [notebook.ipynb](./notebook.ipynb) (if available)

## Quick start

1. **Read the lab instructions**: [lab09.md](./lab09.md)
2. **Install Rust toolchain**: Follow setup instructions in lab
3. **Work through exercises**: Practice Rust syntax
4. **Write your solution**: Edit `src/main.rs` or `src/lib.rs`
5. **Run tests locally**: Verify before pushing

```bash
cd week09/

# Build your code
cargo build

# Run tests
cargo test

# Check formatting
cargo fmt --check

# Run linter
cargo clippy
```

6. **Commit and push**: Submit your work to GitHub

```bash
git add week09/
git commit -m "Complete Week 09 lab"
git push origin main
```

7. **Verify CI/CD**: GitHub Actions checks build, tests, fmt, and clippy

## Expected repository structure

After completing this lab:

```
is4010-[your-username]-course/
├── week01-week08/       # Python weeks
├── week09/
│   ├── README.md         # This file
│   ├── lab09.md          # Lab instructions
│   ├── notebook.ipynb    # Rust exercises (if available)
│   ├── Cargo.toml        # Rust project config
│   └── src/
│       └── main.rs       # Your Rust solution ✅
└── README.md
```

## Need help?

1. Read [lab09.md](./lab09.md) thoroughly
2. Check Rust compiler error messages (they're excellent!)
3. Review [The Rust Book](https://doc.rust-lang.org/book/)
4. Check the [setup guide](../resources/SETUP_GUIDE.md) for Rust installation
5. Ask on Microsoft Teams discussion board
6. Attend office hours
