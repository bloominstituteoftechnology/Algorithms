#!/usr/bin/python
import sys

def climbing_stairs(n, cache=None):
  '''
  function description: 
    function that counts the number of possible ways in which the child can ascend the staircase. 
    child can hop 1, 2, or 3 steps at a time

  pseudo code:
    - note: similar to fibonacci 
    - base case (handles 0, handles negatives)
    - have options that represents hops 1, 2, and 3
    - hint from testing: [0 for i in range()]
  '''
  # handles negatives
  if n < 0:
    return 0
  # handles 0 and 1 (included 1 since it'll be 1 anyways)
  elif n <= 1:
    return 1
  # checks that there is a cache
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    # if there is no cache it'll create one
    if not cache:
      # range (inclusive) in the cache array
      cache = [0 for i in range(n+1)]
    # handles the 3 options of hops (1, 2, 3 hops)
    cache[n] = climbing_stairs(n-1, cache) + climbing_stairs(n-2, cache) + climbing_stairs(n-3, cache)
    return cache[n]



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')