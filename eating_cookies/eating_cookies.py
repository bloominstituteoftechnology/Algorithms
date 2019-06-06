#!/usr/bin/python

import sys

#sys.setrecursionlimit(40010)

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
#def eating_outer(n):
cache = {}
def eating_cookies(n, cache=cache):
  
  if n == 3:
    return 4
  elif n == 2:
    return 2
  elif n <= 1:
    return 1

  if n not in cache:
    cache[n] = eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)

  return cache[n]
  #return eating_cookies(n)  

  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')