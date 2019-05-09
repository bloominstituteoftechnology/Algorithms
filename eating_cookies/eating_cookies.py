#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cash=None):
    if n < 0:
      return 0
    elif n == 0 or n == 1: 
      return 1
    elif n == 2:
      return 2
    elif cash and cash[n] > 0:
      return cash[n]
    else:
      if not cash:
        cash = {i: 0 for i in range(n+1)}
      answer = eating_cookies(n-1, cash) + eating_cookies(n-2, cash) + eating_cookies(n-3, cash)
      cash[n] = answer
      return cash[n]
  
print(eating_cookies(555))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')