"""
Python Context Managers: Advanced Programming Concepts

This module demonstrates various context manager patterns in Python,
including resource management, exception handling, and practical
use cases for the 'with' statement.

Author: Simply-Python Contributors
License: MIT
"""

import os
import time
import threading
from contextlib import contextmanager, ExitStack
from typing import Optional, Any, Generator
from datetime import datetime


# =============================================================================
# SECTION 1: Basic Context Manager Class
# =============================================================================

class FileManager:
    """
    A custom context manager for file operations.
    
    Context managers implement the 'with' statement protocol.
    They ensure resources are properly acquired and released,
    even if exceptions occur.
    
    To create a context manager class, implement:
    1. __enter__() - Called when entering the 'with' block
    2. __exit__() - Called when exiting the 'with' block
    
    Attributes:
        filename: Path to the file
        mode: File open mode ('r', 'w', 'a', etc.)
    """
    
    def __init__(self, filename: str, mode: str = 'r'):
        """
        Initialize the FileManager.
        
        Args:
            filename: Path to the file to manage
            mode: Mode to open the file in (default: 'r' for read)
        """
        self.filename = filename
        self.mode = mode
        self.file = None
        print(f"[FileManager] Initialized for '{filename}' in mode '{mode}'")
    
    def __enter__(self):
        """
        Enter the context - open the file.
        
        This method is called when entering the 'with' block.
        The return value is bound to the 'as' variable.
        
        Returns:
            The opened file object
        """
        print(f"[FileManager] Opening file '{self.filename}'")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context - close the file.
        
        This method is called when exiting the 'with' block,
        whether normally or due to an exception.
        
        Args:
            exc_type: Exception class if an exception occurred
            exc_val: Exception instance if an exception occurred
            exc_tb: Traceback if an exception occurred
            
        Returns:
            False to propagate exceptions, True to suppress them
        """
        if self.file:
            print(f"[FileManager] Closing file '{self.filename}'")
            self.file.close()
        
        if exc_type is not None:
            print(f"[FileManager] Exception occurred: {exc_type.__name__}: {exc_val}")
        
        # Return False to propagate exceptions (don't suppress them)
        return False


# =============================================================================
# SECTION 2: Timer Context Manager
# =============================================================================

class Timer:
    """
    A context manager that measures execution time.
    
    Useful for profiling code blocks and identifying performance
    bottlenecks. The elapsed time is available after exiting.
    """
    
    def __init__(self, description: str = "Operation"):
        """
        Initialize the Timer.
        
        Args:
            description: Description of what's being timed
        """
        self.description = description
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.elapsed: Optional[float] = None
    
    def __enter__(self):
        """Start the timer when entering the context."""
        self.start_time = time.perf_counter()
        print(f"[Timer] Starting: {self.description}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stop the timer and calculate elapsed time."""
        self.end_time = time.perf_counter()
        self.elapsed = self.end_time - self.start_time
        print(f"[Timer] {self.description} took {self.elapsed:.6f} seconds")
        return False


# =============================================================================
# SECTION 3: Context Manager using @contextmanager
# =============================================================================

@contextmanager
def change_directory(path: str) -> Generator[str, None, None]:
    """
    A context manager that temporarily changes the working directory.
    
    The @contextmanager decorator transforms a generator function
    into a context manager. This is often simpler than writing
    a full class.
    
    Structure:
    1. Code before 'yield' runs on __enter__
    2. The yielded value is bound to 'as' variable
    3. Code after 'yield' runs on __exit__
    
    Args:
        path: Directory to change to
        
    Yields:
        The new directory path
    """
    original_dir = os.getcwd()
    print(f"[Directory] Changing from '{original_dir}' to '{path}'")
    
    try:
        os.chdir(path)
        yield path
    finally:
        # This runs on exit, even if an exception occurred
        os.chdir(original_dir)
        print(f"[Directory] Restored to '{original_dir}'")


@contextmanager
def temporary_attribute(obj: Any, attr: str, value: Any) -> Generator[None, None, None]:
    """
    Temporarily set an attribute on an object.
    
    This is useful for testing or temporarily modifying
    behavior without permanent changes.
    
    Args:
        obj: The object to modify
        attr: The attribute name
        value: The temporary value to set
        
    Yields:
        None
    """
    # Save original value (or mark as non-existent)
    has_attr = hasattr(obj, attr)
    original_value = getattr(obj, attr, None) if has_attr else None
    
    print(f"[TempAttr] Setting {attr} = {value}")
    setattr(obj, attr, value)
    
    try:
        yield
    finally:
        if has_attr:
            print(f"[TempAttr] Restoring {attr} = {original_value}")
            setattr(obj, attr, original_value)
        else:
            print(f"[TempAttr] Removing {attr}")
            delattr(obj, attr)


# =============================================================================
# SECTION 4: Exception Handling in Context Managers
# =============================================================================

class SuppressExceptions:
    """
    A context manager that suppresses specified exception types.
    
    Similar to contextlib.suppress(), but with logging.
    Demonstrates how to handle exceptions in __exit__.
    """
    
    def __init__(self, *exceptions):
        """
        Initialize with exception types to suppress.
        
        Args:
            *exceptions: Exception classes to suppress
        """
        self.exceptions = exceptions
        print(f"[Suppress] Will suppress: {[e.__name__ for e in exceptions]}")
    
    def __enter__(self):
        """Enter the context."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context, potentially suppressing exceptions.
        
        If the exception type is in our list, return True to suppress it.
        Otherwise, return False to let it propagate.
        """
        if exc_type is not None:
            if issubclass(exc_type, self.exceptions):
                print(f"[Suppress] Suppressed {exc_type.__name__}: {exc_val}")
                return True  # Suppress the exception
            print(f"[Suppress] Not suppressing {exc_type.__name__}")
        return False


class TransactionManager:
    """
    A context manager simulating database transactions.
    
    Demonstrates the pattern of:
    - Begin transaction on enter
    - Commit on successful exit
    - Rollback on exception
    """
    
    def __init__(self, transaction_name: str):
        """Initialize the transaction."""
        self.name = transaction_name
        self.changes = []
    
    def __enter__(self):
        """Begin the transaction."""
        print(f"[Transaction] BEGIN: {self.name}")
        return self
    
    def add_change(self, change: str):
        """Record a change in the transaction."""
        self.changes.append(change)
        print(f"[Transaction] Change added: {change}")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Commit or rollback based on success/failure."""
        if exc_type is None:
            print(f"[Transaction] COMMIT: {self.name}")
            print(f"[Transaction] Applied changes: {self.changes}")
        else:
            print(f"[Transaction] ROLLBACK: {self.name}")
            print(f"[Transaction] Discarded changes: {self.changes}")
            self.changes.clear()
        
        return False  # Don't suppress exceptions


# =============================================================================
# SECTION 5: Reentrant Context Manager
# =============================================================================

class ReentrantLock:
    """
    A reentrant (nestable) lock context manager.
    
    Can be used in nested 'with' blocks without deadlock.
    Tracks the recursion level and only releases when
    fully exited.
    """
    
    def __init__(self, name: str = "lock"):
        """Initialize the lock."""
        self.name = name
        self._lock = threading.RLock()
        self._count = 0
    
    def __enter__(self):
        """Acquire the lock."""
        self._lock.acquire()
        self._count += 1
        print(f"[Lock] Acquired '{self.name}' (level {self._count})")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Release the lock."""
        self._count -= 1
        self._lock.release()
        print(f"[Lock] Released '{self.name}' (level {self._count})")
        return False


# =============================================================================
# SECTION 6: ExitStack for Dynamic Context Management
# =============================================================================

def demonstrate_exitstack():
    """
    Demonstrate ExitStack for managing multiple context managers.
    
    ExitStack is useful when:
    - The number of context managers is determined at runtime
    - You need to conditionally enter context managers
    - You want to manage cleanup callbacks
    """
    print("\n--- ExitStack Demonstration ---")
    
    with ExitStack() as stack:
        # Dynamically add context managers
        timer1 = stack.enter_context(Timer("Task 1"))
        timer2 = stack.enter_context(Timer("Task 2"))
        
        # Add a cleanup callback
        def cleanup():
            print("[ExitStack] Running cleanup callback")
        stack.callback(cleanup)
        
        # Simulate work
        time.sleep(0.1)
        print("[ExitStack] Work completed")
    
    print("[ExitStack] All contexts exited")


# =============================================================================
# SECTION 7: Async Context Manager (for reference)
# =============================================================================

class AsyncResource:
    """
    An async context manager for asynchronous resources.
    
    Async context managers use:
    - __aenter__ instead of __enter__
    - __aexit__ instead of __exit__
    - 'async with' instead of 'with'
    
    Note: This is shown for reference. Running it requires
    an async event loop (asyncio.run).
    """
    
    def __init__(self, name: str):
        """Initialize the async resource."""
        self.name = name
    
    async def __aenter__(self):
        """Async enter - can await async operations."""
        print(f"[AsyncResource] Acquiring {self.name}")
        # Simulate async acquisition
        # await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async exit - can await async operations."""
        print(f"[AsyncResource] Releasing {self.name}")
        # Simulate async release
        # await asyncio.sleep(0.1)
        return False


# =============================================================================
# SECTION 8: Practical Example - Logging Context
# =============================================================================

class LoggingContext:
    """
    A context manager that provides structured logging.
    
    Logs entry and exit of code blocks with timing and
    exception information.
    """
    
    def __init__(self, operation: str, log_level: str = "INFO"):
        """
        Initialize the logging context.
        
        Args:
            operation: Name of the operation being performed
            log_level: Logging level (INFO, DEBUG, WARNING, ERROR)
        """
        self.operation = operation
        self.log_level = log_level
        self.start_time: Optional[datetime] = None
    
    def __enter__(self):
        """Log entry and start timing."""
        self.start_time = datetime.now()
        print(f"[{self.log_level}] {self.start_time.isoformat()} - "
              f"ENTER: {self.operation}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Log exit with duration and status."""
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()
        
        if exc_type is None:
            status = "SUCCESS"
        else:
            status = f"FAILED ({exc_type.__name__}: {exc_val})"
        
        print(f"[{self.log_level}] {end_time.isoformat()} - "
              f"EXIT: {self.operation} - {status} - "
              f"Duration: {duration:.4f}s")
        
        return False


# =============================================================================
# MAIN: Demonstration of All Context Manager Concepts
# =============================================================================

def main():
    """
    Main function demonstrating all context manager examples.
    """
    print("=" * 60)
    print("PYTHON CONTEXT MANAGERS DEMONSTRATION")
    print("=" * 60)
    
    # Create a temporary file for demonstration
    # Using tempfile for cross-platform compatibility
    import tempfile
    temp_file = os.path.join(tempfile.gettempdir(), "context_manager_demo.txt")
    
    # 1. Basic Context Manager
    print("\n--- 1. Basic FileManager Context Manager ---")
    with FileManager(temp_file, 'w') as f:
        f.write("Hello, Context Managers!")
    
    with FileManager(temp_file, 'r') as f:
        content = f.read()
        print(f"File content: {content}")
    
    # 2. Timer Context Manager
    print("\n--- 2. Timer Context Manager ---")
    with Timer("Heavy computation") as timer:
        # Simulate work
        total = sum(i ** 2 for i in range(100000))
        print(f"Computed sum: {total}")
    print(f"Elapsed time accessible: {timer.elapsed:.6f}s")
    
    # 3. Change Directory Context Manager
    print("\n--- 3. Change Directory Context Manager ---")
    print(f"Current directory: {os.getcwd()}")
    with change_directory("/tmp"):
        print(f"Inside with block: {os.getcwd()}")
    print(f"After with block: {os.getcwd()}")
    
    # 4. Temporary Attribute Context Manager
    print("\n--- 4. Temporary Attribute Context Manager ---")
    
    class Config:
        debug = False
    
    config = Config()
    print(f"Before: debug = {config.debug}")
    with temporary_attribute(config, 'debug', True):
        print(f"Inside: debug = {config.debug}")
    print(f"After: debug = {config.debug}")
    
    # 5. Exception Suppression
    print("\n--- 5. Exception Suppression ---")
    with SuppressExceptions(ValueError, TypeError):
        print("This will raise ValueError, but it will be suppressed")
        raise ValueError("Test error")
    print("Execution continues after suppressed exception!")
    
    # 6. Transaction Manager
    print("\n--- 6. Transaction Manager ---")
    try:
        with TransactionManager("user_update") as txn:
            txn.add_change("Updated username")
            txn.add_change("Updated email")
            # Uncomment to see rollback:
            # raise RuntimeError("Database error!")
    except RuntimeError:
        print("Transaction was rolled back")
    
    # 7. Reentrant Lock
    print("\n--- 7. Reentrant Lock ---")
    lock = ReentrantLock("data_lock")
    with lock:
        print("First level")
        with lock:
            print("Second level (nested)")
        print("Back to first level")
    print("Lock fully released")
    
    # 8. ExitStack
    demonstrate_exitstack()
    
    # 9. Logging Context
    print("\n--- 9. Logging Context ---")
    with LoggingContext("fetch_user_data"):
        time.sleep(0.1)  # Simulate work
        print("Fetching user data...")
    
    # Cleanup
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    print("\n" + "=" * 60)
    print("END OF DEMONSTRATION")
    print("=" * 60)


if __name__ == "__main__":
    main()
