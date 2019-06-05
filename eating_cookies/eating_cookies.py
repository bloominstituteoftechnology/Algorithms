#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies_2(n, cache=None):
  o = 0
  if n == 0:
    o += 1
  for i in range(1,3+1):
    if n - i == 0:
      o += 1
    elif n - i > 0:
      o += eating_cookies(n-i)
  return o

def eating_cookies(n, cache=None):
  if n < 2:
    return 1
  elif n == 2:
    return 2
  o = 2
  add_0 = add_1 = 1
  add_2 = 2
  for _ in range(3, n+1):
    o += add_0 + add_1
    add_n = add_0 + add_1 + add_2
    add_0 = add_1
    add_1 = add_2
    add_2 = add_n
  return o

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')