#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # First Pass
  amount_list = []

  if amount == 0:
    return 1

  def change_making(amount, coins = [], final = None):
    if amount < 0:
      return []
    if amount == 0:
      return coins
    return change_making(amount-1, coins + ['1']) + change_making(amount-5, coins + ['5']) + change_making(amount-10, coins + ['10']) + change_making(amount-25, coins + ['25']) + change_making(amount-50, coins + ['50'])

  unfiltered = list(change_making(amount))
  count = 0
  to_add = []

  for coin in unfiltered:
    count += int(coin)
    if count < amount:
      to_add.append(coin)
    elif count == amount:
      to_add.append(coin)
      to_add.sort()
      if to_add not in amount_list:
        amount_list.append(to_add)
      to_add = []
      count = 0

  return len(amount_list)


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")