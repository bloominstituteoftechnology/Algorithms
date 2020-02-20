#fib (0,1,1,2,3,5,8,13,21)

cache = {}

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in cache:
        return cache[n]

    else:
        value = fib(n-1) + fib(n-2)
        cache[n] = value
        return value

    
print(fib(4))
    
        