#!/usr/bin/python

import sys

#n = number of stairs in ascending staircase
#hop options = hop either 1, 2, or 3 steps at a time

def climbing_stairs(n, cache=None):
  
  if n == 0:
      return 1
  
  elif n < 0:
      return 0


n = 6 
print(climbing_stairs(n))

'''
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')'''