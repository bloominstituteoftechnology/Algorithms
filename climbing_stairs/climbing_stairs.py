#!/usr/bin/python

import sys

def climbing_stairs(num_stairs, cache=None):
    if num_stairs == 0:
        return 0
    if num_stairs == 1:
        return 1

    if num_stairs not in cache:
        cache[nnum_stairs] = climbing_stairs(nnum_stairs-1) + climbing_stairs(nnum_stairs-2)
    return cache[nnum_stairs]

    if num_stairs <= 10:
        


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')
