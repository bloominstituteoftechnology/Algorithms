#!/usr/bin/python

# 1. Understand the problem
# Can eat 1, 2, or 3 cookies at a time.
# if 0 return 1
# Fibonacci esq?
# caching

# 2. Create a Plan
# Create base cases

# 3. Implement Plan
# at first without caching

# 4. Revise
# Caching to pass the large tests, without it solution is too slow to compute tests.

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
# Without Caching.
# if n == 0:
#   return 1
# elif n <= 2:
#   return n
# else:
#   return(eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))

# With Caching
  if n == 0:
    return 1
  elif n <= 2:
    return n
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if not cache:
      cache = {i: 0 for i in range(n+1)}
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]


# print(eating_cookies(1))
# print(eating_cookies(4))
# print(eating_cookies(10))




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

# Attempt Number: 1
# def eating_cookies(n, cache=None):
# if n < 0:
  #   return -1
  # elif n == 0:
  #   return 1
  # elif n == 1:
  #   return 1
  # elif n == 2:
  #   return 2
  # else:
  #   return(eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))

#Attempt Number: 2. Passes small test, probably passes large but runs too slowly to find out.
# def eating_cookies(n, cache=None):
# if n == 0:
#   return 1
# elif n <= 2:
#   return n
# else:
#   return(eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))