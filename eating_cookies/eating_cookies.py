#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
# 0 is irrelivant. There are 0 ways to eat 0 cookies.
# Same goes for neg numbers.
# Should take in integer, and return integer.


def eating_cookies(n, cache=None):
    if n == 0:
        return 1
    elif n < 0:
        return 0

    # Number of cookies cookie monster can eat is:
    # 0, 1, 2, 3. Ignore 0 - it doesn't do anything.
    num_ways = 0
    for i in range(1, 4):
        if cache is not None:
            if cache[n - i] == 0:
                cache[n - i] = eating_cookies(n - i, cache)
            num_ways += cache[n - i]
        else:
            num_ways += eating_cookies(n - i)

    if cache is not None:
        cache[n] = num_ways
    return num_ways

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
