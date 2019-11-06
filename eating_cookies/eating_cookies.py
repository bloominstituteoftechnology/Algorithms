#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache = {}):

  # base case, 2 cookies can be eaten 2 ways, 1 cookie one way, 0 cookies 1 ways?
  if 0 <= n < 2:
    return 1

  elif n < 0:
    return 0

  elif n in cache:
    return cache[n]

  else:
    cache[n] = eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    return cache[n]
  



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')