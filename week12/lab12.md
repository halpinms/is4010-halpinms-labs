# Lab 12: Generic stack implementation

**Due**: End of week (Sunday at 11:59 PM)
**Points:** 10

## 📋 Enhanced objective

Build a fully-functional [generic stack data structure](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) in Rust that demonstrates:
- **Generic programming** with [`<T>` type parameters](https://doc.rust-lang.org/book/ch10-01-syntax.html)
- **Trait implementation** for [`Display`](https://doc.rust-lang.org/std/fmt/trait.Display.html) and [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- **Trait bounds** to constrain generic types
- **Polymorphism** through generics (same code works with any type)
- **Professional code organization** following Rust best practices

This lab synthesizes the generics and traits concepts from Week 12, demonstrating how to build reusable, type-safe data structures in Rust.

---

## 🎯 Background

### Why stacks matter

[Stacks](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) are fundamental data structures used throughout computer science:

**Applications:**
- **Function calls**: Call stack in every programming language
- **Expression evaluation**: Calculators, compilers
- **Undo/redo**: Text editors, graphics programs
- **Browser history**: Back/forward navigation

**Stack operations (LIFO - Last In, First Out):**
- **push**: Add element to top
- **pop**: Remove and return top element
- **peek**: View top element without removing
- **is_empty**: Check if stack has no elements
- **len**: Get number of elements

### Why generics matter

Your `Stack<T>` will work with **any type**:
```rust
let int_stack: Stack<i32> = Stack::new();
let string_stack: Stack<String> = Stack::new();
let vec_stack: Stack<Vec<f64>> = Stack::new();
```

This is the power of **generic programming** - write once, use everywhere!

---

## 🔧 Prerequisites

- **Rust toolchain** - [Installation guide](../../resources/SETUP_GUIDE.md#rust-installation)
- **Git** for version control
- Knowledge of generics and traits from Week 12 lectures

---

## 📁 Part 1: Project setup

### Create the project

```bash
# From your is4010-labs directory
cargo new week12 --bin
cd week12
```

### Set up the initial structure

Replace `src/main.rs` contents:

```rust
fn main() {
    println!("Lab 12: Generic Stack Implementation");

    // You'll test your stack here
    let mut stack = Stack::new();
    stack.push(1);
    stack.push(2);
    stack.push(3);

    println!("Stack: {}", stack);
    println!("Popped: {:?}", stack.pop());
    println!("Peek: {:?}", stack.peek());
}

// Your Stack implementation will go here

#[cfg(test)]
mod tests {
    use super::*;

    // Tests will go here
}
```

Verify setup:
```bash
cargo build  # Should compile (but main won't work yet)
```

---

## 📚 Part 2: Implement the generic Stack

### Define the generic struct

Add this above `main()`:

```rust
struct Stack<T> {
    items: Vec<T>,
}
```

**Key concepts:**
- `<T>` is a **type parameter** - it can be any type
- `Vec<T>` is also generic - our stack uses a vector internally
- When you create `Stack<i32>`, `T` becomes `i32` everywhere

### Implement basic methods

```rust
impl<T> Stack<T> {
    /// Creates a new empty stack
    fn new() -> Stack<T> {
        Stack { items: Vec::new() }
    }

    /// Returns true if the stack has no elements
    fn is_empty(&self) -> bool {
        self.items.is_empty()
    }

    /// Adds an item to the top of the stack
    fn push(&mut self, item: T) {
        self.items.push(item);
    }

    /// Returns the number of items in the stack
    fn len(&self) -> usize {
        self.items.len()
    }

    /// Removes and returns the top item, or None if empty
    fn pop(&mut self) -> Option<T> {
        self.items.pop()
    }

    /// Returns a reference to the top item without removing it
    fn peek(&self) -> Option<&T> {
        self.items.last()
    }
}
```

**Understanding the syntax:**
- `impl<T>` - "For any type T..."
- `&self` - Immutable borrow (doesn't change the stack)
- `&mut self` - Mutable borrow (modifies the stack)
- `Option<T>` - Returns `Some(value)` or `None`

### Test your implementation

Try running:
```bash
cargo run
```

You should see output showing the stack operations working!

### Add comprehensive tests

Add these tests to the test module:

```rust
#[test]
fn test_new_stack_is_empty() {
    let stack: Stack<i32> = Stack::new();
    assert!(stack.is_empty());
    assert_eq!(stack.len(), 0);
}

#[test]
fn test_push_increases_length() {
    let mut stack = Stack::new();
    stack.push(1);
    stack.push(2);
    stack.push(3);
    assert_eq!(stack.len(), 3);
    assert!(!stack.is_empty());
}

#[test]
fn test_pop_returns_last_pushed() {
    let mut stack = Stack::new();
    stack.push(1);
    stack.push(2);
    assert_eq!(stack.pop(), Some(2));
    assert_eq!(stack.pop(), Some(1));
    assert_eq!(stack.pop(), None);
}

#[test]
fn test_pop_empty_stack() {
    let mut stack: Stack<i32> = Stack::new();
    assert_eq!(stack.pop(), None);
}

#[test]
fn test_peek_without_removing() {
    let mut stack = Stack::new();
    stack.push(42);
    assert_eq!(stack.peek(), Some(&42));
    assert_eq!(stack.len(), 1);
}

#[test]
fn test_peek_empty_stack() {
    let stack: Stack<i32> = Stack::new();
    assert_eq!(stack.peek(), None);
}

#[test]
fn test_with_strings() {
    let mut stack = Stack::new();
    stack.push(String::from("hello"));
    stack.push(String::from("world"));
    assert_eq!(stack.pop(), Some(String::from("world")));
}

#[test]
fn test_push_pop_sequence() {
    let mut stack = Stack::new();
    stack.push(1);
    stack.push(2);
    assert_eq!(stack.pop(), Some(2));
    stack.push(3);
    assert_eq!(stack.pop(), Some(3));
    assert_eq!(stack.pop(), Some(1));
}
```

Run tests:
```bash
cargo test
```

You should have **at least 8 tests passing** for basic functionality.

---

## 🎨 Part 3: Implement the Display trait

The [`Display` trait](https://doc.rust-lang.org/std/fmt/trait.Display.html) allows your stack to be printed with `println!("{}", stack)`.

### Add the implementation

Add this to your code:

```rust
use std::fmt;

impl<T: fmt::Display> fmt::Display for Stack<T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[")?;
        for (i, item) in self.items.iter().enumerate() {
            if i > 0 {
                write!(f, ", ")?;
            }
            write!(f, "{}", item)?;
        }
        write!(f, "]")
    }
}
```

**Understanding the syntax:**
- `impl<T: fmt::Display>` - "For any type T that implements Display..."
- This is a **trait bound** - we can only display T if T is displayable
- `write!` and `?` operator for error handling

### Test Display implementation

Add these tests:

```rust
#[test]
fn test_display_format() {
    let mut stack = Stack::new();
    stack.push(1);
    stack.push(2);
    stack.push(3);
    assert_eq!(format!("{}", stack), "[1, 2, 3]");
}

#[test]
fn test_display_empty() {
    let stack: Stack<i32> = Stack::new();
    assert_eq!(format!("{}", stack), "[]");
}

#[test]
fn test_display_strings() {
    let mut stack = Stack::new();
    stack.push("hello");
    stack.push("world");
    assert_eq!(format!("{}", stack), "[hello, world]");
}
```

---

## 🔁 Part 4: Implement the Iterator trait

The [`Iterator` trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html) allows your stack to be used in `for` loops and with iterator methods.

### Add the implementation

```rust
impl<T> Iterator for Stack<T> {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        self.pop()  // Iterates in LIFO order!
    }
}

impl<T> IntoIterator for Stack<T> {
    type Item = T;
    type IntoIter = Stack<T>;

    fn into_iter(self) -> Self::IntoIter {
        self
    }
}
```

**Understanding the syntax:**
- `type Item = T;` - Associated type declaration
- `IntoIterator` trait allows using the stack in `for` loops
- Iterator consumes the stack (pops items in LIFO order)

### Test Iterator implementation

Add these tests:

```rust
#[test]
fn test_iterator() {
    let mut stack = Stack::new();
    stack.push(1);
    stack.push(2);
    stack.push(3);

    let mut iter = stack.into_iter();
    assert_eq!(iter.next(), Some(3));  // LIFO order!
    assert_eq!(iter.next(), Some(2));
    assert_eq!(iter.next(), Some(1));
    assert_eq!(iter.next(), None);
}

#[test]
fn test_for_loop() {
    let mut stack = Stack::new();
    stack.push(1);
    stack.push(2);

    let mut results = Vec::new();
    for item in stack {
        results.push(item);
    }
    assert_eq!(results, vec![2, 1]);  // LIFO!
}

#[test]
fn test_iterator_with_strings() {
    let mut stack = Stack::new();
    stack.push(String::from("first"));
    stack.push(String::from("second"));

    let collected: Vec<String> = stack.into_iter().collect();
    assert_eq!(collected, vec![String::from("second"), String::from("first")]);
}
```

---

## ✅ Part 5: Comprehensive testing

### Final test requirements

Your test suite must have **at least 15 tests** covering:
- Basic functionality (new, push, pop, peek, len, is_empty)
- Multiple data types (integers, strings, etc.)
- Edge cases (empty stack, single element)
- Display trait formatting
- Iterator behavior

Add one more test demonstrating polymorphism:

```rust
#[test]
fn test_polymorphism() {
    // Same Stack code works with different types!
    let mut int_stack = Stack::new();
    int_stack.push(1);
    int_stack.push(2);
    assert_eq!(int_stack.pop(), Some(2));

    let mut string_stack = Stack::new();
    string_stack.push(String::from("hello"));
    string_stack.push(String::from("world"));
    assert_eq!(string_stack.pop(), Some(String::from("world")));

    let mut float_stack = Stack::new();
    float_stack.push(3.14);
    float_stack.push(2.71);
    assert_eq!(float_stack.pop(), Some(2.71));
}
```

### Run all tests

```bash
cargo test
```

Expected output:
```
running 15 tests
...
test result: ok. 15 passed; 0 failed
```

---

## 🎯 Part 6: Update main() for demonstration

Update your `main()` function to demonstrate all capabilities:

```rust
fn main() {
    println!("Lab 12: Generic Stack Implementation\n");

    // Demonstrate with integers
    println!("=== Integer Stack ===");
    let mut int_stack = Stack::new();
    int_stack.push(10);
    int_stack.push(20);
    int_stack.push(30);
    println!("Stack: {}", int_stack);
    println!("Popped: {:?}", int_stack.pop());
    println!("Peek: {:?}", int_stack.peek());
    println!();

    // Demonstrate with strings
    println!("=== String Stack ===");
    let mut string_stack = Stack::new();
    string_stack.push(String::from("Rust"));
    string_stack.push(String::from("is"));
    string_stack.push(String::from("awesome"));
    println!("Stack: {}", string_stack);

    // Demonstrate iterator
    println!("\nIterating (LIFO order):");
    for item in string_stack {
        println!("  {}", item);
    }
}
```

Run:
```bash
cargo run
```

---

## 📦 Expected Repository Structure

Your repository should now contain all 12 labs:

```
is4010-labs-yourname/
├── lab01/ through lab08/  # Python labs
├── lab09/                 # Rust basics
├── lab10/                 # Ownership and borrowing
├── lab11/                 # Structuring code and data
└── week12/                 # Generics and traits ✓
    └── week12/
        ├── Cargo.toml
        ├── Cargo.lock
        └── src/
            └── main.rs    # Generic stack with Display and Iterator traits
```

This demonstrates your mastery of Rust's type system, from basic concepts to advanced generic programming.

---

## 🚨 Troubleshooting

**Common issues?** See the [Common Troubleshooting Guide](../resources/TROUBLESHOOTING.md) for general Rust, testing, and GitHub Actions problems.

**Lab 12-specific issues:**

### **Problem: "error[E0308]: mismatched types"**
- **Cause**: Generic type parameter T doesn't match expected concrete type
- **Solution**:
  - Check that your function signatures use `T` consistently
  - Make sure you're not mixing `T` with concrete types like `i32`
  - Example: `fn push(&mut self, item: T)` not `fn push(&mut self, item: i32)`

### **Problem: "error[E0277]: the trait bound `T: std::fmt::Display` is not satisfied"**
- **Cause**: Trying to use Display functionality without trait bound
- **Solution**:
  - Add trait bound: `impl<T: fmt::Display> fmt::Display for Stack<T>`
  - Import Display: `use std::fmt;`
  - Make sure ALL impl blocks that need Display have the bound

### **Problem: "error[E0599]: no method named `push` found"**
- **Cause**: Method is defined incorrectly or missing `&mut self`
- **Solution**:
  - Check signature: `pub fn push(&mut self, item: T)`
  - Make sure method is inside `impl<T> Stack<T>` block
  - Verify it's `pub` if calling from outside the module

### **Problem: "error[E0308]: expected struct `Stack`, found `Stack<_>`"**
- **Cause**: Type inference can't determine T
- **Solution**:
  - Specify the type explicitly: `let mut stack: Stack<i32> = Stack::new();`
  - Or push an item immediately so Rust can infer: `let mut stack = Stack::new(); stack.push(1);`

### **Problem: "error[E0382]: borrow of moved value"**
- **Cause**: Trying to use stack after it's been moved by into_iter()
- **Solution**:
  - `into_iter()` consumes the stack
  - Clone before iterating if you need to use it again: `stack.clone().into_iter()`
  - Or use references if you don't need to consume

### **Problem: "error[E0046]: not all trait items implemented"**
- **Cause**: Missing required methods in Iterator implementation
- **Solution**:
  - Iterator trait requires `fn next(&mut self) -> Option<Self::Item>`
  - Make sure you have BOTH `type Item = T;` and `fn next(...)`
  - Check the signature matches exactly

### **Problem: Tests compile but fail at runtime**
- **Cause**: Logic error in pop(), push(), or next() implementation
- **Solution**:
  - Add println! debugging: `println!("Stack: {:?}", self.items);`
  - Check your Vec operations: pop() removes from END, push() adds to END
  - Verify is_empty() logic

### **Problem: "error[E0369]: binary operation cannot be applied to type `T`"**
- **Cause**: Trying to compare or operate on T without trait bounds
- **Solution**:
  - For comparisons, add `T: PartialEq` bound
  - For arithmetic, add appropriate trait like `T: Add`
  - Example: `impl<T: PartialEq> Stack<T>`

### **Problem: "error: duplicate definitions with name `next`"**
- **Cause**: Implementing Iterator on both Stack and StackIterator
- **Solution**:
  - Implement Iterator ONLY on StackIterator
  - Implement IntoIterator on Stack to create StackIterator
  - Don't implement Iterator directly on Stack

### **Problem: "use of possibly-uninitialized variable"**
- **Cause**: Trying to use a value from pop() without checking Option
- **Solution**:
  - Always match on Option: `match stack.pop() { Some(v) => ..., None => ... }`
  - Or use if let: `if let Some(v) = stack.pop() { ... }`

### **Problem: "error[E0106]: missing lifetime specifier"**
- **Cause**: Returning references without lifetime annotations (advanced)
- **Solution**:
  - For this lab, avoid returning references
  - Return owned values (T) instead of &T
  - If you must use references, add lifetime: `impl<'a, T> ...`

### **Problem: "clippy warnings about Vec usage"**
- **Cause**: Clippy suggests is_empty() instead of len() == 0
- **Solution**:
  - Change `self.items.len() == 0` to `self.items.is_empty()`
  - Clippy warnings won't fail the build but good to fix

### **Problem: "trait `Display` is not implemented for `T`"**
- **Cause**: Trying to print T without Display bound
- **Solution**:
  - Add `where T: fmt::Display` to the impl block
  - Or use Debug trait instead: `where T: fmt::Debug` with `{:?}`

### **Problem: cargo test fails with "thread panicked"**
- **Cause**: Unwrap on None, assertion failure, or logic error
- **Solution**:
  - Read the panic message carefully - it shows the line number
  - Check your test assertions match expected behavior
  - Verify pop() returns None when stack is empty

### **Problem: "error[E0107]: wrong number of type arguments"**
- **Cause**: Missing <T> or extra type parameters
- **Solution**:
  - Stack creation: `Stack::<i32>::new()` or `Stack::new()` with type inference
  - Impl blocks: `impl<T> Stack<T>` with angle brackets
  - Make sure T is declared in impl before using in type

---

## 🤖 AI Assistance Strategy

Generics and traits are advanced Rust concepts - AI can help you understand and implement them effectively:

### When to Use AI

1. **Understanding generic syntax**: AI excels at explaining `impl<T>` and type parameters
2. **Debugging trait bound errors**: Get help with complex compiler errors about traits
3. **Learning trait implementations**: Ask AI to explain how traits work with examples
4. **Test case generation**: Generate comprehensive tests for generic types

### Example Prompts

1. **For generic basics**:
   ```
   "Explain Rust generics with a simple example. Why do I write `impl<T>` instead of just `impl`? What does the <T> mean?"
   ```

2. **For trait implementations**:
   ```
   "Show me how to implement the Display trait for a generic Stack<T>. Why do I need `T: fmt::Display` as a trait bound?"
   ```

3. **For Iterator pattern**:
   ```
   "I need to implement Iterator for my Stack<T>. Show me the complete pattern including the separate iterator struct and IntoIterator trait."
   ```

4. **For debugging trait errors**:
   ```
   "I'm getting 'the trait bound T: std::fmt::Display is not satisfied'. Here's my code: [paste]. How do I fix this?"
   ```

5. **For testing generics**:
   ```
   "Write comprehensive tests for a generic Stack that works with i32, String, and custom types. Include edge cases like empty stack."
   ```

6. **For understanding ownership with generics**:
   ```
   "When I call into_iter() on my Stack<T>, why can't I use the stack afterward? Explain ownership with generic types."
   ```

### Conversation Example: Generic Type Parameters

**You**: "I don't understand why I need to write `impl<T> Stack<T>` instead of just `impl Stack`. What's the difference?"

**AI**: "The `<T>` declares a type parameter for the implementation block. Here's why it's needed:

```rust
// This says: 'For ANY type T, implement these methods for Stack<T>'
impl<T> Stack<T> {
    pub fn new() -> Self {
        Stack { items: Vec::new() }
    }

    pub fn push(&mut self, item: T) {
        self.items.push(item);
    }
}
```

Without `impl<T>`, Rust wouldn't know what T is. The `<T>` makes T a generic parameter that can be any type."

**You**: "So when I create `Stack::<i32>::new()`, what's happening?"

**AI**: "Rust is instantiating the generic implementation with T=i32:

```rust
// You write:
let stack = Stack::<i32>::new();

// Rust treats it like:
impl Stack<i32> {
    pub fn new() -> Stack<i32> { ... }
    pub fn push(&mut self, item: i32) { ... }
}
```

It's like creating a specific version of Stack for integers!"

### Conversation Example: Trait Bounds

**You**: "Why do I need `T: fmt::Display` when implementing Display for Stack<T>?"

**AI**: "Because to display the Stack, you need to display each T inside it. Without the bound, Rust doesn't know if T can be displayed:

```rust
// This WON'T compile (no guarantee T has Display):
impl<T> fmt::Display for Stack<T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, \"{}\", item)  // ERROR: T might not have Display!
    }
}

// This WILL compile (T required to have Display):
impl<T: fmt::Display> fmt::Display for Stack<T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, \"{}\", item)  // OK: We know T has Display
    }
}
```

The bound `T: fmt::Display` says 'this implementation only works for types that implement Display'."

### Recommended Tools

- **[ChatGPT](https://chat.openai.com/)** - Excellent for explaining generics concepts and trait bounds
- **[Claude](https://claude.ai/)** - Great for debugging complex trait bound errors
- **[Gemini](https://gemini.google.com/)** - Helpful for understanding Iterator pattern
- **[GitHub Copilot](https://github.com/features/copilot)** - In-editor assistance for trait implementations

### When to Debug Yourself

- Simple syntax errors (rustc gives great messages)
- Missing semicolons or braces
- Type inference issues (try adding explicit types)
- Read the compiler suggestions (they're often correct!)

**Pro tip**: Rust's compiler errors for generics are very detailed. Read the full error message including notes and suggestions before asking AI!

---

## 📤 Submission

### Final checklist

- [ ] All 15+ tests passing
- [ ] `cargo build` compiles without warnings
- [ ] `cargo run` demonstrates stack with multiple types
- [ ] Display trait implemented
- [ ] Iterator trait implemented
- [ ] GitHub Actions CI/CD passing

### Submit your work

```bash
# From is4010-labs root
git add week12/
git commit -m "Complete Lab 12: Generic Stack Implementation"
git push origin main
```

Submit repository URL on Canvas:
```
https://github.com/yourusername/is4010-labs
```

---

## 🎯 Grading rubric

| Category | Points |
|----------|--------|
| Generic Stack implementation (all methods) | 3 |
| Display trait implementation | 1 |
| Iterator trait implementation | 2 |
| Comprehensive tests (15+, all passing) | 2 |
| Code organization and documentation | 1 |
| GitHub Actions CI/CD passing | 1 |
| **Total** | **10** |

**Deductions:**
- -1: Compiler warnings
- -2: Tests failing
- -3: Missing trait implementations
- -5: Code doesn't compile

---

## 📚 Resources

**Official Documentation:**
- [Rust Book - Generic Types](https://doc.rust-lang.org/book/ch10-01-syntax.html)
- [Rust Book - Traits](https://doc.rust-lang.org/book/ch10-02-traits.html)
- [Rust Book - Advanced Traits](https://doc.rust-lang.org/book/ch19-03-advanced-traits.html)
- [Display Trait](https://doc.rust-lang.org/std/fmt/trait.Display.html)
- [Iterator Trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

---

**Remember:** This lab demonstrates the power of generic programming - write code once that works with any type! The Stack you build here uses the same generics concepts found throughout Rust's standard library (Vec, HashMap, Option, Result, etc.).

**Good luck!** 🦀
