#!/usr/bin/python

import sys

# def making_change(amount, denominations):
#     # so we can easily use recusion here by
#     # decrementing the amount while removing coinage from denominations
#     # base cases
#     #this works for the small test
#     if amount == 0:
#         return 1
#     if amount < 0:
#         return 0
#     # out of coins
#     if len(denominations) == 0 and amount > 0:
#         return 0
#     else:
#         return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])

def making_change(amount, denominations):
    cache = [0 for i in range(amount +1)]
    cache[0] = 1

    # pick a coin from the denominations list and loop over:
    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            remainder = higher_amount - coin
            # higher_amount is the coin here
            cache[higher_amount] += cache[remainder]

    return cache[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
