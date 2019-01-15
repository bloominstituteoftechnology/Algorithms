#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
    
#  if n <= 0:
#    return 0
#  elif n == 1:
#    return 1
#  elif n == 2:
#    return 2
#  elif n == 3:
#    return 4
#  else:
#    return climbing_stairs(n - 1) + climbing_stairs(n - 2) + climbing_stairs(n - 3)
    
  # If n is too large, it takes a long time to compute.
  # Want to cache the results of the previous numbers
  
  # Check if cache exists, make one if it doesn't
  # If the cache does contain our number, but it's cached value is 0, then throw the whole cache away - it is incompatible with this algorithm
#  local_cache = cache
#  if local_cache == None or (len(local_cache) > n and local_cache[n] == 0):
#    local_cache = []
#    
#    
#  if n <= 0:
#    return 1
#  elif n == 1:
#    return 1
#  elif n == 2:
#    return 2
#  elif n == 3:
#    return 4
#  else:
#    # Check the cache if value exists at index n  
#    if len(local_cache) > n-4:
#      return local_cache[n-4]
#    
#    # The value for a given number of steps seems to be equal to the number of ways you can solve make 1 step and (n-1) steps, make 2 steps and (n-2) steps, or make 3 steps and (n-3) steps
#    value = climbing_stairs(n - 1, cache = local_cache) + climbing_stairs(n - 2, cache = local_cache) + climbing_stairs(n - 3, cache = local_cache)
#    local_cache.append(value)
#    return value
  
  if n <= 0:
    return 1
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else:
    local_cache = cache
    if local_cache == None:
      local_cache = [0 for i in range(n+1)]
      
    # Check the cache if value exists at index n
    cached_value = local_cache[n]
    if cached_value != 0:
      return cached_value
    
    # The value for a given number of steps seems to be equal to the number of ways you can solve make 1 step and (n-1) steps, make 2 steps and (n-2) steps, or make 3 steps and (n-3) steps
    value = climbing_stairs(n - 1, cache = local_cache) + climbing_stairs(n - 2, cache = local_cache) + climbing_stairs(n - 3, cache = local_cache)
    local_cache[n] = value
    return value
    

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]') 