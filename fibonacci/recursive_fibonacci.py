def nth_fib_recursive(n, cache=dict()):
    if n < 2:
        return n
    elif n in cache:
        return cache[n]
    else:
        cache[n] = nth_fib_recursive(n-1, cache) + nth_fib_recursive(n-2, cache)
        return cache[n]

print(nth_fib_recursive(100))
