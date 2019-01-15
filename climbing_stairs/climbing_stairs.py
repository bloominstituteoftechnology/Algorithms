#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    hops = 0
    ways = 0
    if n <= 0:
        return hops
    if n > 3:
        if n % 3 == 0:
            hops += 3
            print("hop")
            climbing_stairs((n - hops))
    return hops


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
# recursion possible
