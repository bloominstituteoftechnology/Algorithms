#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):

  if n in cache:
      return cache[n]

  if n<=0:
      return 1
  # if n ==1:
  #     return 1
  #     cache[1] = 1
  # elif n  == 2:
  #     cache[2] = 2
  #     return 2
  # elif n == 3:
  #     cache[3] = 1 + eating_cookies(2,cache) + eating_cookies(1,cache)
  #     return cache[3]
  # else:
  cache[n] = eating_cookies(n-1,cache)+ eating_cookies(n-2,cache) + eating_cookies(n-3,cache)
  return cache[n]

cache = {1:1, 2:2, 3:4}
print (eating_cookies(0, cache))
print(cache)
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')