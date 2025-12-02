# Python Context Managers

## Overview

This module demonstrates **Python context managers**, a powerful feature for resource management and clean-up code. Context managers ensure that resources are properly acquired and released, even when exceptions occur.

## What You'll Learn

1. **Basic Context Managers** - The `__enter__` and `__exit__` protocol
2. **Timer Context Manager** - Measuring code block execution time
3. **@contextmanager Decorator** - Creating context managers from generators
4. **Exception Handling** - Suppressing and handling exceptions
5. **Transaction Pattern** - Commit/rollback logic
6. **Reentrant Locks** - Nested context manager usage
7. **ExitStack** - Dynamic context manager management
8. **Async Context Managers** - For asynchronous code

## Prerequisites

- Python 3.7 or higher
- Understanding of classes and exception handling
- Familiarity with the `with` statement

## Why Use Context Managers?

| Without Context Manager | With Context Manager |
|------------------------|---------------------|
| Manual resource cleanup | Automatic cleanup |
| Must remember try/finally | Built-in safety |
| Easy to forget cleanup | Impossible to forget |
| Verbose code | Clean, readable code |
| Exceptions may skip cleanup | Always runs cleanup |

## Quick Start

Run the demonstration:

```bash
python context_managers.py
```

## Code Examples

### 1. Basic Context Manager Class

```python
class FileManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False  # Don't suppress exceptions

# Usage
with FileManager('data.txt', 'w') as f:
    f.write('Hello, World!')
# File is automatically closed
```

### 2. Using @contextmanager Decorator

```python
from contextlib import contextmanager

@contextmanager
def timer(description):
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{description}: {elapsed:.2f}s")

# Usage
with timer("Data processing"):
    process_data()
```

### 3. Suppressing Exceptions

```python
from contextlib import suppress

# Built-in way
with suppress(FileNotFoundError):
    os.remove('nonexistent.txt')

# Custom implementation
class SuppressExceptions:
    def __init__(self, *exceptions):
        self.exceptions = exceptions
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self.exceptions)
```

### 4. Transaction Pattern

```python
class Transaction:
    def __enter__(self):
        self.begin()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.commit()
        else:
            self.rollback()
        return False

with Transaction() as txn:
    txn.execute("UPDATE users SET active = true")
    # Commits on success, rolls back on exception
```

## The `__exit__` Method

The `__exit__` method receives three arguments about any exception:

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    # exc_type: Exception class (e.g., ValueError)
    # exc_val: Exception instance (e.g., ValueError("invalid"))
    # exc_tb: Traceback object
    
    if exc_type is None:
        print("No exception occurred")
    else:
        print(f"Exception: {exc_type.__name__}: {exc_val}")
    
    # Return True to suppress the exception
    # Return False to propagate it
    return False
```

## Built-in Context Managers

Python provides many built-in context managers:

```python
# File handling
with open('file.txt') as f:
    content = f.read()

# Locking
with threading.Lock():
    shared_resource.modify()

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    # Directory is deleted after

# Decimal precision
with decimal.localcontext() as ctx:
    ctx.prec = 50
    # High precision calculations
```

## contextlib Utilities

```python
from contextlib import (
    contextmanager,     # Decorator for generator-based context managers
    suppress,           # Suppress specified exceptions
    redirect_stdout,    # Redirect stdout
    ExitStack,          # Manage multiple context managers
    closing,            # Call close() on exit
    nullcontext,        # No-op context manager
)
```

## Best Practices

1. **Always implement cleanup** - Use `finally` in `@contextmanager` functions
2. **Don't suppress exceptions blindly** - Be specific about what you suppress
3. **Keep context managers focused** - One resource per context manager
4. **Use ExitStack for dynamic resources** - When count is determined at runtime
5. **Document exception handling** - Clarify what happens on exceptions

## Common Use Cases

| Use Case | Example |
|----------|---------|
| File handling | Open, read/write, close |
| Database transactions | Begin, commit/rollback |
| Locking | Acquire, use, release |
| Timing | Start, measure, report |
| Configuration | Set, use, restore |
| Connection pools | Get, use, return |
| Temporary changes | Apply, use, revert |

## Further Reading

- [PEP 343 - The "with" Statement](https://www.python.org/dev/peps/pep-0343/)
- [contextlib Documentation](https://docs.python.org/3/library/contextlib.html)
- [Python Documentation - Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)

## License

This code is released under the MIT License. See the [LICENSE](LICENSE) file for details.
