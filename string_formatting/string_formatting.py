"""
Python String Formatting: Simple Programming Concepts

This module demonstrates string formatting in Python,
including f-strings, format() method, and practical examples.

Author: Simply-Python Contributors
License: MIT
"""


# =============================================================================
# SECTION 1: F-Strings (Formatted String Literals)
# =============================================================================

def demonstrate_fstrings():
    """
    Demonstrate f-strings, the modern way to format strings.
    
    F-strings were introduced in Python 3.6 and are the
    recommended way to format strings. They are fast,
    readable, and support any Python expression.
    
    Syntax: f"text {expression} more text"
    """
    print("--- F-Strings ---")
    
    # Basic variable insertion
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")
    
    # Expressions in f-strings
    x = 10
    y = 5
    print(f"{x} + {y} = {x + y}")
    print(f"{x} * {y} = {x * y}")
    
    # Calling methods
    text = "hello"
    print(f"Uppercase: {text.upper()}")


# =============================================================================
# SECTION 2: Number Formatting
# =============================================================================

def demonstrate_number_formatting():
    """
    Demonstrate formatting numbers with f-strings.
    
    You can control decimal places, add thousands separators,
    and format as percentages using format specifiers.
    
    Syntax: f"{value:format_spec}"
    """
    print("\n--- Number Formatting ---")
    
    # Decimal places
    pi = 3.14159265359
    print(f"Pi with 2 decimals: {pi:.2f}")
    print(f"Pi with 4 decimals: {pi:.4f}")
    
    # Thousands separator
    large_number = 1234567
    print(f"With commas: {large_number:,}")
    
    # Percentage
    ratio = 0.856
    print(f"As percentage: {ratio:.1%}")
    
    # Padding numbers
    number = 42
    print(f"Padded with zeros: {number:05d}")


# =============================================================================
# SECTION 3: String Alignment
# =============================================================================

def demonstrate_alignment():
    """
    Demonstrate text alignment and padding.
    
    You can align text left, right, or center within
    a specified width using format specifiers.
    
    < left, > right, ^ center
    """
    print("\n--- String Alignment ---")
    
    text = "Hello"
    
    # Left, right, center alignment (width 15)
    print(f"Left:   |{text:<15}|")
    print(f"Right:  |{text:>15}|")
    print(f"Center: |{text:^15}|")
    
    # Padding with custom character
    print(f"Padded: |{text:-^15}|")
    
    # Creating a simple table
    print("\nSimple Table:")
    items = [("Apple", 1.50), ("Banana", 0.75), ("Orange", 2.00)]
    for item, price in items:
        print(f"  {item:<10} ${price:>5.2f}")


# =============================================================================
# SECTION 4: The format() Method
# =============================================================================

def demonstrate_format_method():
    """
    Demonstrate the str.format() method.
    
    This is an older but still useful way to format strings.
    It uses {} as placeholders.
    """
    print("\n--- The format() Method ---")
    
    # Basic usage
    template = "Hello, {}!"
    print(template.format("World"))
    
    # Multiple placeholders
    template = "{} + {} = {}"
    print(template.format(2, 3, 5))
    
    # Named placeholders
    template = "Name: {name}, Age: {age}"
    print(template.format(name="Bob", age=25))
    
    # Positional arguments
    template = "{0} is {1} years old. {0} likes Python."
    print(template.format("Alice", 30))


# =============================================================================
# SECTION 5: Practical Examples
# =============================================================================

def demonstrate_practical_examples():
    """
    Demonstrate practical string formatting examples.
    
    These are common patterns you'll use in real applications.
    """
    print("\n--- Practical Examples ---")
    
    # Formatting a date
    day, month, year = 15, 6, 2024
    print(f"Date: {day:02d}/{month:02d}/{year}")
    
    # Formatting currency
    price = 49.99
    print(f"Price: ${price:.2f}")
    
    # Debugging with f-strings (Python 3.8+)
    x = 10
    y = 20
    print(f"{x=}, {y=}, {x+y=}")
    
    # Building a progress bar
    progress = 0.65
    bar_length = 20
    filled = int(bar_length * progress)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"Progress: |{bar}| {progress:.0%}")


# =============================================================================
# MAIN: Demonstration of All String Formatting Concepts
# =============================================================================

def main():
    """
    Main function demonstrating all string formatting examples.
    """
    print("=" * 60)
    print("PYTHON STRING FORMATTING DEMONSTRATION")
    print("=" * 60)
    
    demonstrate_fstrings()
    demonstrate_number_formatting()
    demonstrate_alignment()
    demonstrate_format_method()
    demonstrate_practical_examples()
    
    print("\n" + "=" * 60)
    print("END OF DEMONSTRATION")
    print("=" * 60)


if __name__ == "__main__":
    main()
