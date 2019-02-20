#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):

    cache = [0] * (n + 1)
    cache[0] = 1
    cache[1] = 1
    cache[2] = 2

    for i in range(3, n + 1):
      cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
    return cache[n] 


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
