#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# [1, 1, 1], [2, 1], [3]
# [1, 1, 1], [2, 1], [1, 2], [3]

# 5 = eat(4) + eat(3) + eat(2)
# 4 = eat(3) + eat(2) + eat(1)
# 3 = eat(2) + eat(1) + eat(0)
# 2 = eat(1) + eat(0) + eat(-1)
# 1 = eat(0) + eat(-1) + eat(-2)


def eating_cookies(n, cache=None):
    # For each possible number of cookies to eat
    # calculate the number of ways to eat n cookies
    # n = (n - 3) + (n -2) + (n - 1)
    if cache is None:
        cache = [0] * (n + 1)
        cache[0] = 1

    if n < 0:
        return 0

    if cache[n] != 0:
        return cache[n]

    cache[n] = eating_cookies(n - 3, cache) \
        + eating_cookies(n - 2, cache) \
        + eating_cookies(n - 1, cache)
    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
