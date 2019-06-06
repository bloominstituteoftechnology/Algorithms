#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution




def eating_cookies(n, cache=None):
    if n == 0:
        return 1
    return 2 ** (n - 1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')

# 1: 1   
# 2: 2  fib + 1
# 3: 4  fib()
# 4: 7?
# 5: 13  fib(n+2)
#10: 274

# 0  1  2  3  4  5  6  7   8
# 0, 1, 1, 2, 3, 5, 8, 13, 21,
4 + 3 + 3
