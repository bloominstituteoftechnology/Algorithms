#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    total = 0
    print(n)
    if n < 1:
        print('base case: {}'.format(n))
        return 1
    if n-1 > 0:
        print('minus 1: {}'.format(n))
        total += (1 + eating_cookies(n-1))
    if n-2 > 1:
        print('minus 2: {}'.format(n))
        total += (1 + eating_cookies(n-2))
    if n-3 > 2:
        print('minus 3: {}'.format(n))
        total += (1 + eating_cookies(n-3))

    return total


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')