#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  ways = 0
  num_stairs = n
  if(num_stairs > 0):
    if (num_stairs%3==0):
      ways += 1
      print("hello1")
    if (num_stairs%2==0):
      ways += 1
      print("hello2")
    if (num_stairs%1==0):
      ways += 1
      print("hello3")
    if (num_stairs%3==2):
      ways += 1
      print("hello4")
    if (num_stairs%2==1):
      ways += 2
      print("hello5")
  elif (num_stairs==0):
    ways += 1
  print(ways)

climbing_stairs(97)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')