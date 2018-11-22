#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  if (n < 0):
    # print('You climbed past the top stair.')
    return None
  elif (n == 0 or n == 1):
    # print('Only 1 way up')
    return   1
  elif (n == 2):
    # print('2 ways up')
    return 2

  # Option 1: thread the state through each open recursive call
  # else:
    # return climbing_stairs(n - 3) + climbing_stairs(n - 2) + climbing_stairs(n - 1) 
  # This section used for Option 2 below

  # Option 2: use the cache
  if not cache:                        # if cache is empty or nonexistent
    cache = {}                         # make cash an empty dictionary object

  if n not in cache:                   # if cache exists but does not contains n
    cache[n] = climbing_stairs(n - 1, cache) + climbing_stairs(n - 2, cache) + climbing_stairs(n - 3, cache) # return cache value at index n
    
  else:
    return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')