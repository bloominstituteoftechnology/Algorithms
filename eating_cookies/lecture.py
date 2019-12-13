def naive_fib(n):
    if n == 0: return 0
    if n == 1: return 1

    return naive_fib(n - 1) + naive_fib(n - 2)

def cashe_fib(n):
    cache = {0:0, 1:1}

    def cashe_fib_inner(n):
        nonlocal cache

        # if n == 0: return 0
        # if n == 1: return 1
        #
        if n not in cache:
            cashe[n] = cache_fib(n - 1) + cache_fib(n - 2)

        return cache[n]

for i in range(10):
    print(cashe_fib(i))