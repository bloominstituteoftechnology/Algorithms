#!/usr/bin/python
import sys
#cache holds previous values
def climbing_stairs(n, cache=None):
  if n <=  1:
    return 1
  if n == 2: 
    return 2
  if n == 3:
    return 4
  return climbing_stairs(n - 1) + climbing_stairs(n-2) + climbing_stairs(n-3)
  # nth = climbing_stairs(n - 1) + climbing_stairs(n-2) + climbing_stairs(n-3)
  # cache[n] = nth
  # return nth

# if n is 0 theres one way to climb it
# 2 steps from theres only 2 ways = n - 2 steps
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')