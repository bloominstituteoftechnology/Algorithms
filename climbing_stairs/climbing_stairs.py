#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  count = 0
  if n <= 0:
    return 2
  elif n <= 2 and n > 0:
    if not cache == None:
      cache[n] = n
    return n
  elif n == 3:
    if not cache == None:
      cache[n] = 4
    return 4
  else:
    if cache == None:
      count = climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)
      return count
    else:
      if not cache[n] == 0:
        return cache[n]
      else:
        cache[n] = climbing_stairs(n-1, cache) + climbing_stairs(n-2, cache) + climbing_stairs(n-3, cache)
        return cache[n]
      

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')
