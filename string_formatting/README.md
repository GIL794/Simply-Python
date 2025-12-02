# Python String Formatting

## Overview

This module demonstrates **Python string formatting**, essential for creating readable output and formatted text. Learn to use f-strings, the format() method, and various formatting options.

## What You'll Learn

1. **F-Strings** - Modern, fast, and readable string formatting
2. **Number Formatting** - Decimals, thousands separators, percentages
3. **Text Alignment** - Left, right, and center alignment with padding
4. **format() Method** - Traditional formatting approach
5. **Practical Examples** - Real-world formatting patterns

## Prerequisites

- Python 3.7 or higher
- Basic understanding of strings and variables

## What are F-Strings?

F-strings (formatted string literals) are the recommended way to format strings in Python 3.6+:

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 30 years old.
```

## Quick Start

Run the demonstration:

```bash
python string_formatting.py
```

## Code Examples

### 1. Basic F-Strings

```python
name = "Bob"
score = 95

# Variable insertion
print(f"Player: {name}")

# Expressions
print(f"Score doubled: {score * 2}")

# Method calls
print(f"Uppercase: {name.upper()}")
```

### 2. Number Formatting

```python
pi = 3.14159
big = 1234567
ratio = 0.856

# Decimal places
print(f"{pi:.2f}")      # 3.14

# Thousands separator
print(f"{big:,}")       # 1,234,567

# Percentage
print(f"{ratio:.1%}")   # 85.6%

# Zero padding
print(f"{42:05d}")      # 00042
```

### 3. Text Alignment

```python
text = "Hi"

# Width of 10 characters
print(f"|{text:<10}|")  # Left:   |Hi        |
print(f"|{text:>10}|")  # Right:  |        Hi|
print(f"|{text:^10}|")  # Center: |    Hi    |

# Custom fill character
print(f"|{text:-^10}|") # |----Hi----|
```

### 4. Format Specifiers

| Specifier | Description | Example |
|-----------|-------------|---------|
| `.2f` | 2 decimal places | `3.14` |
| `,` | Thousands separator | `1,000` |
| `.1%` | Percentage | `85.6%` |
| `05d` | Zero-padded integer | `00042` |
| `<10` | Left align, width 10 | `text      ` |
| `>10` | Right align, width 10 | `      text` |
| `^10` | Center, width 10 | `   text   ` |

## Comparison: Formatting Methods

```python
name = "Alice"
age = 30

# F-string (recommended)
f"Name: {name}, Age: {age}"

# format() method
"Name: {}, Age: {}".format(name, age)

# %-formatting (old style)
"Name: %s, Age: %d" % (name, age)
```

## Best Practices

1. **Use f-strings** - They're the most readable and fastest option
2. **Keep expressions simple** - Complex logic should be outside the f-string
3. **Use format specs wisely** - They improve readability for numbers
4. **Be consistent** - Stick to one formatting style in your project

## Common Patterns

### Tables

```python
data = [("Apple", 1.50), ("Banana", 0.75)]
for item, price in data:
    print(f"{item:<10} ${price:>5.2f}")
# Apple      $ 1.50
# Banana     $ 0.75
```

### Date Formatting

```python
day, month, year = 5, 12, 2024
print(f"{day:02d}/{month:02d}/{year}")
# 05/12/2024
```

### Debug Output (Python 3.8+)

```python
x = 10
y = 20
print(f"{x=}, {y=}, {x+y=}")
# x=10, y=20, x+y=30
```

## Further Reading

- [Python Documentation - f-strings](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting)
- [PEP 498 - Literal String Interpolation](https://www.python.org/dev/peps/pep-0498/)
- [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language)

## License

This code is released under the MIT License. See the [LICENSE](LICENSE) file for details.
