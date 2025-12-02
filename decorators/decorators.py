"""
Python Decorators: Advanced Programming Concepts

This module demonstrates various decorator patterns in Python,
including function decorators, decorators with arguments,
class decorators, and practical use cases.

Author: Simply-Python Contributors
License: MIT
"""

import functools
import time
from typing import Callable, Any


# =============================================================================
# SECTION 1: Basic Function Decorator
# =============================================================================

def simple_decorator(func: Callable) -> Callable:
    """
    A simple decorator that wraps a function and prints messages
    before and after the function execution.
    
    This is the most basic form of a decorator. It takes a function
    as input and returns a new function that adds behavior.
    
    Args:
        func: The function to be decorated
        
    Returns:
        A wrapper function that adds pre/post execution messages
    """
    @functools.wraps(func)  # Preserves the original function's metadata
    def wrapper(*args, **kwargs):
        print(f"[INFO] Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[INFO] Function {func.__name__} completed")
        return result
    return wrapper


@simple_decorator
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"


# =============================================================================
# SECTION 2: Timing Decorator
# =============================================================================

def timing_decorator(func: Callable) -> Callable:
    """
    A decorator that measures the execution time of a function.
    
    This is extremely useful for profiling and performance optimization.
    It prints the time taken by the decorated function to execute.
    
    Args:
        func: The function to be timed
        
    Returns:
        A wrapper function that times the execution
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"[TIMING] {func.__name__} took {execution_time:.6f} seconds")
        return result
    return wrapper


@timing_decorator
def slow_function(n: int) -> int:
    """
    A deliberately slow function for demonstration.
    Calculates the sum of squares from 1 to n.
    """
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total


# =============================================================================
# SECTION 3: Decorator with Arguments
# =============================================================================

def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    A decorator factory that retries a function if it raises an exception.
    
    This pattern is called a "decorator factory" because it returns
    a decorator. It allows you to pass arguments to customize the
    decorator's behavior.
    
    Args:
        max_attempts: Maximum number of retry attempts (default: 3)
        delay: Delay between retries in seconds (default: 1.0)
        
    Returns:
        A decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"[RETRY] Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            
            # If all attempts fail, raise the last exception
            raise last_exception
        
        return wrapper
    return decorator


@retry(max_attempts=3, delay=0.5)
def unstable_operation(success_rate: float = 0.5) -> str:
    """
    Simulates an unstable operation that might fail.
    Used to demonstrate the retry decorator.
    """
    import random
    if random.random() > success_rate:
        raise ValueError("Operation failed randomly!")
    return "Success!"


# =============================================================================
# SECTION 4: Memoization Decorator (Caching)
# =============================================================================

def memoize(func: Callable) -> Callable:
    """
    A memoization decorator that caches function results.
    
    Memoization is an optimization technique that stores the results
    of expensive function calls and returns the cached result when
    the same inputs occur again.
    
    This is particularly useful for:
    - Recursive functions (like Fibonacci)
    - Functions with expensive computations
    - Functions that are called repeatedly with the same arguments
    
    Args:
        func: The function to be memoized
        
    Returns:
        A wrapper function with caching capability
    """
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        # Create a cache key from the arguments
        if args not in cache:
            cache[args] = func(*args)
            print(f"[CACHE] Computing and caching result for {func.__name__}{args}")
        else:
            print(f"[CACHE] Using cached result for {func.__name__}{args}")
        return cache[args]
    
    return wrapper


@memoize
def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.
    
    Without memoization, this would have exponential time complexity.
    With memoization, it becomes linear!
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# =============================================================================
# SECTION 5: Class Decorator
# =============================================================================

def singleton(cls):
    """
    A class decorator that implements the Singleton pattern.
    
    The Singleton pattern ensures that a class has only one instance
    and provides a global point of access to it.
    
    This is useful for:
    - Configuration managers
    - Database connections
    - Logging objects
    
    Args:
        cls: The class to be made into a singleton
        
    Returns:
        A wrapper function that returns the single instance
    """
    instances = {}
    
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            print(f"[SINGLETON] Created new instance of {cls.__name__}")
        else:
            print(f"[SINGLETON] Returning existing instance of {cls.__name__}")
        return instances[cls]
    
    return get_instance


@singleton
class DatabaseConnection:
    """
    A sample database connection class demonstrating the singleton pattern.
    """
    
    def __init__(self, host: str = "localhost", port: int = 5432):
        self.host = host
        self.port = port
        self.connected = False
    
    def connect(self) -> None:
        """Simulate connecting to the database."""
        self.connected = True
        print(f"[DB] Connected to {self.host}:{self.port}")
    
    def disconnect(self) -> None:
        """Simulate disconnecting from the database."""
        self.connected = False
        print(f"[DB] Disconnected from {self.host}:{self.port}")


# =============================================================================
# SECTION 6: Decorator for Input Validation
# =============================================================================

def validate_types(**expected_types):
    """
    A decorator that validates the types of function arguments.
    
    This is useful for adding runtime type checking to functions,
    especially when working with dynamic data or external inputs.
    
    Args:
        **expected_types: Keyword arguments mapping parameter names to types
        
    Returns:
        A decorator function
        
    Example:
        @validate_types(x=int, y=int)
        def add(x, y):
            return x + y
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function parameter names
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # Check each argument against expected type
            for param_name, expected_type in expected_types.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"Argument '{param_name}' must be {expected_type.__name__}, "
                            f"got {type(value).__name__}"
                        )
            
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


@validate_types(x=int, y=int)
def add_numbers(x: int, y: int) -> int:
    """Add two integers together with type validation."""
    return x + y


# =============================================================================
# MAIN: Demonstration of All Decorators
# =============================================================================

def main():
    """
    Main function demonstrating all decorator examples.
    """
    print("=" * 60)
    print("PYTHON DECORATORS DEMONSTRATION")
    print("=" * 60)
    
    # 1. Simple Decorator
    print("\n--- 1. Simple Decorator ---")
    result = greet("Python Developer")
    print(f"Result: {result}")
    
    # 2. Timing Decorator
    print("\n--- 2. Timing Decorator ---")
    result = slow_function(10000)
    print(f"Sum of squares: {result}")
    
    # 3. Retry Decorator
    print("\n--- 3. Retry Decorator ---")
    try:
        result = unstable_operation(success_rate=0.8)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"All retries failed: {e}")
    
    # 4. Memoization Decorator
    print("\n--- 4. Memoization Decorator ---")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"fibonacci(10) again = {fibonacci(10)}")  # Uses cache
    
    # 5. Singleton Decorator
    print("\n--- 5. Singleton Decorator ---")
    db1 = DatabaseConnection("localhost", 5432)
    db2 = DatabaseConnection("otherhost", 3306)  # Returns same instance!
    print(f"db1 is db2: {db1 is db2}")  # True - same instance
    db1.connect()
    
    # 6. Type Validation Decorator
    print("\n--- 6. Type Validation Decorator ---")
    try:
        result = add_numbers(5, 10)
        print(f"add_numbers(5, 10) = {result}")
        
        # This will raise a TypeError
        result = add_numbers("5", 10)
    except TypeError as e:
        print(f"Type error caught: {e}")
    
    print("\n" + "=" * 60)
    print("END OF DEMONSTRATION")
    print("=" * 60)


if __name__ == "__main__":
    main()
