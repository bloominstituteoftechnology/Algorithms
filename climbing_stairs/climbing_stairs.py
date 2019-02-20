#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  # A Total of 3 steps has 4 different combinations
  if n == 3:
    return 4
  # A Total of 2 steps has 2 different combinations
  if n == 2:
    return 2
  # A Total of 1 and 0 steps has 1 different combinations
  if n <= 1:
    return 1

  return climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)


print(f"Answer: {climbing_stairs(10)}")

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')