"""
Python Lambda Functions: Simple Programming Concepts

This module demonstrates lambda functions in Python,
including basic usage, common patterns, and practical examples.

Author: Simply-Python Contributors
License: MIT
"""


# =============================================================================
# SECTION 1: Basic Lambda Function
# =============================================================================

def demonstrate_basic_lambda():
    """
    Demonstrate basic lambda function syntax.
    
    Lambda functions are small, anonymous functions defined with
    the 'lambda' keyword. They can have any number of arguments
    but only one expression.
    
    Syntax: lambda arguments: expression
    """
    print("--- Basic Lambda Function ---")
    
    # A simple lambda that adds two numbers
    add = lambda x, y: x + y
    print(f"add(5, 3) = {add(5, 3)}")
    
    # Lambda with one argument
    square = lambda x: x ** 2
    print(f"square(4) = {square(4)}")
    
    # Lambda with no arguments
    greeting = lambda: "Hello, World!"
    print(f"greeting() = {greeting()}")


# =============================================================================
# SECTION 2: Lambda with Built-in Functions
# =============================================================================

def demonstrate_lambda_with_builtins():
    """
    Demonstrate using lambda with built-in functions like
    map(), filter(), and sorted().
    
    These combinations are very common in Python programming
    and make code more concise and readable.
    """
    print("\n--- Lambda with Built-in Functions ---")
    
    numbers = [1, 2, 3, 4, 5]
    
    # Using map() to apply a function to each element
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"Squared: {squared}")
    
    # Using filter() to keep elements that match a condition
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
    
    # Using sorted() with a custom key
    words = ["apple", "pie", "banana", "cat"]
    by_length = sorted(words, key=lambda w: len(w))
    print(f"Sorted by length: {by_length}")


# =============================================================================
# SECTION 3: Lambda for Sorting
# =============================================================================

def demonstrate_lambda_sorting():
    """
    Demonstrate using lambda functions for custom sorting.
    
    The key parameter in sorted() and list.sort() accepts
    a function that extracts a comparison key from each element.
    """
    print("\n--- Lambda for Sorting ---")
    
    # List of tuples (name, age)
    people = [
        ("Alice", 30),
        ("Bob", 25),
        ("Charlie", 35)
    ]
    
    # Sort by age
    by_age = sorted(people, key=lambda p: p[1])
    print(f"Sorted by age: {by_age}")
    
    # Sort by name (alphabetically)
    by_name = sorted(people, key=lambda p: p[0])
    print(f"Sorted by name: {by_name}")
    
    # Sort in reverse order
    by_age_desc = sorted(people, key=lambda p: p[1], reverse=True)
    print(f"Sorted by age (descending): {by_age_desc}")


# =============================================================================
# SECTION 4: Lambda in Dictionary Operations
# =============================================================================

def demonstrate_lambda_with_dict():
    """
    Demonstrate using lambda with dictionaries.
    
    Lambdas are useful for extracting values from dictionaries
    and for creating simple data transformations.
    """
    print("\n--- Lambda with Dictionaries ---")
    
    # List of dictionaries
    students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 92},
        {"name": "Charlie", "grade": 78}
    ]
    
    # Sort by grade
    by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
    print("Students by grade (highest first):")
    for student in by_grade:
        print(f"  {student['name']}: {student['grade']}")
    
    # Extract all names
    names = list(map(lambda s: s["name"], students))
    print(f"All names: {names}")


# =============================================================================
# SECTION 5: Lambda vs Regular Functions
# =============================================================================

def demonstrate_lambda_vs_def():
    """
    Compare lambda functions with regular function definitions.
    
    Lambda functions are best for simple, one-line operations.
    For anything more complex, use regular def functions.
    """
    print("\n--- Lambda vs Regular Functions ---")
    
    # Lambda version
    multiply_lambda = lambda x, y: x * y
    
    # Equivalent regular function
    def multiply_def(x, y):
        return x * y
    
    print(f"Lambda: multiply_lambda(3, 4) = {multiply_lambda(3, 4)}")
    print(f"Def: multiply_def(3, 4) = {multiply_def(3, 4)}")
    
    # Both produce the same result
    print(f"Results are equal: {multiply_lambda(3, 4) == multiply_def(3, 4)}")


# =============================================================================
# MAIN: Demonstration of All Lambda Concepts
# =============================================================================

def main():
    """
    Main function demonstrating all lambda function examples.
    """
    print("=" * 60)
    print("PYTHON LAMBDA FUNCTIONS DEMONSTRATION")
    print("=" * 60)
    
    demonstrate_basic_lambda()
    demonstrate_lambda_with_builtins()
    demonstrate_lambda_sorting()
    demonstrate_lambda_with_dict()
    demonstrate_lambda_vs_def()
    
    print("\n" + "=" * 60)
    print("END OF DEMONSTRATION")
    print("=" * 60)


if __name__ == "__main__":
    main()
