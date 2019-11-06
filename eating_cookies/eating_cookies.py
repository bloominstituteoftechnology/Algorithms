#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n):
    cache = {}

    def eat(num):
        if num == 0:
            return 1
        elif num < 0:
            return 0
        elif num not in cache:
            total = eat(num - 1) + eat(num - 2) + eat(num - 3)
            cache[num] = total
        return cache[num]
    return eat(n)

# print (eating_cookies(3))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
