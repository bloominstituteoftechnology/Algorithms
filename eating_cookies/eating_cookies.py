#!/usr/bin/python

import sys
# from numpy import roots, flip

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache = None):
  # Note: this program should work fine, in theory, but Numpy's implementation of root
  # finding builds up floating-point errors too fast. It gives the wrong answer for 0,
  # and it reliably gives almost, but not quite, correct answers on large values.
  # int(round(sum(roots([1, -1, -1, -1]) ** (n + 2) * flip(roots([44, 0, 4, -1])))))

  # this function passes all tests when implemented in Mathematica, however
  # eatingCookies[n_] := 
  #    Round[Inner[Times, 
  #      Array[Root[-1 - # - #^2 + #^3 &, #] &, 3]^(n + 2), 
  #      Array[Root[-1 + 4*# + 44*#^3 &, #] &, 3], Plus]]
  # So, clearly, the concept is fine, but Python's libraries aren't.

  if n < 2:
    return 1
  elif n == 2:
    return 2

  if cache == None:
    cache = [None] * (n + 1)
  else:
    cache = cache

  if cache[n] == None or cache[n] == 0:
    cache[n - 3] = eating_cookies(n - 3, cache)
    cache[n - 2] = eating_cookies(n - 2, cache)
    cache[n - 1] = eating_cookies(n - 1, cache)

    return cache[n - 1] + cache[n - 2] + cache[n - 3]
  else:
    return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')