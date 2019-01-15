#!/usr/bin/python

import sys
import math

cache = {}

def climbing_stairs(n, cache=cache):
  if n < 3:
    return math.factorial(n)
  if n in cache:
    return cache[n]
  sum = climbing_stairs(n-3) + climbing_stairs(n-2) + climbing_stairs(n-1)
  cache[n] = sum
  # print(sum)
  return sum
  # return climbing_stairs(n-3) + climbing_stairs(n-2) + climbing_stairs(n-1)


print(climbing_stairs(500))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')