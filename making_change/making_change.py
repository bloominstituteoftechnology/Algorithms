#!/usr/bin/python

import sys

def making_change(amount, denominations= [1, 5, 10, 25, 50]):
  if amount == 0 or amount == 1:
    return 1
  count = [0] * (amount + 1)
  count[0] = 1
  for coin in denominations:
    for j in range(coin, amount + 1):
        count[j] += count[j - coin]
        print(count)
  return(count[amount])

print(making_change(10))

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")