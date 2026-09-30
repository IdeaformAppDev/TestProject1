# Fibonacci Calculator

This project contains an efficient implementation of the nth Fibonacci number calculator with two different approaches:

## Files

1. `fibonacci.py` - Contains both iterative and matrix exponentiation implementations
2. `test_fibonacci.py` - Unit tests for the Fibonacci functions
3. `demo_fibonacci.py` - Demo script showing how the functions work

## Features

- **Iterative approach** (`fibonacci(n)`): O(n) time complexity, O(1) space complexity
- **Matrix exponentiation approach** (`fibonacci_fast(n)`): O(log n) time complexity for better performance on large inputs
- Comprehensive unit tests to verify correctness
- Error handling for negative inputs
- Clear documentation and examples

## Usage

```python
from fibonacci import fibonacci, fibonacci_fast

# Calculate Fibonacci numbers
result = fibonacci(10)      # Returns 55
fast_result = fibonacci_fast(10)  # Also returns 55
```

Both functions will return the same result, but `fibonacci_fast` is more efficient for large values of n.