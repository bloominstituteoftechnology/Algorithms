#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if cache is None:
        cache = [0 for x in range(n + 1)]
    if cache[n] is not 0:
        return cache[n]

    val = climbing_stairs(n-1, cache) + climbing_stairs(n-2,
                                                        cache) + climbing_stairs(n-3, cache)
    cache[n] = val
    return val


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
