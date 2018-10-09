#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):

  if n <= 0: 
    return 0
  elif n == 1: 
    return 1
  elif n == 2: 
    return 2
  elif n == 3: 
    return 4 
  return climbing_stairs(n-1, cache) + climbing_stairs(n-2, cache) + climbing_stairs(n-3, cache)   

  pass 
# does not work for big numbers yet

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')