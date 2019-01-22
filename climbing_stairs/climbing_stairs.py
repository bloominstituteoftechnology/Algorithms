#!/usr/bin/python

import sys

def climbing_stairs(n, cache={}):
  cache[0] = 1
  cache[1] = 1
  cache[2] = 2
  
  if n in cache:
    return cache[n]
  else:
    if cache.get(n-1, False) == False:
      climbing_stairs(n-1)
    if cache.get(n-2, False) == False:
      climbing_stairs(n-2)
    if cache.get(n-3, False) == False:
      climbing_stairs(n-3)
    else:
      cache[n] = cache[n-1] + cache[n-2] + cache[n-3]
      return climbing_stairs(n)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')