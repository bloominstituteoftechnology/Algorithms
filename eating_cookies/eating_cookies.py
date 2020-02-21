#!/usr/bin/python

# 0: eat 0 cookies 1 time 
# 1: eat 1 cookie 1 time 
# 2: eat 1 cookie 1 time 
# 2: eat 2 cookies 
# 3: eat 1 cookie 1 time, eat 1 cookie 1 time, eat 1 cookie 1 time

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n < 0: 
    return 0 
  if n == 0:
    return 1 
  elif cache and cache[n] > 0:
      return cache[n]
  else: 
    if cache is None: 
      cache = {}
    value = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    cache[n] = value
    return value 
    
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')