#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):

    
    place = [0] * (n)
    print(place)
    place[0] = 1
    place[1] = 1
    place[2] = 2
    i = 3
    while i <= n:
        place[i] = climbing_stairs(i - 3) + climbing_stairs(i - 2) + climbing_stairs(i - 1)
        i += 1
    return place[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
