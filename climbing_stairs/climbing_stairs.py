#!/usr/bin/python

import sys

"""
Thoughts about this problem:

- The obvious relationship: the greater the number of stairs, the greater the number of combinations to ascend
- The relationship is not linear since the largest stair hop is 3
- Caching seems like a decent idea here
- If n = 0, there is nothing to do
- If n < 3, the number of ways to ascend the stairs is equal to the number of stairs
- As per Jon's note: for n >= 3, the total of the 3 previous n combinations will equal the current n

"""
def climbing_stairs(n, cache=None):
  if n == 0:
    return 1
  if n < 3:
    return n # first three cases covered, n = 0 or n < 3
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if not cache:
      cache = {i: 0 for i in range(n + 1)}
    cache[n] = climbing_stairs(n - 1, cache) + climbing_stairs(n - 2, cache), + climbing_stairs(n - 3, cache)
    return cache[n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')