#!/usr/bin/python

import sys

#n = number of stairs in ascending staircase
#hop options = hop either 1, 2, or 3 steps at a time

def countWaysUtil(n,m):

  if n <= 1:
    return n
  res = 0
  i = 1
  while i<=m and i<=n:
    res = res + countWaysUtil(n-i, m) 
    i = i + 1
  return res 

def climbing_stairs(s, m):

  return countWaysUtil(s+1,m)
  
m = 3
s = 5
print(climbing_stairs(s,m))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')