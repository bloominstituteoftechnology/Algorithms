#!/usr/bin/python

import sys

def climbing_stairs(n, cache={}):
  if n <= 1:
    return 1
  elif n == 2:
    return 2

  if n in cache:
    return cache[n]

  result = climbing_stairs(n-3) + climbing_stairs(n-2) + climbing_stairs(n-1)
  cache[n] = result

  return result

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')