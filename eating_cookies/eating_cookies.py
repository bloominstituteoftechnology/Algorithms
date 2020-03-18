#!/usr/bin/python

import sys

# counter = 0
# cache = {0: 0, 1: 1}
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache={0: 1, 1: 1}):
  if n < 0:
    return 0
  elif n in cache:
    return cache[n]
  else:
    result = eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    cache[n] = result
    return result

  



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')