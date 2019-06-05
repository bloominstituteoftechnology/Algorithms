#!/usr/bin/python
import sys
# [0, 1, 1, 2, 3, 5, 8]

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n):
    if n <= 0:
        return 0
    if n <= 2:
        return n
    if n == 3:
        return 4

    return(eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))


print(eating_cookies(10))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
