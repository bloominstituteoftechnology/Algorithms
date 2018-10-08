#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    # this is a working solution
    if cache is None:
        cache = [0 for i in range(20)]
    cache[0] = 1
    cache[1] = 1
    cache[2] = 2
    for i in range(3, n + 1):
        cache[i] = cache[i - 3] + cache[i - 2] + cache[i - 1]

    return cache[n]

    # #####  Using recur
    # if n == 0:
    #     return 1
    # elif n < 3 and n != 0:
    #     return n

    # return climbing_stairs(n - 1) + climbing_stairs(n - 2) + climbing_stairs(n - 3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
