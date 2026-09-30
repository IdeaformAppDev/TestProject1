def fibonacci(n):
    """
    Calculate the nth Fibonacci number efficiently using an iterative approach.

    The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): The position in the Fibonacci sequence (non-negative integer)

    Returns:
        int: The nth Fibonacci number

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Use iterative approach for O(n) time and O(1) space complexity
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def fibonacci_fast(n):
    """
    Calculate the nth Fibonacci number using matrix exponentiation for better performance.

    This approach has O(log n) time complexity and is more efficient for large values of n.

    Args:
        n (int): The position in the Fibonacci sequence (non-negative integer)

    Returns:
        int: The nth Fibonacci number

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Matrix exponentiation approach
    def matrix_multiply(A, B):
        """Multiply two 2x2 matrices."""
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]

    def matrix_power(matrix, power):
        """Calculate matrix^power using fast exponentiation."""
        if power == 1:
            return matrix

        # Identity matrix
        result = [[1, 0], [0, 1]]
        base = matrix

        while power > 0:
            if power % 2 == 1:
                result = matrix_multiply(result, base)
            base = matrix_multiply(base, base)
            power //= 2

        return result

    # Base transformation matrix for Fibonacci
    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(fib_matrix, n)

    return result_matrix[0][1]