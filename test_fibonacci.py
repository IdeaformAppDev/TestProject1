import unittest
from fibonacci import fibonacci, fibonacci_fast


class TestFibonacci(unittest.TestCase):
    """Test cases for Fibonacci function implementations."""

    def test_fibonacci_base_cases(self):
        """Test the base cases of the Fibonacci sequence."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_small_numbers(self):
        """Test small Fibonacci numbers."""
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_negative_input(self):
        """Test that negative inputs raise ValueError."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-10)

    def test_fibonacci_fast_base_cases(self):
        """Test the base cases of the fast Fibonacci sequence."""
        self.assertEqual(fibonacci_fast(0), 0)
        self.assertEqual(fibonacci_fast(1), 1)

    def test_fibonacci_fast_small_numbers(self):
        """Test small Fibonacci numbers with the fast implementation."""
        self.assertEqual(fibonacci_fast(2), 1)
        self.assertEqual(fibonacci_fast(3), 2)
        self.assertEqual(fibonacci_fast(4), 3)
        self.assertEqual(fibonacci_fast(5), 5)
        self.assertEqual(fibonacci_fast(6), 8)
        self.assertEqual(fibonacci_fast(7), 13)
        self.assertEqual(fibonacci_fast(8), 21)
        self.assertEqual(fibonacci_fast(9), 34)
        self.assertEqual(fibonacci_fast(10), 55)

    def test_fibonacci_fast_negative_input(self):
        """Test that negative inputs raise ValueError for fast implementation."""
        with self.assertRaises(ValueError):
            fibonacci_fast(-1)
        with self.assertRaises(ValueError):
            fibonacci_fast(-10)

    def test_both_implementations_match(self):
        """Test that both implementations give the same results."""
        for i in range(20):
            self.assertEqual(fibonacci(i), fibonacci_fast(i))

    def test_large_fibonacci_number(self):
        """Test with a larger Fibonacci number to ensure performance."""
        # Test a reasonably large number
        result1 = fibonacci(30)
        result2 = fibonacci_fast(30)
        self.assertEqual(result1, result2)
        self.assertEqual(result1, 832040)


if __name__ == '__main__':
    unittest.main()