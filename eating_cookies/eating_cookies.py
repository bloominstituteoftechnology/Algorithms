#!/usr/bin/python

'''
UNDERSTANDING:

- Can eat 0-3 cookies per time
- base case is 0, 1, 2, 3

Pattern:
result of the Nth case is the sum of 3 previous result.

Similar to fibonacci sequence but instead of 2 previous numbers it is the 3 previous numbers
'''

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):

  cache = {}   # Memoization

  def fib_inner(n):
     # O(n)
    nonlocal cache

  # TODO make sure n is non-negative

    # if n == None:
    #   return 1

    if n == 0:
      return 1

    if n == 1:
      return 1
        
    if n < 0:
      return 0

    if n not in cache:
      cache[n] = fib_inner(n-1) + fib_inner(n-2) + fib_inner(n-3)

    return cache[n]

  return fib_inner(n)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')