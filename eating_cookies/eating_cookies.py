#!/usr/bin/python

import sys

# cookie monster can eat 0, 1, 2, or 3 cookies at a time
# n is how many cookies he has to eat
# we want to know how many different ways he can eat all of the cookies
# base cases: if n == 0, just return 0
# if n == 1, we can to return 1


# so really it eems like we need to figure out how many
# ways we can divide n into chunks of 3, 2, and 1

# my current thought process is this:
#   i suppose we can start by splitting into a
#   list of highest possible values. i.e, 5 -> [3,2]
#
#    then we take each of those nodes and split them down, tree style
#                    [3,2]
#        [2,1,2]       -        [1,2,2]
# [1,1,1,2] - [2,1,1,1]   [1,1,1,2] - [1,2,1,1]
#
#      etc...
#
#
#    or, to show test case in readme:
#    [3]
# [2,1],[1,2]
# [1,1,1],  {[1,1,1] <--- dosnt count because [1,1,1] already happened}
# so essentially, our function needs to take n, split it into the
# larget possible list, down until we have single values of 1 or 0, then
# add those values back together


def eating_cookies(n, cache=None):
    if n <= 1:
        return n

    baseList = []
    # fill list with the fastest way to eat all cookies.
    # ie, n=8 would give -> [3, 3, 2]
    baseList = [3] * (n//3)
    print(baseList)
    if n % 3 == 2:
        baseList.append(2)
    elif n % 3 == 1:
        baseList.append(1)
    print(baseList)


eating_cookies(2)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
