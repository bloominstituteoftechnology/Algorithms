#!/usr/bin/python

import sys
# can go up one stair at a time
# two stairs at a time
# three stairs at a time
# and other random orders
def climbing_stairs(n, cache=None):
    options = [1, 2, 3]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')