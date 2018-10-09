#!/usr/bin/python

import sys

def making_change(amount, denominations):
  pass 
# USD - $1, $5, $10, etc.
currency = [1, 5, 10, 20, 50, 100]

# the amount to change - $120
amount = 120


minimum_number_of_currency = [0]
currency_composition = [[]]

for i in xrange(1, amount + 1):
    best = 10000
    currenncyCombo = None

    for j in currency:
        if i - j > -1 and minimum_number_of_currency[i - j] + 1 < best:
            best = minimum_number_of_currency[i - j] + 1
            currencyCombo = currency_composition[i - j] + [j]

    minimum_number_of_currency.append(best)
    currency_composition.append(currencyCombo)

    print '{0:3} {1} {2}'.format(i, best, currencyCombo)

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
