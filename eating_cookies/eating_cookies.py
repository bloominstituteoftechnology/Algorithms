#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, yeet=None):
  if n <= 0:
    return 1
  elif n == 1 :
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  elif yeet and yeet[n] > 0:
    return yeet[n]
  else:
    if not yeet:
      yeet = {i: 0 for i in range(n+1)}
    yeet[n] = eating_cookies(n-1, yeet) + eating_cookies(n-2, yeet) + eating_cookies(n-3, yeet)
    return yeet[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')