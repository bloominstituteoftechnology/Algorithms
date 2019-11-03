#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# n === 5
# 3,2
# 3, 1, 1
# 2, 3
# 2, 2, 1
# 2, 1, 1, 1
# 1, 3, 1, 1
# 1, 2, 2
# 1,2, 1, 1
# 1, 1, 1, 1, 1

def eating_cookies(n, cache=None):
  
  #base case
  if n < 0:
    return 0
  elif n == 0:
    return 1
  
  cache = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
  return cache
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')