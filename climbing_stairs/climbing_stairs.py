#!/usr/bin/python

import sys


def climbing_stairs(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)
    # count = 0
    # length = 'aaa'
    # while length <= n:
    #     a = b
    #     b = c
    #     c = a + b
    # count = count + 1
    # str1 = str(c)
    # if len(str1) > len(length):
    #     length = str1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')

        # Can hope 1 2 or 3 steps at a time.
