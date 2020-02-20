#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
<<<<<<< HEAD
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
=======
def eating_cookies(n, cache=1):
    if n < 1:
        return cache
    eating_cookies(n-1, cache+1)
    return eating_cookies(n-1, cache+1)
>>>>>>> 6e2db05b8a3f0c76af988dce75cb44b335883fc7

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')