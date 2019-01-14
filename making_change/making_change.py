#!/usr/bin/python

import sys
amount = 30
denominations =[1,5,10,25,50]

def making_change(amount, denominations):

  if amount >= 25 and amount <= 50:
    x = round((amount/5)/2)

    y = (amount/25)
    z = round(amount/25)
    xx = y - z
    xy = xx(25)

    combos = xy + x
    return combos
  else:
    return (print("not in range"))

making_change(amount, denominations)

'''
if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")'''