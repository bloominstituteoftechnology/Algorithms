#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # iterative
    # if n <= 1:
    #     return 1
    # else:
    #     result = [None] * (n+1)
    #     result[0] = 1
    #     result[1] = 1
    #     result[2] = 2

    #     for i in range(3, n+1):
    #         result[i] = result[i-1] + result[i-2] + result[i-3]

    #     return result[n]

    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = {i: 0 for i in range(n+1)}

        cache[n] = eating_cookies(
            n-1, cache)+eating_cookies(n-2, cache)+eating_cookies(n-3, cache)
    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
