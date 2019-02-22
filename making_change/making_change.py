#!/usr/bin/python

import sys

cache = {}


def making_change(amount, denominations):
  global cache

  if amount in cache:
    return cache[amount]

  elif amount == 0:
    return 1

  else:
    poss_denom = [coin for coin in denominations if coin <= amount]
    # result = making_change(amount - greatest, denominations)
    # print(poss_denom)
    result = 0
    for index in range(0, len(poss_denom)):
      curent_denom = poss_denom[index]
      denoms_for_recursion = poss_denom[:index + 1]

      result += making_change(amount - curent_denom, denoms_for_recursion)

    cache[amount] = result
    print(cache)
    return result

# print(making_change(10, [1,5,10,25,50]))
  

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
