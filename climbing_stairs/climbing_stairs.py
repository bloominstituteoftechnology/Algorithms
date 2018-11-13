#!/usr/bin/python

import sys
thing = {}
thing[0] = 0
thing[1] = 1
thing[2] = 2
 
def climbing_stairs(n, cache=None):
  
  if n==0 or n==1:
    return 1

  if n==2:
    return 2

 
  
  if n not in thing:
    thing[n] = climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)
  
  return thing[n]





if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')