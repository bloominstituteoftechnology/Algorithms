#!/usr/bin/python

import sys

# def counting_stairs(n):
#   if n < 0:
#     return 0
#   elif n == 0:
#     return 1
#   else:
#     return counting_stairs(n-1) + counting_stairs(n-2) + counting_stairs(n-3)


def counting_stairs(n, cache=None):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif cache and cache[n] > 1:
    return cache[n]
  else:
    if cache:
      cache[n] = counting_stairs(n-1, cache) + counting_stairs(n-2, cache) + counting_stairs(n-3, cache)
      return cache[n]
    else:
      return counting_stairs(n-1) + counting_stairs(n-2) + counting_stairs(n-3) 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=counting_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: counting_stairs.py [num_stairs]')