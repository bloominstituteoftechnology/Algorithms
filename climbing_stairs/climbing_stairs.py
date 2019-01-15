#!/usr/bin/python

import sys

# First Pass
# def climbing_stairs(n, cache=None):
#   if (n == 0 or n == 1):
#     return 1
#   elif (n == 2):
#     return 2
  
#   else:
#     return climbing_stairs(n - 1) + climbing_stairs(n - 2) + climbing_stairs(n - 3)

def climbing_stairs(n, cache=None):
  if (n == 0 or n == 1):
    return 1
  elif (n == 2):
    return 2
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if not cache:
      cache = {i: 0 for i in range(n+1)}
    cache[n] = climbing_stairs(n-1, cache) + climbing_stairs(n-2, cache) + climbing_stairs(n-3, cache)
    return cache[n]

n = 10
print(climbing_stairs(n))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')