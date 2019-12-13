#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  #BASE CASES
  if n < 0: return 0
  if n == 0: return 1
  if n == 1: return 1
  
  return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

cache = {}

def recursion(n):
  #BASE CASES
  if n < 0: return 0
  if n == 0: return 1
  if n == 1: return 1
  
  if n not in cache:
	  cache[n] = recursion(n-1) + recursion(n-2) + recursion(n-3)

  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')