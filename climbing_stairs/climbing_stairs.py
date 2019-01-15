#!/usr/bin/python

import sys
# count = 0
# x = 0
def climbing_stairs(n, cache={}):
  #nCr = n!/r!(n-r)!

  if n < 0:
    return 0
  if n == 0:
    return 1
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 4
  if n == 4:
    return 7

  if n in cache:
    return cache[n]

  nth = climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)
  cache[n] = nth
  return nth




          
            

    



  pass 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')