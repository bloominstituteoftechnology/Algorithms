#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache={}):
  # Set up base case for 0 and 1
  if (n <= 1):
    cache[n] = 1
  elif (n == 2): # Set up base case for n = 2
    cache[n] = 2
  elif (n not in cache): # For case n > 2
    cache[n] = eating_cookies(n-1, cache=cache) + eating_cookies(n-2, cache=cache) + eating_cookies(n-3, cache=cache)
  return cache[n] 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
