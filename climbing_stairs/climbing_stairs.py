#!/usr/bin/python

import sys
import math

def climbing_stairs(n, cache=None):
  return math.factorial(n) / math.factorial(n-2)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')