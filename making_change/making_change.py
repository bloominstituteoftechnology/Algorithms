#!/usr/bin/python

import sys

cache = {}

denominations = {
  'p': 1,
  'n': 5,
  'd': 10,
  'q': 25,
  'h': 50
}

def making_change(n, d = denominations):
  global cache

  if n in cache:
    return cache[n]

  elif n == 0:
    return 1

  elif n < 5:
    result = making_change(n - d['p'])
    cache[n] = result
    return result

  elif n < 10 and n >= 5 :
    result = making_change(n - d['p']) + making_change(n - d['n'])
    cache[n] = result
    return result

  elif n < 25 and n >= 10 :
    result = making_change(n - d['p']) + making_change(n - d['n']) + making_change(n - d['d'])
    cache[n] = result
    return result

  elif n < 50 and n >= 25 :
    result = making_change(n - d['p']) + making_change(n - d['n']) + making_change(n - d['d']) + making_change(n - d['q'])
    cache[n] = result
    return result

  else:
    result = making_change(n - d['p']) + making_change(n - d['n']) + making_change(n - d['d']) + making_change(n - d['q']) + making_change(n - d['h'])

# if __name__ == "__main__":
#   # Test our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
#     denominations = [1, 5, 10, 25, 50]
#     amount = int(sys.argv[1])
#     print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
#   else:
#     print("Usage: making_change.py [amount]")

print(making_change(20))