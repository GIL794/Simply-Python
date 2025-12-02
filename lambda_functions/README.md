# Python Lambda Functions

## Overview

This module demonstrates **Python lambda functions**, small anonymous functions that are useful for simple operations. Lambda functions are a powerful tool for writing concise and readable code.

## What You'll Learn

1. **Basic Lambda Syntax** - How to define lambda functions
2. **Lambda with Built-ins** - Using lambda with map(), filter(), sorted()
3. **Custom Sorting** - Sorting collections with lambda keys
4. **Dictionary Operations** - Working with dictionaries using lambdas
5. **Lambda vs def** - When to use lambda vs regular functions

## Prerequisites

- Python 3.7 or higher
- Basic understanding of functions
- Familiarity with lists and loops

## What is a Lambda Function?

A lambda function is a small, anonymous function defined with the `lambda` keyword:

```python
# Syntax
lambda arguments: expression

# Example
add = lambda x, y: x + y
result = add(5, 3)  # Returns 8
```

## Quick Start

Run the demonstration:

```bash
python lambda_functions.py
```

## Code Examples

### 1. Basic Lambda

```python
# Single argument
square = lambda x: x ** 2
print(square(4))  # 16

# Multiple arguments
add = lambda x, y: x + y
print(add(2, 3))  # 5

# No arguments
greet = lambda: "Hello!"
print(greet())  # Hello!
```

### 2. With map() and filter()

```python
numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
# Result: [2, 4, 6, 8, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Result: [2, 4]
```

### 3. Custom Sorting

```python
words = ["apple", "pie", "banana"]

# Sort by length
by_length = sorted(words, key=lambda w: len(w))
# Result: ['pie', 'apple', 'banana']

# Sort by last character
by_last = sorted(words, key=lambda w: w[-1])
# Result: ['banana', 'apple', 'pie']
```

## When to Use Lambda

| Use Lambda | Use def |
|------------|---------|
| Simple one-line operations | Complex logic |
| As arguments to map/filter/sorted | Reusable functions |
| Quick inline calculations | Functions needing docstrings |
| Short callback functions | Multi-line operations |

## Best Practices

1. **Keep it simple** - If logic is complex, use a regular function
2. **One expression only** - Lambda can only contain one expression
3. **Readability first** - Don't sacrifice clarity for brevity
4. **Consider list comprehensions** - Often more readable than map/lambda

## Common Patterns

### Sorting Dictionaries

```python
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted_by_age = sorted(people, key=lambda p: p["age"])
```

### Getting Max/Min by Key

```python
oldest = max(people, key=lambda p: p["age"])
youngest = min(people, key=lambda p: p["age"])
```

### Conditional Expression

```python
# Lambda with conditional
classify = lambda x: "even" if x % 2 == 0 else "odd"
print(classify(4))  # "even"
```

## Further Reading

- [Python Documentation - Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Python Documentation - map()](https://docs.python.org/3/library/functions.html#map)
- [Python Documentation - filter()](https://docs.python.org/3/library/functions.html#filter)

## License

This code is released under the MIT License. See the [LICENSE](LICENSE) file for details.
