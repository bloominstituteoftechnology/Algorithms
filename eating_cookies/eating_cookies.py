#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
    if cache is None:
        cache = {}

    if n == 0:
        one_way = 1
        return one_way

    elif n < 0:
        no_way = 0
        return no_way

    elif cache and cache[n]:
        return cache[n]

    else:
        eating_one_cookie = eating_cookies(n - 1, cache)
        eating_two_cookie = eating_cookies(n - 2, cache)
        eating_three_cookie = eating_cookies(n - 3, cache)
        cache[n] = eating_one_cookie + eating_two_cookie + eating_three_cookie
        return cache[n]


# def eating_cookies(n):
#     if n == 0:
#         return 1

#     elif n < 0:
#         return 0

#     else:
#         return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print(
#             "There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
#                 ways=eating_cookies(num_cookies), n=num_cookies
#             )
#         )
#     else:
#         print("Usage: eating_cookies.py [num_cookies]")

print(eating_cookies(5))
