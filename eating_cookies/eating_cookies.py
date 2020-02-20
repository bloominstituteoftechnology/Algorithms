#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n):
    if n < 0:
        return 0
    elif n == 0 :
        return 1
    else:
        a = eating_cookies(n-1)
        b = eating_cookies(n-2)
        c = eating_cookies(n-3)
        total = a + b + c
        return total

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')