#!/usr/bin/python


# Pseudocode
# Given a jar of cookies with "n" amount inside.
# How many way can he eat all n cookies?
# Can eat 0,1,2, or 3 cookies at a time.
# Cant be negative(assuming?)
# n = 0 answer is 1 bcuz can eat 0 times
# n = 1 answer is 1
# n = 2 answer is 2, bcuz (1,1) and (2)
# n = 3 answer is 4, bcuz (1,1,1), (1,2), (2,1), (3)
# n = 5 answer is 13

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):

    if n < 0:
        return 0
    if n <= 1:
        return 1
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    # n = 3 -> eating_cookies(2) + eating_cookies(1) + eating_cookies(0) = 2 + 1 + 1 = 4
    # n = 4 -> eating_cookies(3) + eating_cookies(2) + eating_cookies(1) = 4 + 2 + 1 = 7
    # n = 5 -> eating_cookies(4) + eating_cookies(3) + eating_cookies(2) = 7 + 4 + 2 = 13


# print(eating_cookies(3))


# print(eating_cookies(2))
# print(eating_cookies(3))
# print(eating_cookies(5))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
