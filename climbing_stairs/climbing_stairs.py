#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  if  n < 0:
    return 0
  elif n == 0:
    return 1
    #check if the answer is in the cache
  elif cache and cache [n] > 0:
    return cache[n]
  else:
    if not cache:
      #cache = {i: 0 for i in range(n+1)}
      cache = [0 for i in range(n+1)]
    # populate the cache
    cache[n] = cliumbing_stairs(n-1, cahce) + climbing_stairs(n-2, cache) + climbing_stairs(n-3, cache)
    return cache[n]

  print(climbing_stairs(10))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')