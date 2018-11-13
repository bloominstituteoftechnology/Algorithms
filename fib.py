# fib(0) = 0
# fib(1) = 1
# fib(n) = fib(n-1) + fib(n-2)


####### MEMOIZATION #######
###
# cache = {}

# def fib_memoized(n):
#     if n == 0:
#         return 0

#     if n == 1:
#         return 1
    
#     if n not in cache:
#         cache[n] = fib_memoized(n-1) + fib_memoized(n-2)
#     return cache[n]

# cache[0] = 0
# cache[1] = 1

# for i in range(1000):
#     print(f'{i}: {fib_memoized(i)}')

####### BOTTOM UP #######
def fib_bottomup(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    p0 = 0
    p1 = 1

    for i in range(n-1):
        next = p0 + p1

        p0 = p1
        p1 = next

    return next

for i in range(500):
    print(f'{i}: {fib_bottomup(i)}')



#### (easy way, but not efficient) ####
##
# def fib(n):
#     if n == 0:
#         return 0

#     if n == 1:
#         return 1
    
#     return fib(n-1) + fib(n-2)

# for i in range(100):
#     print(f'{i}: {fib(i)}')