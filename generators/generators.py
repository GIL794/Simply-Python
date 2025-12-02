"""
Python Generators and Iterators: Advanced Programming Concepts

This module demonstrates various generator patterns in Python,
including generator functions, generator expressions, custom iterators,
and practical use cases for memory-efficient data processing.

Author: Simply-Python Contributors
License: MIT
"""

from typing import Iterator, Generator, Any, List
import sys


# =============================================================================
# SECTION 1: Basic Generator Function
# =============================================================================

def count_up_to(max_value: int) -> Generator[int, None, None]:
    """
    A simple generator that yields numbers from 1 up to max_value.
    
    Generators are special functions that return an iterator.
    Instead of returning all values at once (like a list),
    they yield one value at a time, making them memory-efficient.
    
    The 'yield' keyword pauses the function and saves its state.
    When next() is called, it resumes from where it left off.
    
    Args:
        max_value: The maximum number to count up to
        
    Yields:
        Integers from 1 to max_value
    """
    count = 1
    while count <= max_value:
        yield count  # Pause here and return the value
        count += 1   # Resume here on next call


def demonstrate_basic_generator():
    """Demonstrate basic generator usage."""
    print("--- Basic Generator ---")
    
    # Create a generator object
    counter = count_up_to(5)
    print(f"Generator object: {counter}")
    
    # Iterate manually using next()
    print(f"First value: {next(counter)}")
    print(f"Second value: {next(counter)}")
    
    # Iterate remaining values with for loop
    print("Remaining values:", end=" ")
    for num in counter:
        print(num, end=" ")
    print()


# =============================================================================
# SECTION 2: Generator Expression
# =============================================================================

def compare_list_vs_generator():
    """
    Compare memory usage between list comprehension and generator expression.
    
    Generator expressions look similar to list comprehensions but use
    parentheses () instead of brackets []. They don't create the entire
    list in memory - they generate values on-the-fly.
    """
    print("\n--- List vs Generator Memory Comparison ---")
    
    # List comprehension - creates entire list in memory
    numbers_list = [x ** 2 for x in range(1000)]
    list_size = sys.getsizeof(numbers_list)
    
    # Generator expression - generates values on demand
    numbers_gen = (x ** 2 for x in range(1000))
    gen_size = sys.getsizeof(numbers_gen)
    
    print(f"List comprehension size: {list_size:,} bytes")
    print(f"Generator expression size: {gen_size:,} bytes")
    print(f"Memory saved: {((list_size - gen_size) / list_size * 100):.1f}%")
    
    # Both produce the same results
    print(f"First 5 squares from generator: {[next(numbers_gen) for _ in range(5)]}")


# =============================================================================
# SECTION 3: Infinite Generator
# =============================================================================

def fibonacci_generator() -> Generator[int, None, None]:
    """
    An infinite generator for Fibonacci numbers.
    
    Infinite generators never stop yielding values.
    They're useful when you don't know in advance how many
    values you'll need.
    
    WARNING: Don't use list() on an infinite generator!
    Always use with a limiting condition.
    
    Yields:
        The next Fibonacci number in the sequence
    """
    a, b = 0, 1
    while True:  # Infinite loop
        yield a
        a, b = b, a + b  # Calculate next Fibonacci number


def demonstrate_infinite_generator():
    """Demonstrate infinite generator with limiting."""
    print("\n--- Infinite Fibonacci Generator ---")
    
    fib = fibonacci_generator()
    
    # Get first 10 Fibonacci numbers
    print("First 10 Fibonacci numbers:", end=" ")
    for _ in range(10):
        print(next(fib), end=" ")
    print()
    
    # Continue from where we left off
    print("Next 5 Fibonacci numbers:", end=" ")
    for _ in range(5):
        print(next(fib), end=" ")
    print()


# =============================================================================
# SECTION 4: Generator with send() - Coroutine Pattern
# =============================================================================

def accumulator() -> Generator[float, float, None]:
    """
    A generator that receives values and accumulates them.
    
    Generators can receive values using the send() method.
    This turns them into "coroutines" - functions that can
    both produce and receive data.
    
    The expression `value = yield total` does two things:
    1. Yields the current total to the caller
    2. Receives a new value when send() is called
    
    Yields:
        The running total
        
    Receives:
        A number to add to the total
    """
    total = 0.0
    while True:
        # yield returns total and receives new value
        value = yield total
        if value is not None:
            total += value


def demonstrate_send():
    """Demonstrate generator send() method."""
    print("\n--- Generator with send() ---")
    
    acc = accumulator()
    
    # Must call next() first to start the generator
    print(f"Initial total: {next(acc)}")
    
    # Send values and receive running total
    print(f"After sending 10: {acc.send(10)}")
    print(f"After sending 20: {acc.send(20)}")
    print(f"After sending 5: {acc.send(5)}")


# =============================================================================
# SECTION 5: Generator Pipeline
# =============================================================================

def read_numbers(data: List[int]) -> Generator[int, None, None]:
    """
    First stage: Read numbers from a data source.
    Simulates reading from a file or database.
    """
    for number in data:
        yield number


def filter_even(numbers: Iterator[int]) -> Generator[int, None, None]:
    """
    Second stage: Filter to keep only even numbers.
    """
    for num in numbers:
        if num % 2 == 0:
            yield num


def square(numbers: Iterator[int]) -> Generator[int, None, None]:
    """
    Third stage: Square each number.
    """
    for num in numbers:
        yield num ** 2


def demonstrate_pipeline():
    """
    Demonstrate generator pipeline for data processing.
    
    Generator pipelines connect multiple generators together.
    Data flows through each stage, being transformed as it goes.
    
    Benefits:
    - Memory efficient: only one item in memory at a time
    - Lazy evaluation: processing happens only when needed
    - Modular: each stage can be tested and reused independently
    """
    print("\n--- Generator Pipeline ---")
    
    # Sample data
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original data: {data}")
    
    # Create the pipeline
    pipeline = square(filter_even(read_numbers(data)))
    
    # Process the pipeline
    results = list(pipeline)
    print(f"After pipeline (even numbers squared): {results}")


# =============================================================================
# SECTION 6: Custom Iterator Class
# =============================================================================

class Range:
    """
    A custom iterator that mimics Python's range() function.
    
    To create a custom iterator, you need to implement:
    1. __iter__() - Returns the iterator object itself
    2. __next__() - Returns the next value or raises StopIteration
    
    This is the class-based approach to creating iterators.
    Generators are often simpler, but classes offer more control.
    """
    
    def __init__(self, start: int, stop: int = None, step: int = 1):
        """
        Initialize the Range iterator.
        
        Args:
            start: Starting value (or stop if stop is None)
            stop: Stopping value (exclusive)
            step: Step size between values
        """
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step
        self.current = self.start
    
    def __iter__(self):
        """
        Return the iterator object.
        Called when iteration begins.
        """
        return self
    
    def __next__(self) -> int:
        """
        Return the next value in the sequence.
        Raises StopIteration when the sequence is exhausted.
        """
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value


def demonstrate_custom_iterator():
    """Demonstrate custom iterator class."""
    print("\n--- Custom Iterator Class ---")
    
    # Use like range()
    print("Range(5):", list(Range(5)))
    print("Range(2, 8):", list(Range(2, 8)))
    print("Range(10, 0, -2):", list(Range(10, 0, -2)))


# =============================================================================
# SECTION 7: yield from - Delegating to Sub-generators
# =============================================================================

def flatten(nested_list: List) -> Generator[Any, None, None]:
    """
    Recursively flatten a nested list structure.
    
    The 'yield from' expression delegates to another iterable or generator.
    It's equivalent to: for item in iterable: yield item
    
    But 'yield from' is more efficient and handles edge cases
    like exceptions and send() properly.
    
    Args:
        nested_list: A potentially nested list structure
        
    Yields:
        Each non-list element from the nested structure
    """
    for item in nested_list:
        if isinstance(item, list):
            # Delegate to recursive call
            yield from flatten(item)
        else:
            yield item


def chain(*iterables) -> Generator[Any, None, None]:
    """
    Chain multiple iterables together.
    Similar to itertools.chain().
    
    Args:
        *iterables: Variable number of iterables to chain
        
    Yields:
        Each element from each iterable in order
    """
    for iterable in iterables:
        yield from iterable


def demonstrate_yield_from():
    """Demonstrate yield from delegation."""
    print("\n--- yield from Delegation ---")
    
    # Flatten nested list
    nested = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
    print(f"Nested list: {nested}")
    print(f"Flattened: {list(flatten(nested))}")
    
    # Chain iterables
    result = list(chain([1, 2], "ab", (3, 4)))
    print(f"Chained [1,2] + 'ab' + (3,4): {result}")


# =============================================================================
# SECTION 8: Generator for Large File Processing
# =============================================================================

def read_large_file_lines(filename: str) -> Generator[str, None, None]:
    """
    Read a large file line by line without loading it entirely into memory.
    
    This is a common real-world use case for generators.
    Reading a 10GB file with a list would crash most computers.
    With a generator, we only hold one line in memory at a time.
    
    Args:
        filename: Path to the file to read
        
    Yields:
        Each line from the file (stripped of whitespace)
    """
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


def process_csv_lazily(lines: Iterator[str]) -> Generator[dict, None, None]:
    """
    Process CSV data lazily, converting each line to a dictionary.
    
    This demonstrates how generators can be chained for
    memory-efficient data processing pipelines.
    
    Args:
        lines: Iterator of CSV lines (first line is header)
        
    Yields:
        Dictionary representing each row
    """
    # Get header from first line
    # Handle empty iterator case
    try:
        header = next(lines).split(',')
    except StopIteration:
        return  # Empty iterator, nothing to yield
    
    # Process remaining lines
    for line in lines:
        values = line.split(',')
        yield dict(zip(header, values))


def demonstrate_file_processing():
    """Demonstrate file processing with generators (simulated)."""
    print("\n--- Large File Processing Pattern ---")
    
    # Simulate CSV data (in real use, this would be file lines)
    csv_data = [
        "name,age,city",
        "Alice,30,New York",
        "Bob,25,Los Angeles",
        "Charlie,35,Chicago"
    ]
    
    # Process lazily
    records = process_csv_lazily(iter(csv_data))
    
    print("Processing CSV records one at a time:")
    for record in records:
        print(f"  {record}")


# =============================================================================
# MAIN: Demonstration of All Generator Concepts
# =============================================================================

def main():
    """
    Main function demonstrating all generator examples.
    """
    print("=" * 60)
    print("PYTHON GENERATORS AND ITERATORS DEMONSTRATION")
    print("=" * 60)
    
    demonstrate_basic_generator()
    compare_list_vs_generator()
    demonstrate_infinite_generator()
    demonstrate_send()
    demonstrate_pipeline()
    demonstrate_custom_iterator()
    demonstrate_yield_from()
    demonstrate_file_processing()
    
    print("\n" + "=" * 60)
    print("END OF DEMONSTRATION")
    print("=" * 60)


if __name__ == "__main__":
    main()
