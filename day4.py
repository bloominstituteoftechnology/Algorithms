def fib_top_down_dynamic(n, cache={}):

    # cache = {}

    def fib2(n):   # O(n) time, O(n) space

        nonlocal cache

        if n == 0: return 0 # base case
        if n == 1: return 1

        if n not in cache:
            cache[n] = fib2(n-1) + fib2(n-2)

        return cache[n]
    
    return fib2(n)


def fib_bottom_up_iterative(n):  # O(n) time, O(n) space
    if n == 0: return 0
    if n == 1: return 1

    p2 = 0
    p = 1

    count = 0

    while count < n-1:
        c = p + p2

        p2 = p
        p = c

        count += 1

    return c

for i in range(1500):
    print(f'{i}: {fib_top_down_dynamic(i)}')