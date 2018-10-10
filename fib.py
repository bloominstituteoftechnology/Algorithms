def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fib((n-1) + (n-2))

print(fib(3))