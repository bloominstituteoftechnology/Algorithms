fib_cache = {}
def fib(n):
    # if we have cached the value, then return it
    if n in fib_cache:
        return fib_cache[n]
    # compute the Nth term
    if n <= 2:
        value = n
    elif n>2:
      value = fib(n-1) + fib(n-2)

    # cache the value and return it
    fib_cache[n] = value
    return value

print(fib(5))


# *** V2 ***

def fib(n, cache):
    if n < 2:
        return n
    elif cache[n] > 0:
        return cache[n]
    cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    return cache[n]

n = 35
cache = {i: 0 for i in range(n + 1)}
print(fib(n, cache))

# *** v3 *** w/iteration
def iter_fib(n):
    answer = 0
    prev = 1
    prevPrev = 0
    for i in range(n-1):
        answer = prev + prevPrev
        prev = answer
        prevPrev = prev
    return answer