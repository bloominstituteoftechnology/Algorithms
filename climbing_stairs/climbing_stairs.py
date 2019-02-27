#!/usr/bin/python
# initt

import sys

def climbing_stairs(n, cache=None):
  # Base case, if no stairs to climb we stop
  if n < 0:
    return 0
  # child can only move in 1, 2, or 3 steps
  elif n == 0:
    return 1
  elif cache is None:
    cache = [0 for x in range(n + 1)]
  elif cache[n] is not 0:
    return cache[n]


  total = climbing_stairs(n - 3, cache) + climbing_stairs(n - 2, cache) + climbing_stairs(n - 1, cache)
  cache[n] = total

  return total



print(climbing_stairs(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')