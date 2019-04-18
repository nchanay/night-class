"""
recursion.py
"""


def factorial(n):
    """
    returns n x (n-1) x (n-2) x ... x 1
    """
    if n == 1:
        print('bottoming out')
        return 1
    print('n = ', n)
    f = n * factorial(n-1)
    print(f'{n}! = {f}')
    return f


def count_up_to_n(n):
    """
    recursively prints from 1 to n
    """
    if n < 1:
        return
    count_up_to_n(n-1)
    print(n)


def count_down_to_n(n):
    """
    recursively prints from n to 1
    """
    if n < 1:
        return
    print(n)
    count_down_to_n(n-1)


def summation(n):
    """
    returns n + (n-1) + (n-2) + ... + 0
    """
    if n == 0:
        print('bottoming out')
        return 0
    print('n = ', n)
    f = n + summation(n-1)
    print(f'summation {n} = {f}')
    return f


def fibonacci(n):
    """
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


fibonacci_cache = [0, 1]


def memoized_fibonacci(n):
    """
    uses cached fibonacci numbers to calculate the bt fibonacci number
    """
    if n >= len(fibonacci_cache):
        fib = memoized_fibonacci(n-1) + memoized_fibonacci(n-2)
        fibonacci_cache.append(fib)
        return fib
    return fibonacci_cache[n]


def binary_search(l, target, start, end):
    """
    recursively searches for a target in list
    """
    mid = start + (end - start) // 2
    if target == l[mid]:
        return mid
    elif end <= start:
        return 'Not found'
    else:
        if target < l[mid]:
            return binary_search(l, target, start, mid)
        elif l[mid] < target:
            return binary_search(l, target, mid + 1, end)


def merge(l1, l2):
    merged = []
    i = j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    merged += l1[i:]
    merged += l2[j:]
    return merged


def mergesort(l):
    if len(l) <= 1:
        return l
    elif len(l) == 2:
        if l[0] < l[1]:
            return l
        else:
            return [l[1], l[0]]
    else:
        mid = len(l) // 2
        return merge(mergesort(l[:mid]), mergesort(l[mid:]))


print(factorial(5))
count_up_to_n(10)
count_down_to_n(10)
print(summation(5))
print(fibonacci(10))
print(memoized_fibonacci(10))
