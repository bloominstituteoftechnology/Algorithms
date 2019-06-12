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


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
