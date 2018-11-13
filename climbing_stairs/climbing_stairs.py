#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  cache = [1, 1, 2, 4]
  if n < 4:
    return cache[n]
  for i in range(4, n+1):
    ans = 0
    ans += cache[i-1] + cache[i-2] + cache[i-3]
    cache.append(ans)
  return cache[len(cache)-1]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')