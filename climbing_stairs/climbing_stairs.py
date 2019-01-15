#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    cache = {0: 1, 1: 1, 2: 2}
    current = 3
    while current <= n:
        cache[current] = cache[current-1] + cache[current-2] + cache[current-3]
        current += 1
    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
