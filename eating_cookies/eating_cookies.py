#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache={}):
  # special cases
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

  # top down dynamic solution
  if n not in cache:
    # cache[4] = 4 + 2 + 1 = 7 
    # cache[5] = 7 + 4 + 2 = 13
    cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


  return cache[n]





if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')