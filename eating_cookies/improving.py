
cache = {0: 1, 1: 1}
def recursion_fibonacci(n):
    #base
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1

    # handling cache
    if n in cache:
        return cache[n]
    # if not in cache: 
    cache[n] = recursion_fibonacci(n-1) + recursion_fibonacci(n-2)
    return cache[n]

x=recursion_fibonacci(10)
print(x)

