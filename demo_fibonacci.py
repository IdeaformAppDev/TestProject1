#!/usr/bin/env python3
"""
Demo script for the Fibonacci calculator functions.
"""

from fibonacci import fibonacci, fibonacci_fast

def main():
    print("Fibonacci Calculator Demo")
    print("=" * 30)

    # Test some values
    test_values = [0, 1, 2, 3, 4, 5, 10, 20, 30]

    print("n\tIterative\tFast")
    print("-" * 30)

    for n in test_values:
        iter_result = fibonacci(n)
        fast_result = fibonacci_fast(n)
        print(f"{n}\t{iter_result}\t\t{fast_result}")

    # Show that both methods give the same results
    print("\nVerification:")
    for i in range(15):
        assert fibonacci(i) == fibonacci_fast(i), f"Mismatch at n={i}"
    print("✓ Both implementations produce identical results!")

if __name__ == "__main__":
    main()