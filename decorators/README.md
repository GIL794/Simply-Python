# Python Decorators

## Overview

This module demonstrates **Python decorators**, one of the most powerful and elegant features for advanced Python programming. Decorators allow you to modify or extend the behavior of functions and classes without directly changing their source code.

## What You'll Learn

1. **Basic Function Decorators** - How to wrap functions to add behavior
2. **Timing Decorators** - Measuring function execution time
3. **Decorators with Arguments** - Creating flexible, parameterized decorators
4. **Memoization** - Caching function results for performance
5. **Class Decorators** - Implementing patterns like Singleton
6. **Input Validation** - Runtime type checking with decorators

## Prerequisites

- Python 3.7 or higher
- Basic understanding of functions and classes
- Familiarity with `*args` and `**kwargs`

## How Decorators Work

A decorator is essentially a function that takes another function as input and returns a new function that usually extends the original function's behavior.

```python
@my_decorator
def my_function():
    pass

# Is equivalent to:
def my_function():
    pass
my_function = my_decorator(my_function)
```

## Quick Start

Run the demonstration:

```bash
python decorators.py
```

## Code Examples

### 1. Basic Decorator

```python
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@simple_decorator
def greet(name):
    return f"Hello, {name}!"
```

### 2. Decorator with Arguments

```python
def retry(max_attempts=3, delay=1.0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
        return wrapper
    return decorator

@retry(max_attempts=5, delay=2.0)
def fetch_data():
    # Your code here
    pass
```

### 3. Memoization (Caching)

```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

## Best Practices

1. **Use `functools.wraps`** - Preserves the original function's metadata (name, docstring, etc.)

2. **Keep decorators focused** - Each decorator should do one thing well

3. **Handle `*args` and `**kwargs`** - Make decorators work with any function signature

4. **Document your decorators** - Clearly explain what behavior they add

5. **Consider performance** - Decorators add overhead; use wisely in performance-critical code

## Use Cases

| Decorator Type | Use Case |
|---------------|----------|
| Logging | Track function calls and parameters |
| Timing | Profile performance |
| Caching | Optimize repeated computations |
| Authentication | Check user permissions |
| Retry | Handle transient failures |
| Validation | Verify input types/values |
| Rate Limiting | Control API request frequency |

## Further Reading

- [PEP 318 - Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)
- [PEP 3129 - Class Decorators](https://www.python.org/dev/peps/pep-3129/)
- [Python Documentation - Decorators](https://docs.python.org/3/glossary.html#term-decorator)

## License

This code is released under the MIT License. See the [LICENSE](LICENSE) file for details.
