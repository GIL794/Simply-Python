# Python List Comprehensions

## Overview

This module demonstrates **Python list comprehensions**, a concise and readable way to create lists. List comprehensions are one of Python's most loved features for their elegance and efficiency.

## What You'll Learn

1. **Basic Syntax** - Creating lists with comprehensions
2. **Filtering** - Using conditions to filter items
3. **If-Else Expressions** - Conditional transformations
4. **Nested Comprehensions** - Working with multi-dimensional data
5. **String Processing** - Using comprehensions with strings

## Prerequisites

- Python 3.7 or higher
- Basic understanding of lists and loops
- Familiarity with conditional statements

## What is a List Comprehension?

A list comprehension is a compact way to create a list by applying an expression to each item in an iterable:

```python
# Syntax
[expression for item in iterable]

# Example
squares = [x ** 2 for x in range(5)]
# Result: [0, 1, 4, 9, 16]
```

## Quick Start

Run the demonstration:

```bash
python list_comprehensions.py
```

## Code Examples

### 1. Basic Comprehension

```python
# Create a list of squares
squares = [x ** 2 for x in range(5)]
# Result: [0, 1, 4, 9, 16]

# Convert to uppercase
names = ["alice", "bob"]
upper = [name.upper() for name in names]
# Result: ["ALICE", "BOB"]
```

### 2. With Filtering

```python
numbers = [1, 2, 3, 4, 5, 6]

# Keep only even numbers
evens = [x for x in numbers if x % 2 == 0]
# Result: [2, 4, 6]

# Filter and transform
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
# Result: [4, 16, 36]
```

### 3. If-Else Expression

```python
numbers = [1, 2, 3, 4, 5]

# Replace odd with 0
result = [x if x % 2 == 0 else 0 for x in numbers]
# Result: [0, 2, 0, 4, 0]

# Label as even/odd
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
# Result: ["odd", "even", "odd", "even", "odd"]
```

### 4. Nested Comprehension

```python
# Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
# Result: [1, 2, 3, 4, 5, 6]

# Create a 2D list
grid = [[i * j for j in range(3)] for i in range(3)]
# Result: [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

## Comparison: Loop vs Comprehension

| For Loop | List Comprehension |
|----------|-------------------|
| More verbose | Concise one-liner |
| Multiple lines | Single expression |
| Explicit append | Implicit list creation |
| Always readable | Best for simple cases |

```python
# For loop
result = []
for x in range(5):
    result.append(x ** 2)

# List comprehension
result = [x ** 2 for x in range(5)]
```

## Best Practices

1. **Keep it simple** - If comprehension is complex, use a for loop
2. **One line rule** - If it doesn't fit on one line, consider alternatives
3. **Readability matters** - Clear code is better than clever code
4. **Avoid side effects** - Comprehensions are for creating lists, not actions

## Other Comprehension Types

Python also supports:

```python
# Set comprehension
unique_squares = {x ** 2 for x in [1, 2, 2, 3]}
# Result: {1, 4, 9}

# Dictionary comprehension
squares_dict = {x: x ** 2 for x in range(4)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9}

# Generator expression (uses parentheses)
squares_gen = (x ** 2 for x in range(5))
# Creates a generator, not a list
```

## Further Reading

- [Python Documentation - List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [PEP 202 - List Comprehensions](https://www.python.org/dev/peps/pep-0202/)

## License

This code is released under the MIT License. See the [LICENSE](LICENSE) file for details.
