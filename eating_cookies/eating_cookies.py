#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n <= 0 :
    return 1
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else:
    locally_cached = cache
    if locally_cached is None:
      locally_cached = [0 for i in range(n+1)]
      cached_value = locally_cached[n]
      if cached_value != 0:
        return cached_value

    cookies = eating_cookies(n-1, cache = locally_cached) + eating_cookies(n-2, cache=locally_cached) + eating_cookies(n-3, cache= locally_cached)
    locally_cached[n] = cookies
    return cookies

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')