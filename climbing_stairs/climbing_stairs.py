#!/usr/bin/python

import sys
cache = {}
def climbing_stairs(n, cache={}):
  #cache = {}
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 4
  if n in cache:
    return cache[n]

  cache[n] = climbing_stairs(n-1, cache) + climbing_stairs(n-2, cache) + climbing_stairs(n-3, cache)
  print(cache)
  return cache[n]



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')