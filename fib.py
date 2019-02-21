# fib(n) = fib(n - 1) + fib(n - 2)


def fib(n):
    # Manually set base cases for F0 and F1 so that the recursion won't try to get negative values
    if n == 1:
        return 1
    if n <= 0:
        return 0
    return fib(n - 1) + fib(n - 2)


cache = {}


def dynamic_fib(n):
    # Manually set base cases for F0 and F1 so that the recursion won't try to get negative values
    if n == 1:
        return 1
    if n <= 0:
        return 0
    if n in cache:
        return cache[n]
    val = dynamic_fib(n - 1) + dynamic_fib(n - 2)
    cache[n] = val
    return val


inputs = [i for i in range(10, 40)]
