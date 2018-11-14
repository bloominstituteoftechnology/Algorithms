#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  if n == 0:
    return 1
  if n == 1:
    return 1
  if n == 2:
    return 2

  cache = [1, 1, 2]

  for i in range(3, n + 1):
    cache.append(cache[-1] + cache[-2] + cache[-3])

  return cache[-1]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')