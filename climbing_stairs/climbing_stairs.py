#!/usr/bin/python

import sys

cache = {}

def climbing_stairs(n, c = None):
  global cache

  if n in cache:
    return cache[n]
  
  elif n == 0:
    return 1

  elif n == 1:
    result = climbing_stairs(n - 1)
    cache[n] = result
    return result

  elif n == 2:
    result =  climbing_stairs(n - 1) + climbing_stairs(n - 2)
    cache[n] = result
    return result


  elif n >= 3:
    result = climbing_stairs(n - 1) + climbing_stairs(n - 2) + climbing_stairs(n - 3)
    cache[n] = result
    return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')

# print(climbing_stairs(50)) # 10562230626642

# Initial thoughts, after Beej's demonstration of doing
# fibonnaci with cache, getting a sppedy result was pretty
# straight foreward

# to summarize before we calculate a result we check to see
# if it has been calculated before. If not pass it to
# 1,2,or 3 recursions. Everytime a new result is calculated
# store it in cache.

# this way the function only needs to be concerned with how to calculate
# 1, 2, and 3 since 3 is the maximum number of steps.

# everytime the function gets down to 0 it returns a 1.
# each 1 returned is a possibility.