#!/usr/bin/python

import sys
#1,2,3 steps at a time

def climbing_stairs(n, cache=None):
  if n < 0:
    return 0
  if n == 0:
    return 1
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 3
  cache = {i : 0 for i in range(n+1)}
  cache[n] += climbing_stairs(n-1)
  if cache == cache[n]:
    return cache[n]
  pass 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')