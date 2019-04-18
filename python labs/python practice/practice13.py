# Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.

# fibonacci(8) → [1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci(n):
    """
    >>> fibonacci(8)
    [1, 1, 2, 3, 5, 8, 13, 21]
    """
    if n >= len(fibonacci_cache):
        fib = fibonacci(n-1) + fibonacci(n-2)
        fibonacci_cache.append(fib)
        return fib
    return fibonacci_cache[n]


fibonacci_cache = [0, 1]
print(fibonacci(8))
print(fibonacci_cache)
