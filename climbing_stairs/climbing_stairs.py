#!/usr/bin/python

import sys

#find results such that sum(results) = n
# find combos = the different combinations of results

def climbing_stairs(n):
  # if n == 0 or n < 0:
  #   print(0)
  # elif n == 1:
  #   print(1)
  # elif n == 2:
  #   print(2)
  # else:
  a = climbing_stairs(n - 1) + climbing_stairs(n - 2) + climbing_stairs(n - 3)
  print(a)

climbing_stairs(4)

# def climbing_stairs(n, cache=None):
#   pass

# def()

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_stairs = int(sys.argv[1])
#     print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
#   else:
#     print('Usage: climbing_stairs.py [num_stairs]')
