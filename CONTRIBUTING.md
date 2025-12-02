# Contributing to Simply-Python

Thank you for your interest in contributing to Simply-Python! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Coding Guidelines](#coding-guidelines)
- [Pull Request Process](#pull-request-process)
- [Adding New Modules](#adding-new-modules)

## 📜 Code of Conduct

This project is dedicated to providing a welcoming and inclusive environment. We expect all contributors to:

- Be respectful and considerate
- Welcome newcomers and help them learn
- Accept constructive criticism gracefully
- Focus on what is best for the community

## 🤔 How Can I Contribute?

### Reporting Bugs

If you find a bug in any example:

1. Check if it's already reported in the [Issues](https://github.com/GIL794/Simply-Python/issues)
2. If not, create a new issue with:
   - A clear, descriptive title
   - Steps to reproduce the problem
   - Expected vs actual behavior
   - Python version you're using

### Suggesting Enhancements

Have an idea for a new module or improvement?

1. Check existing issues and discussions
2. Create a new issue describing:
   - The concept you'd like to see covered
   - Why it would be valuable for learners
   - Any specific examples you have in mind

### Improving Documentation

Documentation improvements are always welcome:

- Fix typos and grammatical errors
- Clarify explanations
- Add more examples
- Improve formatting

### Adding Code Examples

Want to add new examples or improve existing ones?

- Follow our [Coding Guidelines](#coding-guidelines)
- Ensure examples are well-commented
- Add appropriate documentation

## 🚀 Getting Started

1. **Fork the repository**

   Click the "Fork" button at the top right of the repository page.

2. **Clone your fork**

   ```bash
   git clone https://github.com/YOUR-USERNAME/Simply-Python.git
   cd Simply-Python
   ```

3. **Create a branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**

   Edit files, add new content, fix bugs, etc.

5. **Test your changes**

   ```bash
   # Run the module you modified
   python module_name/module_name.py
   ```

6. **Commit your changes**

   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

7. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

8. **Open a Pull Request**

   Go to the original repository and click "New Pull Request"

## 📝 Coding Guidelines

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use meaningful variable and function names
- Maximum line length: 88 characters (Black formatter standard)

### Comments and Documentation

Every code example should include:

1. **Module docstring** - Explain what the file demonstrates

   ```python
   """
   Brief description of the module.
   
   More detailed explanation of what concepts
   are covered and why they're important.
   
   Author: Simply-Python Contributors
   License: MIT
   """
   ```

2. **Function/Class docstrings** - Explain purpose and usage

   ```python
   def my_function(param: str) -> str:
       """
       Brief description of what the function does.
       
       More detailed explanation if needed.
       
       Args:
           param: Description of the parameter
           
       Returns:
           Description of return value
           
       Example:
           >>> my_function("hello")
           "HELLO"
       """
   ```

3. **Inline comments** - Explain complex logic

   ```python
   # Calculate the running average
   # We use cumulative sum divided by count for efficiency
   avg = cumsum / count
   ```

### Type Hints

Use type hints for function signatures:

```python
from typing import List, Optional, Generator

def process_items(items: List[str]) -> Optional[str]:
    ...
```

### Example Structure

Each example file should follow this structure:

```python
"""Module docstring."""

# Imports
import ...

# Constants (if any)
CONSTANT = ...

# Section 1: Topic
# ================
class/def ...

# Section 2: Topic
# ================
class/def ...

# Main demonstration
def main():
    """Main function demonstrating all examples."""
    ...

if __name__ == "__main__":
    main()
```

## 🔄 Pull Request Process

1. **Ensure your code runs without errors**

2. **Update documentation** if you've changed functionality

3. **Write a clear PR description** explaining:
   - What changes you made
   - Why you made them
   - Any relevant issue numbers

4. **Wait for review** - Maintainers will review your PR

5. **Address feedback** - Make requested changes if any

6. **Celebrate** 🎉 - Your contribution is merged!

## ➕ Adding New Modules

When creating a new module:

1. **Create a new directory** with a descriptive name

   ```
   new_topic/
   ├── new_topic.py
   ├── README.md
   └── LICENSE
   ```

2. **Follow the existing structure**
   - Look at existing modules for examples
   - Include comprehensive comments
   - Add multiple examples showing different aspects

3. **Create a README.md** including:
   - Overview of the topic
   - What the learner will gain
   - Prerequisites
   - Code examples
   - Best practices
   - Further reading

4. **Copy the LICENSE file** from the root

5. **Update the root README.md** to include your new module

### Module Ideas

Here are some advanced Python topics we'd love to see:

- Metaclasses
- Descriptors
- Async/Await programming
- Multithreading and multiprocessing
- Design patterns
- Type system and protocols
- Testing patterns
- Memory management

## 💬 Questions?

If you have questions about contributing, feel free to:

- Open an issue with the "question" label
- Start a discussion in the repository

---

**Thank you for contributing to Simply-Python!** 🐍
