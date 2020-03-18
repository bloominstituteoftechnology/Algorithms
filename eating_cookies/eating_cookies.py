#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# cache is the inventory --> 4 cookies
# n is for cookies

def eating_cookies(n, cache=None):
  # starter
  combinations = 0

  # base
  if n == 0:
    combinations += 1
    return combinations
    # check if inventory has items:
  if cache is not None:
    if cache[n] > 0:
      return cache
  if n >= 3:
    combinations = eating_cookies(n-3, cache)
    if cache is not None:
      cache[n] = combinations
  if n >= 2:
    combinations = eating_cookies(n-2, cache)
    if cache is not None:
      cache[n] = combinations
  if n >= 1:
    combinations = eating_cookies(n-1, cache)
    if cache is not None:
      cache[n] = combinations

  return combinations            

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')