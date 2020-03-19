#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# cache is the inventory --> 4 cookies
# n is for cookies

def eating_cookies(n, cache=None):
  # starter
  # base:
  if not cache:
    cache = [0]*(n+1)
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif cache[n] > 1:
    return cache[n]
  else:
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

def eating_cookies2(n, cache=None):
  # starter
  # base:

  if n <= 0:
    return 0
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 4

  return eating_cookies2(n-1) + eating_cookies2(n-2) + eating_cookies2(n-3)
# lines 41 and 42 debug eating cookies2 and it works on small numbers
n=3
print(eating_cookies2(n-1) + eating_cookies2(n-2) + eating_cookies2(n-3))

def eating_cookies3(n, cache=None):
  # starter
  if cache is None:
    cache = {}
  # base:

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  elif cache and cache[n]:
    return cache[n]
  else:
    cache[n] = eating_cookies3(n-1, cache) + eating_cookies3(n-2, cache) + eating_cookies3(n-3, cache)
  

  return cache[n]
y = eating_cookies3(400, {})
print(y)
        


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')