#!/usr/bin/python

import sys
# can go up one stair at a time
# two stairs at a time
# three stairs at a time
# and other random orders


def climbing_stairs(n):
    # Not using the cache yet, might get back to it
    if n == 0:
        return 1
    if n <= 2:
        return n

    prev = 2
    prev2 = 1
    prev3 = 1
    current = 0

    for i in range(2, n):
        current = prev + prev2 + prev3
        prev3 = prev2  #  every iteration previous number gets set to next number in series
        prev2 = prev
        prev = current

    return current



if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')