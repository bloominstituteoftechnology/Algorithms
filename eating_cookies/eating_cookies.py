#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):

  # Solution Without Cache
  # if n == 0:
  #   return 1
  # elif n < 0:
  #   return 0
  # else:
  #   return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

  # Solution With Cache
  if n == 0:
    return 1
  elif n < 0:
    return 0
  elif cache == None:
    cache = {i: 0 for i in range(n+1)}
    eating_cookies(n, cache)
  else:
    if cache[n] > 0:
      return cache[n]
    else:
      cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
  return cache[n]

# print(eating_cookies(5))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')