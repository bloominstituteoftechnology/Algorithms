#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n):
    if n == 0:
        return 1
    elif n < 1:
        return 0
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    # 0, 1, 2, 3
    # n = 7
    # m = 3
    # arr = []
    # count = n
    # loop
    # if(count >= m)
    #   arr.append(m)
    # else:
    #   arr.appen(count)
    #  count = n - sum(arr) = 1
    # [3, 3, 1] = whatever
    # for i in range(len(whatevber), 0, -1):
    #   if whatever[i] - 1 != 0:
    #     [3, 2, 1, 1]
    #
    # [3, 2, 1, 1]
    # [3, 1,1,1,1]
    # [2, 1, 1, 1, 1, 1]
    # [1, 1, 1, 1, 1, 1, 1]
    # [2,2,2,1]
    # [2, 2, 1, 1, 1]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
