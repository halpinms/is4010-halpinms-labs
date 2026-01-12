# Lab 14: Rust CLI Application

**Due**: End of week (Sunday at 11:59 PM)
**Points**: 10 points
**Chapter**: Chapter 14 - Rust CLI Applications

---

## Objective

Build a complete command-line password generator application that integrates all the Rust concepts you've learned: ownership, modules, traits, generics, iterators, and error handling. This lab demonstrates how to create a professional CLI tool using `clap` with multiple subcommands.

**What you'll learn:**
- Building CLI applications with clap
- Secure random number generation in Rust
- String manipulation and validation
- File I/O for configuration and history
- Combining iterators, traits, and error handling
- Professional Rust project structure

---

## Background

Password security is critical in modern software development. Strong, random passwords are essential for protecting user accounts and sensitive data. You'll build a CLI tool that generates secure passwords with customizable options and validates password strength.

**Real-world applications:**
- Password managers (1Password, Bitwarden, LastPass)
- DevOps tools (generate API keys, tokens)
- Security auditing tools
- System administration utilities

**Key concepts applied:**
- **Ownership** (Lab 10): String ownership and borrowing
- **Modules** (Lab 11): Organize generator, validator, and CLI modules
- **Traits** (Lab 12): Custom traits for password generation strategies
- **Iterators** (Lab 13): Filter and map for password generation
- **Error Handling** (Lab 13): Result types for validation
- **clap**: Professional CLI argument parsing

**Documentation & Resources:**
- [clap documentation](https://docs.rs/clap/latest/clap/)
- [clap examples](https://github.com/clap-rs/clap/tree/master/examples) (see derive examples for Parser/Subcommand patterns)
- [clap::Parser trait](https://docs.rs/clap/latest/clap/trait.Parser.html)
- [clap::Subcommand derive](https://docs.rs/clap/latest/clap/trait.Subcommand.html)
- [rand crate](https://docs.rs/rand/latest/rand/)
- [rand::thread_rng()](https://docs.rs/rand/latest/rand/fn.thread_rng.html)
- [rand::Rng trait](https://docs.rs/rand/latest/rand/trait.Rng.html)
- [String methods](https://doc.rust-lang.org/std/string/struct.String.html)
- [chars() iterator](https://doc.rust-lang.org/std/primitive.str.html#method.chars)
- [collect()](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)
- [cargo test](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [cargo clippy](https://github.com/rust-lang/rust-clippy)
- [Integration testing](https://doc.rust-lang.org/book/ch11-03-test-organization.html#integration-tests)
- [OWASP Password Guidelines](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#password-complexity)

---

## Prerequisites

Before starting this lab, ensure you have:
- [ ] Completed Labs 09-13 (Rust basics through idiomatic Rust)
- [ ] Rust toolchain installed (rustc, cargo)
- [ ] Familiarity with cargo test, cargo fmt, cargo clippy

---

## Part 1: Project Setup

Create a new Rust project in your week14/ folder:

```bash
cd week14
cargo new passgen
cd passgen
```

### Add Dependencies

Edit `week14/passgen/Cargo.toml`:

```toml
[package]
name = "passgen"
version = "0.1.0"
edition = "2021"

[dependencies]
clap = { version = "4.5", features = ["derive"] }
rand = "0.8"
```

### Project Structure

Your final structure should look like:

```
week14/
└── passgen/
    ├── Cargo.toml
    ├── src/
    │   ├── main.rs           # CLI application entry point
    │   ├── generator.rs      # Password generation logic
    │   ├── validator.rs      # Password strength validation
    │   └── lib.rs            # Library exports
    └── tests/
        └── integration_test.rs
```

---

## Part 2: Password Generator Module

Create `week14/passgen/src/generator.rs` with password generation functionality.

### Requirements

Implement the following functions:

**1. `generate_random(length: usize, use_symbols: bool) -> String`**
- Generate a random password with specified length
- Include uppercase, lowercase, and digits by default
- Optionally include symbols (!@#$%^&*) if `use_symbols` is true
- Use the `rand` crate for secure randomness

**2. `generate_passphrase(word_count: usize, separator: char) -> String`**
- Generate a passphrase from a predefined word list
- Join words with the specified separator (e.g., `-` or `_`)
- Example: "correct-horse-battery-staple"

**3. `generate_pin(length: usize) -> String`**
- Generate a numeric PIN code
- Only digits 0-9

### Example Implementation Pattern

```rust
use rand::Rng;

const LOWERCASE: &str = "abcdefghijklmnopqrstuvwxyz";
const UPPERCASE: &str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const DIGITS: &str = "0123456789";
const SYMBOLS: &str = "!@#$%^&*";

pub fn generate_random(length: usize, use_symbols: bool) -> String {
    let mut rng = rand::thread_rng();
    let mut charset = String::new();
    charset.push_str(LOWERCASE);
    charset.push_str(UPPERCASE);
    charset.push_str(DIGITS);
    
    if use_symbols {
        charset.push_str(SYMBOLS);
    }
    
    let chars: Vec<char> = charset.chars().collect();
    
    // Use iterators to generate password
    (0..length)
        .map(|_| {
            let idx = rng.gen_range(0..chars.len());
            chars[idx]
        })
        .collect()
}
```

---

## Part 3: Password Validator Module

Create `week14/passgen/src/validator.rs` with password strength validation.

### Password Strength Enum

```rust
#[derive(Debug, PartialEq, Clone)]
pub enum PasswordStrength {
    Weak,
    Medium,
    Strong,
    VeryStrong,
}
```

### Requirements

Implement the following functions:

**1. `validate_strength(password: &str) -> PasswordStrength`**
- Analyze password and return strength rating
- Criteria:
  - **Weak**: < 8 characters or only lowercase
  - **Medium**: 8+ characters, mixed case
  - **Strong**: 8+ characters, mixed case + digits
  - **VeryStrong**: 12+ characters, mixed case + digits + symbols

**2. `check_common_patterns(password: &str) -> bool`**
- Return true if password contains common patterns
- Check for: sequential numbers (123, 456), repeated characters (aaa, 111), keyboard patterns (qwerty, asdf)

**3. `calculate_entropy(password: &str) -> f64`**
- Calculate password entropy in bits
- Formula: length * log2(charset_size)
- Return entropy as floating point

### Example Implementation Pattern

```rust
pub fn validate_strength(password: &str) -> PasswordStrength {
    let len = password.len();
    let has_lower = password.chars().any(|c| c.is_lowercase());
    let has_upper = password.chars().any(|c| c.is_uppercase());
    let has_digit = password.chars().any(|c| c.is_numeric());
    let has_symbol = password.chars().any(|c| !c.is_alphanumeric());
    
    match (len, has_lower, has_upper, has_digit, has_symbol) {
        (l, _, _, _, true) if l >= 12 => PasswordStrength::VeryStrong,
        (l, true, true, true, _) if l >= 8 => PasswordStrength::Strong,
        (l, true, true, _, _) if l >= 8 => PasswordStrength::Medium,
        _ => PasswordStrength::Weak,
    }
}
```

---

## Part 4: Library Module

Create `week14/passgen/src/lib.rs` to export your modules:

```rust
pub mod generator;
pub mod validator;

// Re-export commonly used items
pub use generator::{generate_random, generate_passphrase, generate_pin};
pub use validator::{validate_strength, PasswordStrength};
```

---

## Part 5: CLI Application

Create `week14/passgen/src/main.rs` with the main CLI using clap.

### CLI Commands

Your CLI should support these commands:

```bash
# Generate random password
cargo run -- random --length 16 --symbols

# Generate passphrase
cargo run -- passphrase --words 4 --separator -

# Generate PIN
cargo run -- pin --length 6

# Validate password strength
cargo run -- validate "MyP@ssw0rd123"

# Display help
cargo run -- --help
```

### Implementation Pattern

```rust
use clap::{Parser, Subcommand};
use passgen::{generate_random, generate_passphrase, generate_pin, validate_strength};

#[derive(Parser)]
#[command(name = "passgen")]
#[command(about = "A secure password generator and validator", long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Generate a random password
    Random {
        /// Password length
        #[arg(short, long, default_value_t = 16)]
        length: usize,
        
        /// Include symbols
        #[arg(short, long)]
        symbols: bool,
    },
    
    /// Generate a passphrase
    Passphrase {
        /// Number of words
        #[arg(short, long, default_value_t = 4)]
        words: usize,
        
        /// Word separator
        #[arg(short, long, default_value = "-")]
        separator: char,
    },
    
    /// Generate a numeric PIN
    Pin {
        /// PIN length
        #[arg(short, long, default_value_t = 4)]
        length: usize,
    },
    
    /// Validate password strength
    Validate {
        /// Password to validate
        password: String,
    },
}

fn main() {
    let cli = Cli::parse();
    
    match cli.command {
        Commands::Random { length, symbols } => {
            let password = generate_random(length, symbols);
            println!("Generated password: {}", password);
        }
        Commands::Passphrase { words, separator } => {
            let passphrase = generate_passphrase(words, separator);
            println!("Generated passphrase: {}", passphrase);
        }
        Commands::Pin { length } => {
            let pin = generate_pin(length);
            println!("Generated PIN: {}", pin);
        }
        Commands::Validate { password } => {
            let strength = validate_strength(&password);
            println!("Password strength: {:?}", strength);
        }
    }
}
```

---

## Part 6: Testing

Create `week14/passgen/tests/integration_test.rs`:

```rust
use passgen::{generate_random, generate_pin, validate_strength, PasswordStrength};

#[test]
fn test_random_password_length() {
    let password = generate_random(20, false);
    assert_eq!(password.len(), 20);
}

#[test]
fn test_random_password_with_symbols() {
    let password = generate_random(100, true);
    // With 100 characters, very likely to contain at least one symbol
    let has_symbol = password.chars().any(|c| "!@#$%^&*".contains(c));
    assert!(has_symbol || password.len() == 100);
}

#[test]
fn test_pin_only_digits() {
    let pin = generate_pin(6);
    assert_eq!(pin.len(), 6);
    assert!(pin.chars().all(|c| c.is_numeric()));
}

#[test]
fn test_validate_weak_password() {
    assert_eq!(validate_strength("abc"), PasswordStrength::Weak);
    assert_eq!(validate_strength("password"), PasswordStrength::Weak);
}

#[test]
fn test_validate_medium_password() {
    assert_eq!(validate_strength("Password"), PasswordStrength::Medium);
}

#[test]
fn test_validate_strong_password() {
    assert_eq!(validate_strength("Password123"), PasswordStrength::Strong);
}

#[test]
fn test_validate_very_strong_password() {
    assert_eq!(validate_strength("MyP@ssw0rd123!"), PasswordStrength::VeryStrong);
}

#[test]
fn test_passphrase_word_count() {
    let passphrase = passgen::generate_passphrase(5, '-');
    let word_count = passphrase.split('-').count();
    assert_eq!(word_count, 5);
}

#[test]
fn test_passphrase_separator() {
    let passphrase = passgen::generate_passphrase(3, '_');
    assert!(passphrase.contains('_'));
}
```

---

## Usage Examples

Test your CLI application:

```bash
# Navigate to the passgen directory
cd week14/passgen

# Generate a 20-character password with symbols
cargo run -- random --length 20 --symbols

# Generate a 4-word passphrase
cargo run -- passphrase --words 4 --separator -

# Generate a 6-digit PIN
cargo run -- pin --length 6

# Validate passwords
cargo run -- validate "password123"
cargo run -- validate "MySecure$Pass2024"

# Run tests
cargo test

# Check code quality
cargo fmt
cargo clippy
```

---

## Expected Output

### Random Password
```
$ cargo run -- random --length 16 --symbols
Generated password: K8#mP$2vQx@9Lw!n
```

### Passphrase
```
$ cargo run -- passphrase --words 4 --separator -
Generated passphrase: correct-horse-battery-staple
```

### PIN
```
$ cargo run -- pin --length 6
Generated PIN: 824759
```

### Validation
```
$ cargo run -- validate "password123"
Password strength: Medium

$ cargo run -- validate "MyP@ssw0rd123!"
Password strength: VeryStrong
```

---

## Expected Repository Structure

Your repository should now contain all 14 labs:

```
is4010-labs-yourname/
├── lab01/                    # Development toolkit setup
├── lab02/                    # AI-assisted development
├── lab03/                    # Python basics + testing
├── lab04/                    # Data structures
├── lab05/                    # Functions and error handling
├── lab06/                    # Object-oriented programming
├── lab07/                    # Data and APIs
├── lab08/                    # Python CLI application
├── lab09/                    # Rust basics
├── lab10/                    # Ownership and borrowing
├── lab11/                    # Structuring code and data
├── lab12/                    # Generics and traits
├── lab13/                    # Idiomatic Rust
└── week14/                    # Rust CLI application ✓
    └── passgen/
        ├── Cargo.toml
        ├── Cargo.lock
        ├── src/
        │   ├── main.rs
        │   ├── lib.rs
        │   ├── generator.rs
        │   └── validator.rs
        └── tests/
            └── integration_test.rs
```

---

## 🚨 Troubleshooting

**Common issues?** See the [Common Troubleshooting Guide](../resources/TROUBLESHOOTING.md) for general Rust, testing, and GitHub Actions problems.

**Lab 14-specific issues:**

### **Problem: "error: cannot find macro `clap` in this scope"**
- **Cause**: clap dependency not properly configured
- **Solution**:
  - Check `Cargo.toml` has correct clap version
  - Run `cargo build` to download dependencies
  - Make sure features = ["derive"] is included

### **Problem: Generated passwords are always the same**
- **Cause**: Not using proper random number generator
- **Solution**:
  - Use `rand::thread_rng()` not a seeded generator
  - Make sure you're calling `generate_random()` each time, not caching

### **Problem: "the trait bound `Commands: clap::Parser` is not satisfied"**
- **Cause**: Using Parser derive on Subcommand or vice versa
- **Solution**:
  - Use `#[derive(Parser)]` only on main CLI struct
  - Use `#[derive(Subcommand)]` on the Commands enum

### **Problem: Password validation tests fail randomly**
- **Cause**: Random generation means non-deterministic output
- **Solution**:
  - Test properties (length, character types) not exact values
  - Use large sample sizes for statistical tests
  - Example: `assert!(password.len() == expected_length)`

### **Problem: "unresolved import `passgen::generator`"**
- **Cause**: Module not properly exported in lib.rs
- **Solution**:
  - Make sure `pub mod generator;` is in lib.rs
  - Check file is named exactly `generator.rs`
  - Use `cargo clean && cargo build`

### **Problem: Integration tests can't find library functions**
- **Cause**: Tests trying to import from wrong location
- **Solution**:
  - Import from crate name: `use passgen::generate_random;`
  - NOT from module: `use generator::generate_random;`
  - Make sure lib.rs re-exports items

### **Problem: Clippy warnings about needless collect**
- **Cause**: Calling `.collect()` then immediately iterating
- **Solution**:
  - Chain iterators instead: `.iter().map(...).filter(...).collect()`
  - Only collect when you need to store the result

### **Problem: "argument 'symbols' is not used" warning**
- **Cause**: Defined CLI argument but not passing to function
- **Solution**:
  - Make sure to use the argument: `generate_random(length, symbols)`
  - Not: `generate_random(length, false)`

---

## Submission

### Step 1: Run All Tests

```bash
# From week14/passgen directory
cargo test
cargo fmt --check
cargo clippy -- -D warnings

# All tests should pass ✓
# Code should be properly formatted ✓
# No clippy warnings ✓
```

### Step 2: Test CLI Functionality

```bash
# Test all subcommands
cargo run -- random --length 20 --symbols
cargo run -- passphrase --words 5 --separator _
cargo run -- pin --length 8
cargo run -- validate "TestPassword123!"
```

### Step 3: Commit and Push

```bash
# From repository root
git add week14/
git commit -m "Complete Lab 14: Password Generator CLI"
git push origin main
```

### Step 4: Verify CI/CD

1. Go to your repository on GitHub
2. Click **Actions** tab
3. Find **Lab 14** workflow
4. Verify it shows a **green checkmark ✓**

---

## Success Criteria

Your lab is complete when:
- [ ] All required files created (main.rs, lib.rs, generator.rs, validator.rs)
- [ ] All CLI commands work (random, passphrase, pin, validate)
- [ ] Tests pass locally (`cargo test`)
- [ ] Code formatted (`cargo fmt`)
- [ ] No clippy warnings (`cargo clippy`)
- [ ] GitHub Actions shows green checkmark

**Grading**:
- ✅ **10 points**: All tests pass in GitHub Actions
- ❌ **0 points**: Any tests failing in GitHub Actions

---

## Optional Challenges

Want to go further? Try these extensions:

1. **Password history**: Save generated passwords to JSON file
2. **Entropy calculator**: Display password entropy in validate command
3. **Batch generation**: Generate multiple passwords at once
4. **Custom character sets**: Allow user to specify allowed characters
5. **Strength requirements**: Add `--min-strength` flag for generation

These are **not required** for full credit but are great practice!

---

## 🤖 AI Assistance Strategy

This final Rust lab combines all your skills - AI can help you design and implement a polished CLI application:

### When to Use AI

1. **CLI design decisions**: Ask AI about subcommand structure and argument organization
2. **Random generation**: Get help with secure random number generation patterns
3. **Password validation logic**: AI can help design strength validation algorithms
4. **Test case generation**: Create comprehensive test suites for all functions

### Example Prompts

1. **For clap setup**:
   ```
   "Show me how to set up a Rust CLI with clap derive macros. I need subcommands for 'random', 'passphrase', 'pin', and 'validate' with different arguments for each."
   ```

2. **For password generation**:
   ```
   "I need to generate a random password in Rust using the rand crate. It should include uppercase, lowercase, digits, and optionally symbols. Show me an idiomatic implementation."
   ```

3. **For validation logic**:
   ```
   "Create a Rust function that validates password strength. Return an enum with Weak/Medium/Strong/VeryStrong based on length, character variety, and complexity."
   ```

4. **For integration tests**:
   ```
   "Write Rust integration tests for a password generator. Test different lengths, symbol inclusion, and edge cases like length=0."
   ```

5. **For debugging clap errors**:
   ```
   "I'm getting 'the trait bound Commands: clap::Parser is not satisfied'. Here's my code: [paste]. What's wrong with my derive macros?"
   ```

6. **For iterator usage**:
   ```
   "Show me how to use iterators to generate a random password by selecting from a character set, more idiomatic than a for loop."
   ```

### Conversation Example: Designing CLI Structure

**You**: "I'm building a password generator CLI with 4 subcommands. Each needs different arguments. How should I structure this with clap?"

**AI**: "Use the derive API with a main struct and subcommand enum:

```rust
use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(name = "passgen")]
#[command(about = "Password generator and validator")]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    Random {
        #[arg(short, long, default_value_t = 16)]
        length: usize,

        #[arg(short, long)]
        symbols: bool,
    },
    Passphrase {
        #[arg(short, long, default_value_t = 4)]
        words: usize,
    },
    // ... other subcommands
}
```

Then match on `cli.command` in main()."

**You**: "How do I make the symbols flag optional?"

**AI**: "The `bool` type with `#[arg(short, long)]` is automatically a flag - it's false by default, true when present. No value needed:

```bash
cargo run -- random --symbols  # symbols = true
cargo run -- random            # symbols = false
```

Perfect for optional features!"

### Conversation Example: Password Strength Algorithm

**You**: "What's a good algorithm for password strength validation that considers length and character types?"

**AI**: "Here's a robust approach with an enum for clarity:

```rust
#[derive(Debug, PartialEq)]
enum PasswordStrength {
    Weak,
    Medium,
    Strong,
    VeryStrong,
}

fn validate_strength(password: &str) -> PasswordStrength {
    let len = password.len();
    let has_lower = password.chars().any(|c| c.is_lowercase());
    let has_upper = password.chars().any(|c| c.is_uppercase());
    let has_digit = password.chars().any(|c| c.is_numeric());
    let has_symbol = password.chars().any(|c| !c.is_alphanumeric());

    match (len, has_lower, has_upper, has_digit, has_symbol) {
        (l, _, _, _, true) if l >= 12 => PasswordStrength::VeryStrong,
        (l, true, true, true, _) if l >= 8 => PasswordStrength::Strong,
        (l, true, true, _, _) if l >= 8 => PasswordStrength::Medium,
        _ => PasswordStrength::Weak,
    }
}
```

Uses pattern matching for clean logic!"

### Recommended Tools

- **[ChatGPT](https://chat.openai.com/)** - Excellent for clap patterns and CLI design
- **[Claude](https://claude.ai/)** - Great for password validation algorithms
- **[Gemini](https://gemini.google.com/)** - Helpful for random generation patterns
- **[GitHub Copilot](https://github.com/features/copilot)** - In-editor test generation

### When to Debug Yourself

- Cargo build errors (rustc messages are very clear)
- Simple type mismatches
- Missing derive macros
- Typos in clap attributes

**Pro tip**: Run `cargo run -- --help` frequently to see how your CLI is structured. Clap auto-generates help text from your code!

---

## Looking Back: Your Rust Journey

Congratulations on completing the Rust track! You've learned:

**Lab 09**: Rust basics, ownership fundamentals, cargo workflow
**Lab 10**: Deep dive into ownership, borrowing, and lifetimes
**Lab 11**: Modules, structs, enums, and pattern matching
**Lab 12**: Generics, traits, and the type system
**Lab 13**: Iterators, smart pointers, and error handling
**Lab 14**: Building a complete CLI application ✨

You now have the foundation to:
- Build safe, concurrent systems
- Create command-line tools
- Understand low-level programming concepts
- Appreciate Rust's guarantees (memory safety, thread safety)
- Apply Rust in real-world projects

**Next steps**:
- Explore async Rust (tokio, async-std)
- Build web services with actix-web or axum
- Contribute to open-source Rust projects
- Continue with personal Rust projects

---

## 📚 Additional Resources

- **clap Examples**: https://github.com/clap-rs/clap/tree/master/examples
- **Rust CLI Book**: https://rust-cli.github.io/book/
- **rand Crate Guide**: https://rust-random.github.io/book/
- **Password Security**: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#password-complexity

---

**Need Help?**
- Review Chapters 9-14 in the textbook
- Check the troubleshooting section above
- See [Common Troubleshooting Guide](../resources/TROUBLESHOOTING.md)
- Use AI assistants (Copilot, Gemini CLI, ChatGPT)
- Ask on the course discussion board
- Attend office hours

**Congratulations on completing all 14 labs!** 🎉
