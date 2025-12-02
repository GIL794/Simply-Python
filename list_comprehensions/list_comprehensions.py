"""
Python List Comprehensions: Simple Programming Concepts

This module demonstrates list comprehensions in Python,
including basic usage, filtering, nested comprehensions,
and practical examples.

Author: Simply-Python Contributors
License: MIT
"""


# =============================================================================
# SECTION 1: Basic List Comprehension
# =============================================================================

def demonstrate_basic_comprehension():
    """
    Demonstrate basic list comprehension syntax.
    
    List comprehensions provide a concise way to create lists.
    They consist of brackets containing an expression followed
    by a for clause.
    
    Syntax: [expression for item in iterable]
    """
    print("--- Basic List Comprehension ---")
    
    # Traditional for loop approach
    squares_loop = []
    for x in range(5):
        squares_loop.append(x ** 2)
    print(f"Using for loop: {squares_loop}")
    
    # List comprehension approach (much cleaner!)
    squares_comp = [x ** 2 for x in range(5)]
    print(f"Using comprehension: {squares_comp}")
    
    # Creating a list of strings
    names = ["alice", "bob", "charlie"]
    upper_names = [name.upper() for name in names]
    print(f"Uppercase names: {upper_names}")


# =============================================================================
# SECTION 2: List Comprehension with Condition
# =============================================================================

def demonstrate_conditional_comprehension():
    """
    Demonstrate list comprehension with filtering conditions.
    
    You can add an if clause to filter items.
    Syntax: [expression for item in iterable if condition]
    """
    print("\n--- Conditional List Comprehension ---")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Get only even numbers
    evens = [x for x in numbers if x % 2 == 0]
    print(f"Even numbers: {evens}")
    
    # Get numbers greater than 5
    greater_than_5 = [x for x in numbers if x > 5]
    print(f"Numbers > 5: {greater_than_5}")
    
    # Combine transformation and filtering
    squared_evens = [x ** 2 for x in numbers if x % 2 == 0]
    print(f"Squared evens: {squared_evens}")


# =============================================================================
# SECTION 3: Conditional Expression in Comprehension
# =============================================================================

def demonstrate_if_else_comprehension():
    """
    Demonstrate using if-else expression in list comprehension.
    
    When you want to transform items differently based on a condition,
    use the if-else expression before the for clause.
    
    Syntax: [expr_if_true if condition else expr_if_false for item in iterable]
    """
    print("\n--- If-Else in Comprehension ---")
    
    numbers = [1, 2, 3, 4, 5]
    
    # Replace odd numbers with 0
    result = [x if x % 2 == 0 else 0 for x in numbers]
    print(f"Even or 0: {result}")
    
    # Label numbers as "even" or "odd"
    labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
    print(f"Labels: {labels}")
    
    # Transform based on condition
    modified = [x * 2 if x > 3 else x for x in numbers]
    print(f"Double if > 3: {modified}")


# =============================================================================
# SECTION 4: Nested List Comprehension
# =============================================================================

def demonstrate_nested_comprehension():
    """
    Demonstrate nested list comprehensions.
    
    You can nest for loops within a comprehension to work
    with multi-dimensional data.
    """
    print("\n--- Nested List Comprehension ---")
    
    # Flatten a 2D list
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [num for row in matrix for num in row]
    print(f"Original matrix: {matrix}")
    print(f"Flattened: {flat}")
    
    # Create a multiplication table
    table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"Multiplication table:")
    for row in table:
        print(f"  {row}")


# =============================================================================
# SECTION 5: Working with Strings
# =============================================================================

def demonstrate_string_comprehension():
    """
    Demonstrate list comprehension with strings.
    
    Strings are iterable, so you can use comprehensions
    to process characters or words.
    """
    print("\n--- String Comprehension ---")
    
    # Extract vowels from a string
    text = "Hello World"
    vowels = [char for char in text if char.lower() in "aeiou"]
    print(f"Vowels in '{text}': {vowels}")
    
    # Get word lengths
    sentence = "Python is awesome"
    words = sentence.split()
    lengths = [len(word) for word in words]
    print(f"Word lengths: {lengths}")
    
    # Capitalize first letter of each word
    words_cap = [word.capitalize() for word in words]
    print(f"Capitalized: {words_cap}")


# =============================================================================
# MAIN: Demonstration of All List Comprehension Concepts
# =============================================================================

def main():
    """
    Main function demonstrating all list comprehension examples.
    """
    print("=" * 60)
    print("PYTHON LIST COMPREHENSIONS DEMONSTRATION")
    print("=" * 60)
    
    demonstrate_basic_comprehension()
    demonstrate_conditional_comprehension()
    demonstrate_if_else_comprehension()
    demonstrate_nested_comprehension()
    demonstrate_string_comprehension()
    
    print("\n" + "=" * 60)
    print("END OF DEMONSTRATION")
    print("=" * 60)


if __name__ == "__main__":
    main()
