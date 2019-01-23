#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  if n == 0:
    return 0
  else:
    return n + 1 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')

    print(climbing_stairs(3))

    # visualize steps
    # 4 steps = 1 big step, 3 steps and 1 step, 2 steps and 2 steps, 1 step and 3 steps, 4 steps