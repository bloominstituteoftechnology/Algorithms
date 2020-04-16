#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if cache is None:
        cache = [0 for i in range(n + 1)]
    total_ways = 0
    if cache[n] != 0:
        return cache[n]
    if n == 0:
        new_ways = 1
        total_ways += new_ways
    if n >= 1:
        new_ways = eating_cookies(n - 1, cache)
        total_ways += new_ways
    if n >= 2:
        new_ways = eating_cookies(n - 2, cache)
        total_ways += new_ways
    if n >= 3:
        new_ways = eating_cookies(n - 3, cache)
        total_ways += new_ways
    cache[n] = total_ways
    return total_ways


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies),
                                                                                    n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
