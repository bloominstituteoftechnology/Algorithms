#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    # if cache[n] != 0:
    #     return cache[n]
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    total = 0
    total += eating_cookies(n-3)
    total += eating_cookies(n-2)
    total += eating_cookies(n-1)
    # cache[n] = total
    return total

# tutorial https://dbader.org/blog/python-memoization
def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func

# this works great!
# has to be tested with cacheless versions of the big calls tho
eating_cookies = memoize(eating_cookies)
    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')