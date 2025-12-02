# Python Generators and Iterators

## Overview

This module demonstrates **Python generators and iterators**, essential tools for memory-efficient programming. Generators allow you to work with large datasets and infinite sequences without loading everything into memory at once.

## What You'll Learn

1. **Basic Generators** - The `yield` keyword and how generators work
2. **Generator Expressions** - Compact syntax for simple generators
3. **Infinite Generators** - Creating sequences that never end
4. **Coroutine Pattern** - Sending values to generators with `send()`
5. **Generator Pipelines** - Chaining generators for data processing
6. **Custom Iterators** - Creating iterator classes with `__iter__` and `__next__`
7. **yield from** - Delegating to sub-generators
8. **File Processing** - Memory-efficient large file handling

## Prerequisites

- Python 3.7 or higher
- Understanding of functions and loops
- Familiarity with list comprehensions

## Why Use Generators?

| Feature | List | Generator |
|---------|------|-----------|
| Memory Usage | Stores all items | Stores one item |
| Creation Time | Creates all items upfront | Creates items on-demand |
| Access Pattern | Random access | Sequential access |
| Reusability | Can iterate multiple times | Single iteration |
| Infinite Sequences | Not possible | Possible |

## Quick Start

Run the demonstration:

```bash
python generators.py
```

## Code Examples

### 1. Basic Generator

```python
def count_up_to(n):
    """Yields numbers from 1 to n."""
    count = 1
    while count <= n:
        yield count
        count += 1

# Usage
for num in count_up_to(5):
    print(num)  # Prints 1, 2, 3, 4, 5
```

### 2. Generator Expression

```python
# List comprehension (creates entire list)
squares_list = [x**2 for x in range(1000000)]

# Generator expression (creates values on-demand)
squares_gen = (x**2 for x in range(1000000))

# Generator uses minimal memory!
```

### 3. Infinite Generator

```python
def fibonacci():
    """Infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 Fibonacci numbers
fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
```

### 4. Generator Pipeline

```python
def read_data(data):
    for item in data:
        yield item

def filter_valid(items):
    for item in items:
        if item.is_valid():
            yield item

def transform(items):
    for item in items:
        yield item.transform()

# Chain together
pipeline = transform(filter_valid(read_data(raw_data)))

for result in pipeline:
    process(result)
```

## Key Concepts

### The `yield` Keyword

- `yield` pauses the function and returns a value
- The function remembers its state
- `next()` resumes execution until the next `yield`

### Generator vs Iterator

- **Iterator**: An object with `__iter__()` and `__next__()` methods
- **Generator**: A function that uses `yield` (automatically creates an iterator)
- All generators are iterators, but not all iterators are generators

### The `yield from` Statement

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)  # Delegate to sub-generator
        else:
            yield item
```

## Best Practices

1. **Use generators for large data** - When working with files or APIs
2. **Prefer generator expressions** - For simple transformations
3. **Chain generators** - Create modular, reusable pipelines
4. **Remember single-use** - Generators can only be iterated once
5. **Use `itertools`** - Python's built-in library for common patterns

## Common Patterns

### Reading Large Files

```python
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
```

### Batching Data

```python
def batch(iterable, size):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch
```

### Window Sliding

```python
from collections import deque

def sliding_window(iterable, size):
    window = deque(maxlen=size)
    for item in iterable:
        window.append(item)
        if len(window) == size:
            yield tuple(window)
```

## Related Python Libraries

- **itertools** - Efficient iterator building blocks
- **more-itertools** - Extended iterator utilities
- **toolz** - Functional programming utilities

## Further Reading

- [PEP 255 - Simple Generators](https://www.python.org/dev/peps/pep-0255/)
- [PEP 342 - Coroutines via Enhanced Generators](https://www.python.org/dev/peps/pep-0342/)
- [PEP 380 - Syntax for Delegating to a Subgenerator](https://www.python.org/dev/peps/pep-0380/)

## License

This code is released under the MIT License. See the [LICENSE](LICENSE) file for details.
