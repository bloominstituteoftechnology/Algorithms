#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  # cache = {0:1, 1:1, 2:2, 3:4}
  # if cache.get(n) is None:
  #   cache[n] =  climbing_stairs(n-1, cache) + climbing_stairs(n-2, cache) + climbing_stairs(n-3, cache)
  # return cache[n]

  # if n == 1 or n == 0:
  #   return 1
  # elif n == 2:
  #   return 2
  # return climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)

  cache = {0:1, 1:1, 2:2, 3:4}
  counter = 3
  while counter <= n:
    cache[counter]=cache[counter-1] + cache[counter-2] + cache[counter-3]
    counter+=1
  return cache[n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')