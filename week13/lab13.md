# Lab 13: Idiomatic Rust

**Due**: End of week (Sunday at 11:59 PM)
**Points**: 10 points
**Chapter**: Chapter 13 - Idiomatic Rust

---

## Objective

Master advanced Rust patterns that make code elegant, efficient, and truly "Rusty". This lab covers three essential topics: iterators and closures for functional programming, smart pointers for flexible memory management, and idiomatic error handling with `Result<T, E>`. These patterns are used throughout professional Rust codebases.

**What you'll learn:**
- Iterator methods (`.map()`, `.filter()`, `.fold()`, `.collect()`)
- Closures and higher-order functions
- Smart pointers (`Box<T>`, `Rc<T>`, `RefCell<T>`)
- Idiomatic error handling with `Result<T, E>` and the `?` operator
- Custom error types
- Combining all three patterns in real-world scenarios

---

## Background

Rust's power comes from patterns that combine safety, performance, and expressiveness. These three concepts are fundamental to writing idiomatic Rust:

**Iterators & Closures**: Process collections functionally without explicit loops
**Smart Pointers**: Manage memory flexibly while maintaining safety
**Error Handling**: Make errors explicit and recoverable without exceptions

**Real-world usage:**
- **Iterators**: Data processing pipelines (similar to Python's list comprehensions)
- **Smart pointers**: Building trees, graphs, and shared ownership scenarios
- **Result<T, E>**: Every library in the Rust ecosystem uses this for error handling

**Documentation & Resources:**
- [Iterator trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [Iterator methods](https://doc.rust-lang.org/std/iter/trait.Iterator.html#provided-methods)
- [Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Fn traits](https://doc.rust-lang.org/book/ch13-01-closures.html#closure-type-inference-and-annotation)
- [FnOnce, FnMut, Fn](https://doc.rust-lang.org/std/ops/index.html#traits)
- [Smart Pointers](https://doc.rust-lang.org/book/ch15-00-smart-pointers.html)
- [Box<T>](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [Rc<T>](https://doc.rust-lang.org/std/rc/struct.Rc.html)
- [RefCell<T>](https://doc.rust-lang.org/std/cell/struct.RefCell.html)
- [Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
- [Result<T, E>](https://doc.rust-lang.org/std/result/enum.Result.html)
- [? operator](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html#a-shortcut-for-propagating-errors-the--operator)
- [Custom error types](https://doc.rust-lang.org/rust-by-example/error/multiple_error_types/define_error_type.html)
- [thiserror crate](https://docs.rs/thiserror/latest/thiserror/) (optional)
- [anyhow crate](https://docs.rs/anyhow/latest/anyhow/) (optional)

---

## Prerequisites

Before starting this lab, ensure you have:
- [ ] Completed Labs 09-12 (Rust basics through traits)
- [ ] Rust toolchain installed (`cargo --version`)
- [ ] Understanding of ownership and borrowing
- [ ] Familiarity with structs and enums

---

## Part 1: Iterators and Closures (30%)

Iterators allow you to process sequences of items without manual indexing. Closures are anonymous functions that can capture their environment.

### Exercise 1.1: Text Statistics

Create a function that analyzes text using iterator methods.

In `src/main.rs`:

```rust
/// Analyzes text and returns word count, average word length, and longest word.
///
/// # Arguments
/// * `text` - The text to analyze
///
/// # Returns
/// Tuple of (word_count, average_length, longest_word)
///
/// # Examples
/// ```
/// let stats = analyze_text("hello world");
/// assert_eq!(stats, (2, 5.0, "hello".to_string()));
/// ```
fn analyze_text(text: &str) -> (usize, f64, String) {
    let words: Vec<&str> = text
        .split_whitespace()
        .collect();

    if words.is_empty() {
        return (0, 0.0, String::new());
    }

    let word_count = words.len();

    // Calculate average word length using iterator methods
    let total_length: usize = words
        .iter()
        .map(|word| word.len())
        .sum();
    
    let average_length = total_length as f64 / word_count as f64;

    // Find longest word
    let longest_word = words
        .iter()
        .max_by_key(|word| word.len())
        .unwrap_or(&"")
        .to_string();

    (word_count, average_length, longest_word)
}
```

### Exercise 1.2: Custom Iterator Chains

Implement a function that uses multiple iterator methods chained together.

```rust
/// Filters and transforms a list of numbers:
/// - Keep only even numbers
/// - Square each number
/// - Return sum of results
///
/// # Examples
/// ```
/// let result = process_numbers(&[1, 2, 3, 4, 5, 6]);
/// assert_eq!(result, 56); // 2^2 + 4^2 + 6^2 = 4 + 16 + 36 = 56
/// ```
fn process_numbers(numbers: &[i32]) -> i32 {
    numbers
        .iter()
        .filter(|&&n| n % 2 == 0)  // Keep only even numbers
        .map(|&n| n * n)             // Square each
        .sum()                        // Sum them up
}
```

### Exercise 1.3: Closures with State

Create a closure that captures and modifies external state.

```rust
/// Returns a closure that counts how many times it's been called.
///
/// # Examples
/// ```
/// let mut counter = make_counter();
/// assert_eq!(counter(), 1);
/// assert_eq!(counter(), 2);
/// assert_eq!(counter(), 3);
/// ```
fn make_counter() -> impl FnMut() -> i32 {
    let mut count = 0;
    move || {
        count += 1;
        count
    }
}
```

**Your task**: Implement these three functions and add tests for each.

---

## Part 2: Smart Pointers (30%)

Smart pointers provide additional functionality beyond regular references while maintaining Rust's safety guarantees.

### Exercise 2.1: Box<T> for Recursive Types

Use `Box<T>` to create a simple binary tree.

```rust
#[derive(Debug, PartialEq)]
enum BinaryTree<T> {
    Empty,
    Node {
        value: T,
        left: Box<BinaryTree<T>>,
        right: Box<BinaryTree<T>>,
    },
}

impl<T> BinaryTree<T> {
    /// Creates a new empty tree
    fn new() -> Self {
        BinaryTree::Empty
    }

    /// Creates a leaf node (node with no children)
    fn leaf(value: T) -> Self {
        BinaryTree::Node {
            value,
            left: Box::new(BinaryTree::Empty),
            right: Box::new(BinaryTree::Empty),
        }
    }

    /// Creates a node with left and right children
    fn node(value: T, left: BinaryTree<T>, right: BinaryTree<T>) -> Self {
        BinaryTree::Node {
            value,
            left: Box::new(left),
            right: Box::new(right),
        }
    }
}
```

### Exercise 2.2: Rc<T> for Shared Ownership

Use `Rc<T>` (Reference Counted) when multiple parts of your code need to own the same data.

```rust
use std::rc::Rc;

#[derive(Debug)]
struct SharedData {
    value: i32,
}

/// Demonstrates shared ownership with Rc<T>
fn demonstrate_rc() {
    let data = Rc::new(SharedData { value: 42 });
    
    // Create additional owners
    let owner1 = Rc::clone(&data);
    let owner2 = Rc::clone(&data);
    
    println!("Reference count: {}", Rc::strong_count(&data)); // Should print 3
    println!("Value: {}", owner1.value);
    
    // When all owners go out of scope, data is deallocated
}
```

### Exercise 2.3: RefCell<T> for Interior Mutability

Combine `Rc<T>` and `RefCell<T>` for shared mutable data.

```rust
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
struct Counter {
    value: i32,
}

impl Counter {
    fn new() -> Rc<RefCell<Counter>> {
        Rc::new(RefCell::new(Counter { value: 0 }))
    }

    fn increment(counter: &Rc<RefCell<Counter>>) {
        counter.borrow_mut().value += 1;
    }

    fn get_value(counter: &Rc<RefCell<Counter>>) -> i32 {
        counter.borrow().value
    }
}

/// Demonstrates multiple shared mutable references
fn demonstrate_refcell() {
    let counter = Counter::new();
    let counter_ref1 = Rc::clone(&counter);
    let counter_ref2 = Rc::clone(&counter);

    Counter::increment(&counter_ref1);
    Counter::increment(&counter_ref2);

    println!("Counter value: {}", Counter::get_value(&counter)); // Should print 2
}
```

**Your task**: Implement all three smart pointer examples and add tests.

---

## Part 3: Idiomatic Error Handling (30%)

Rust doesn't have exceptions. Instead, it uses `Result<T, E>` for recoverable errors.

### Exercise 3.1: Basic Result Handling

Create a function that returns `Result<T, E>`.

```rust
/// Divides two numbers, returning an error for division by zero.
///
/// # Examples
/// ```
/// assert_eq!(divide(10.0, 2.0), Ok(5.0));
/// assert!(divide(10.0, 0.0).is_err());
/// ```
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err(String::from("Division by zero"))
    } else {
        Ok(a / b)
    }
}
```

### Exercise 3.2: The ? Operator

The `?` operator propagates errors automatically.

```rust
use std::fs::File;
use std::io::{self, Read};

/// Reads a file and returns its contents.
/// Uses ? operator to propagate errors.
fn read_file_contents(path: &str) -> io::Result<String> {
    let mut file = File::open(path)?;  // ? propagates error if file doesn't exist
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;  // ? propagates read errors
    Ok(contents)
}
```

### Exercise 3.3: Custom Error Types

Create your own error type for better error handling.

```rust
use std::fmt;

#[derive(Debug, Clone)]
enum ParseError {
    EmptyInput,
    InvalidNumber(String),
    OutOfRange(i32),
}

impl fmt::Display for ParseError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            ParseError::EmptyInput => write!(f, "Input string is empty"),
            ParseError::InvalidNumber(s) => write!(f, "Invalid number: {}", s),
            ParseError::OutOfRange(n) => write!(f, "Number out of range: {}", n),
        }
    }
}

/// Parses a string to a positive number (1-100).
///
/// # Errors
/// Returns ParseError if:
/// - Input is empty
/// - Input is not a valid number
/// - Number is not in range 1-100
fn parse_positive_number(input: &str) -> Result<i32, ParseError> {
    if input.is_empty() {
        return Err(ParseError::EmptyInput);
    }

    let num: i32 = input
        .trim()
        .parse()
        .map_err(|_| ParseError::InvalidNumber(input.to_string()))?;

    if num < 1 || num > 100 {
        return Err(ParseError::OutOfRange(num));
    }

    Ok(num)
}
```

**Your task**: Implement all error handling functions and add comprehensive tests.

---

## Part 4: Integrative Exercise (10%)

Combine all three concepts in a real-world scenario.

### File Processor with Error Handling

Create a program that:
1. Uses **iterators** to process lines from input
2. Uses **smart pointers** to share configuration
3. Uses **Result** for robust error handling

```rust
use std::rc::Rc;
use std::cell::RefCell;

#[derive(Debug, Clone)]
struct Config {
    min_length: usize,
    max_length: usize,
}

#[derive(Debug)]
enum ProcessError {
    LineTooShort(String),
    LineTooLong(String),
}

impl fmt::Display for ProcessError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            ProcessError::LineTooShort(line) => {
                write!(f, "Line too short: {}", line)
            }
            ProcessError::LineTooLong(line) => {
                write!(f, "Line too long: {}", line)
            }
        }
    }
}

/// Processes text lines with shared configuration.
/// Filters lines by length and converts to uppercase.
fn process_lines(
    lines: &[String],
    config: Rc<RefCell<Config>>,
) -> Result<Vec<String>, ProcessError> {
    lines
        .iter()
        .map(|line| {
            let cfg = config.borrow();
            let len = line.len();

            if len < cfg.min_length {
                Err(ProcessError::LineTooShort(line.clone()))
            } else if len > cfg.max_length {
                Err(ProcessError::LineTooLong(line.clone()))
            } else {
                Ok(line.to_uppercase())
            }
        })
        .collect()
}
```

**Your task**: Implement this integrative example and test it with various inputs.

---

## Testing

Add comprehensive tests to `src/main.rs`:

```rust
#[cfg(test)]
mod tests {
    use super::*;

    // Part 1: Iterators and Closures Tests
    #[test]
    fn test_analyze_text_basic() {
        let result = analyze_text("hello world");
        assert_eq!(result.0, 2);
        assert!((result.1 - 5.0).abs() < 0.01);
        assert_eq!(result.2, "hello");
    }

    #[test]
    fn test_analyze_text_empty() {
        let result = analyze_text("");
        assert_eq!(result, (0, 0.0, String::new()));
    }

    #[test]
    fn test_process_numbers() {
        assert_eq!(process_numbers(&[1, 2, 3, 4, 5, 6]), 56);
        assert_eq!(process_numbers(&[1, 3, 5]), 0);
        assert_eq!(process_numbers(&[]), 0);
    }

    #[test]
    fn test_counter_closure() {
        let mut counter = make_counter();
        assert_eq!(counter(), 1);
        assert_eq!(counter(), 2);
        assert_eq!(counter(), 3);
    }

    // Part 2: Smart Pointers Tests
    #[test]
    fn test_binary_tree_creation() {
        let tree = BinaryTree::node(
            5,
            BinaryTree::leaf(3),
            BinaryTree::leaf(7),
        );
        
        match tree {
            BinaryTree::Node { value, .. } => assert_eq!(value, 5),
            _ => panic!("Expected Node"),
        }
    }

    #[test]
    fn test_rc_reference_counting() {
        let data = Rc::new(SharedData { value: 42 });
        assert_eq!(Rc::strong_count(&data), 1);
        
        let _owner1 = Rc::clone(&data);
        assert_eq!(Rc::strong_count(&data), 2);
        
        let _owner2 = Rc::clone(&data);
        assert_eq!(Rc::strong_count(&data), 3);
    }

    #[test]
    fn test_refcell_mutation() {
        let counter = Counter::new();
        assert_eq!(Counter::get_value(&counter), 0);
        
        Counter::increment(&counter);
        assert_eq!(Counter::get_value(&counter), 1);
        
        Counter::increment(&counter);
        assert_eq!(Counter::get_value(&counter), 2);
    }

    // Part 3: Error Handling Tests
    #[test]
    fn test_divide_success() {
        assert_eq!(divide(10.0, 2.0), Ok(5.0));
        assert_eq!(divide(9.0, 3.0), Ok(3.0));
    }

    #[test]
    fn test_divide_by_zero() {
        assert!(divide(10.0, 0.0).is_err());
    }

    #[test]
    fn test_parse_positive_number_valid() {
        assert_eq!(parse_positive_number("50"), Ok(50));
        assert_eq!(parse_positive_number("1"), Ok(1));
        assert_eq!(parse_positive_number("100"), Ok(100));
    }

    #[test]
    fn test_parse_positive_number_errors() {
        assert!(matches!(
            parse_positive_number(""),
            Err(ParseError::EmptyInput)
        ));
        
        assert!(matches!(
            parse_positive_number("abc"),
            Err(ParseError::InvalidNumber(_))
        ));
        
        assert!(matches!(
            parse_positive_number("150"),
            Err(ParseError::OutOfRange(150))
        ));
    }

    // Part 4: Integrative Tests
    #[test]
    fn test_process_lines_success() {
        let config = Rc::new(RefCell::new(Config {
            min_length: 3,
            max_length: 10,
        }));

        let lines = vec![
            "hello".to_string(),
            "world".to_string(),
        ];

        let result = process_lines(&lines, config);
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), vec!["HELLO", "WORLD"]);
    }

    #[test]
    fn test_process_lines_too_short() {
        let config = Rc::new(RefCell::new(Config {
            min_length: 5,
            max_length: 10,
        }));

        let lines = vec!["hi".to_string()];
        let result = process_lines(&lines, config);
        assert!(result.is_err());
    }
}
```

---

## Expected Repository Structure

Your repository should now contain all 13 labs:

```
is4010-labs-yourname/
├── lab01/ through lab08/  # Python labs
├── lab09/                 # Rust basics
├── lab10/                 # Ownership and borrowing
├── lab11/                 # Structuring code and data
├── lab12/                 # Generics and traits
└── week13/                 # Idiomatic Rust ✓
    └── week13/
        ├── Cargo.toml
        ├── Cargo.lock
        ├── src/
        │   ├── main.rs
        │   └── lib.rs
        └── tests/
            └── integration_tests.rs
```

This demonstrates your progression through advanced Rust concepts, from basic syntax to idiomatic patterns used in production code.

---

## Running Your Code

```bash
# From repository root
cd week13

# Run all tests
cargo test

# Run tests with output
cargo test -- --nocapture

# Run specific test
cargo test test_analyze_text

# Check formatting
cargo fmt --check

# Run clippy (linter)
cargo clippy

# Build and run
cargo run
```

---

## Expected Output

When running `cargo test`, you should see:

```
running 15 tests
test tests::test_analyze_text_basic ... ok
test tests::test_analyze_text_empty ... ok
test tests::test_process_numbers ... ok
test tests::test_counter_closure ... ok
test tests::test_binary_tree_creation ... ok
test tests::test_rc_reference_counting ... ok
test tests::test_refcell_mutation ... ok
test tests::test_divide_success ... ok
test tests::test_divide_by_zero ... ok
test tests::test_parse_positive_number_valid ... ok
test tests::test_parse_positive_number_errors ... ok
test tests::test_process_lines_success ... ok
test tests::test_process_lines_too_short ... ok

test result: ok. 15 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

---

## 🚨 Troubleshooting

**Common issues?** See the [Common Troubleshooting Guide](../resources/TROUBLESHOOTING.md) for general Rust, testing, and GitHub Actions problems.

**Lab 13-specific issues:**

### **Problem: "cannot borrow as mutable" with closures**
- **Cause**: Closure needs `FnMut` instead of `Fn`
- **Solution**:
  - Use `FnMut` when closure modifies captured variables
  - Use `move` keyword to transfer ownership into closure
  - Example: `fn make_counter() -> impl FnMut() -> i32`

### **Problem: "Box<T> cannot be sized" error**
- **Cause**: Trying to create recursive type without Box
- **Solution**:
  - Wrap recursive fields in `Box<T>`: `left: Box<BinaryTree<T>>`
  - Box provides a known size (pointer size) for recursive types
  - Without Box, compiler can't determine struct size

### **Problem: "cannot move out of borrowed content" with Rc**
- **Cause**: Trying to move value out of `Rc<T>`
- **Solution**:
  - Use `Rc::clone(&data)` to create new reference
  - Never dereference and move: `*data` (this won't work)
  - Rc::clone is cheap - only increments reference count

### **Problem: "already borrowed: BorrowMutError" with RefCell**
- **Cause**: Trying to borrow mutably while immutable borrow exists (or vice versa)
- **Solution**:
  - `borrow()` and `borrow_mut()` follow Rust's borrowing rules at runtime
  - Make sure borrows go out of scope before borrowing again
  - Use separate scopes if needed:
    ```rust
    {
        let val = counter.borrow();
        // use val
    } // borrow ends here
    counter.borrow_mut().value += 1; // now this works
    ```

### **Problem: "the `?` operator can only be used in a function that returns Result"**
- **Cause**: Using `?` in a function that returns non-Result type
- **Solution**:
  - Change function signature to return `Result<T, E>`
  - Or handle error explicitly with `match` or `.unwrap()`
  - Example: `fn my_func() -> Result<i32, MyError>` instead of `fn my_func() -> i32`

### **Problem: "cannot use `?` operator with different error types"**
- **Cause**: Trying to use `?` with errors that don't convert to each other
- **Solution**:
  - Use `.map_err()` to convert error types:
    ```rust
    value.parse()
        .map_err(|_| ParseError::InvalidNumber(value.to_string()))?
    ```
  - Or use a library like `thiserror` or `anyhow` for automatic conversion

### **Problem: Iterator method chain compile errors**
- **Cause**: Type inference issues or incorrect chaining
- **Solution**:
  - Break chain into steps and compile incrementally
  - Add type annotations: `.collect::<Vec<_>>()`
  - Check that each method returns the right type for the next
  - Use `.into_iter()` vs `.iter()` correctly

### **Problem: "closure may outlive the current function"**
- **Cause**: Closure captures reference that might not live long enough
- **Solution**:
  - Use `move` keyword to transfer ownership: `move || { ... }`
  - Or ensure captured references have sufficient lifetime
  - Example: `fn make_counter() -> impl FnMut()` requires `move`

### **Problem: "trait `Display` is not implemented"**
- **Cause**: Custom error type doesn't implement Display
- **Solution**:
  - Implement `std::fmt::Display` trait for your error type
  - Required for error types to work with `?` operator
  - See Exercise 3.3 for example implementation

### **Problem: Tests pass locally but fail in GitHub Actions**
- **Cause**: Floating point comparison or platform differences
- **Solution**:
  - Use epsilon comparison for floats: `(a - b).abs() < 0.0001`
  - Don't use exact `==` for f64 values
  - Check that you're not relying on filesystem specifics

---

## 🤖 AI Assistance Strategy

This lab covers advanced Rust patterns that AI tools can help you understand and implement effectively:

### When to Use AI

1. **Understanding iterator chains**: AI excels at explaining complex iterator method combinations
2. **Debugging smart pointer issues**: Get help with Rc/RefCell borrow checker errors
3. **Designing error types**: Ask AI to help create custom error enums with proper variants
4. **Clarifying closure syntax**: AI can explain Fn, FnMut, and FnOnce trait differences

### Example Prompts

1. **For iterator chains**:
   ```
   "I need to filter a vector of strings by length, convert to uppercase, and collect into a Vec. Show me the idiomatic Rust iterator chain."
   ```

2. **For smart pointers**:
   ```
   "Explain when to use Box<T> vs Rc<T> vs RefCell<T> in Rust. Provide examples of each use case."
   ```

3. **For error handling**:
   ```
   "I have a parse_number function that can fail in two ways: EmptyInput and InvalidNumber. Show me how to create a custom error enum and use the ? operator."
   ```

4. **For closure understanding**:
   ```
   "What's the difference between FnOnce, FnMut, and Fn traits in Rust closures? When would each be required?"
   ```

5. **For debugging borrow checker**:
   ```
   "I'm getting 'cannot borrow as mutable because it is also borrowed as immutable' with Rc<RefCell<T>>. Here's my code: [paste]. How do I fix it?"
   ```

6. **For binary tree implementation**:
   ```
   "Show me how to implement a binary tree in Rust using Box<T> for recursive structure. Include insert and find methods."
   ```

### Conversation Example: Iterator Chains

**You**: "I have a Vec<String> and I need to:
1. Filter strings longer than 3 characters
2. Remove whitespace
3. Convert to uppercase
4. Collect into a Vec

How do I chain these operations idiomatically?"

**AI**: "Here's the idiomatic Rust approach using iterator adapters:

```rust
let result: Vec<String> = strings
    .iter()
    .filter(|s| s.len() > 3)
    .map(|s| s.trim())
    .map(|s| s.to_uppercase())
    .map(|s| s.to_string())
    .collect();
```

Each method is an iterator adapter that transforms the data. The final `collect()` consumes the iterator and builds the Vec."

**You**: "Can I combine the two map operations?"

**AI**: "Yes! You can chain transformations in a single map:

```rust
let result: Vec<String> = strings
    .iter()
    .filter(|s| s.len() > 3)
    .map(|s| s.trim().to_uppercase())
    .collect();
```

This is more efficient because it creates fewer intermediate iterators."

### Conversation Example: Smart Pointers

**You**: "I'm building a tree structure where multiple nodes can reference the same configuration object. The configuration can be updated. What smart pointer combination should I use?"

**AI**: "You need `Rc<RefCell<Config>>`. Here's why:

- `Rc<T>` provides shared ownership (multiple nodes can reference it)
- `RefCell<T>` provides interior mutability (config can be updated)

Example:

```rust
use std::rc::Rc;
use std::cell::RefCell;

struct Config { /* fields */ }
struct Node {
    config: Rc<RefCell<Config>>,
}

let shared_config = Rc::new(RefCell::new(Config { /* ... */ }));
let node1 = Node { config: Rc::clone(&shared_config) };
let node2 = Node { config: Rc::clone(&shared_config) };

// Update through any reference
shared_config.borrow_mut().some_field = new_value;
```

Both nodes see the update!"

### Recommended Tools

- **[ChatGPT](https://chat.openai.com/)** - Excellent for explaining Rust concepts and iterator patterns
- **[Claude](https://claude.ai/)** - Great for debugging complex borrow checker errors
- **[Gemini](https://gemini.google.com/)** - Helpful for understanding smart pointer combinations
- **[GitHub Copilot](https://github.com/features/copilot)** - In-editor assistance for implementing iterator chains

### When to Debug Yourself

- Simple iterator method lookups (check [std::iter documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html))
- Basic syntax errors (rustc gives great error messages)
- Understanding compiler error messages (read them carefully, they're very informative)

**Pro tip**: Rust's compiler errors often include suggestions for fixes. Read the full error message before asking AI for help!

---

## Submission

### Step 1: Run Tests and Checks

```bash
# From repository root
cd week13

# Run all tests
cargo test

# Check formatting
cargo fmt --check

# Run clippy
cargo clippy -- -D warnings

# All should pass ✓
```

### Step 2: Commit and Push

```bash
# From repository root
git add week13/
git commit -m "Complete Lab 13: Idiomatic Rust"
git push origin main
```

### Step 3: Verify CI/CD

1. Go to your repository on GitHub
2. Click **Actions** tab
3. Find **Lab 13** workflow
4. Verify it shows a **green checkmark ✓**

---

## Success Criteria

Your lab is complete when:
- [ ] All 15+ tests pass (`cargo test`)
- [ ] Code compiles without warnings
- [ ] `cargo fmt --check` passes
- [ ] `cargo clippy` has no warnings
- [ ] GitHub Actions shows green checkmark
- [ ] All three concepts implemented (iterators, smart pointers, error handling)
- [ ] Integrative exercise combines all concepts

**Grading**:
- ✅ **10 points**: All tests pass in GitHub Actions, fmt and clippy clean
- ❌ **0 points**: Any tests failing or clippy warnings

---

## Optional Challenges

Want to go further? Try these extensions:

1. **Custom Iterator**: Implement the `Iterator` trait for BinaryTree (in-order traversal)
2. **Arc<Mutex<T>>**: Convert RefCell example to use Arc/Mutex for thread safety
3. **Error Chain**: Create multiple error types and convert between them
4. **Collect to HashMap**: Use iterators to build a word frequency counter
5. **Lazy Evaluation**: Create an infinite iterator with `.take(n)`

These are **not required** for full credit but are great practice!

---

## 📚 Additional Resources

- **The Rust Book Ch 13**: https://doc.rust-lang.org/book/ch13-00-functional-features.html
- **The Rust Book Ch 15**: https://doc.rust-lang.org/book/ch15-00-smart-pointers.html
- **The Rust Book Ch 9**: https://doc.rust-lang.org/book/ch09-00-error-handling.html
- **Iterator Documentation**: https://doc.rust-lang.org/std/iter/trait.Iterator.html
- **Rc Documentation**: https://doc.rust-lang.org/std/rc/struct.Rc.html
- **RefCell Documentation**: https://doc.rust-lang.org/std/cell/struct.RefCell.html

---

**Need Help?**
- Review Chapter 13 in the textbook
- Check the troubleshooting section above
- See [Common Troubleshooting Guide](../resources/TROUBLESHOOTING.md)
- Use AI assistants (Copilot, Gemini CLI, ChatGPT)
- Ask on the course discussion board
- Attend office hours
