#!/usr/bin/python

import sys

def counting_stairs(n):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  else:
    return counting_stairs(n-1) + counting_stairs(n-2) + counting_stairs(n-3)


def memo_counting_stairs(n, cache):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif cache[n] > 1:
    return cache[n]
  else:
    cache[n] = memo_counting_stairs(n-1, cache) + memo_counting_stairs(n-2, cache) + memo_counting_stairs(n-3, cache)
    return cache[n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print(counting_stairs(num_stairs))
  else:
    print('Usage: stairs.py [num_stairs]')