#!/usr/bin/python

import sys
# first pass using recursive calls giving 0.002s for 2 tests
def climbing_stairs(n, cache=None):
  # base case for n is zero
  if n == 0:
      return 1
  # secondary base of n < 0
  elif n < 0:
      return 0
  # now testing for cache and cahce of n being greater than 0
  elif cache and cache[n] > 0:
      return cache[n]
  # then if all bases fail run a recursive chache hitter
  else:
      # test for empty cache and fill the cache using a for in loop
      if not cache:
          cache = {i: 0 for i in range(n+1)}
      # use recursive calls of climbing stairs of [n - 1] + [n - 2] + [n - 3]
      cache[n] = climbing_stairs(
          n-1, cache) + climbing_stairs(n-2, cache) + climbing_stairs(n-3, cache)
      # return the cache at n
      return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')