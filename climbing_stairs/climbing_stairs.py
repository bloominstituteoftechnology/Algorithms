#!/usr/bin/python

import sys

count = 0
def climbing_stairs(n, cache=None):
  
  if n <= 0:
    return 1
  elif n <= 2 and n > 0:
    return count + n
  elif n == 3:
    return count + 4
  else:
    return count + climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')