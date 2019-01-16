#!/usr/bin/python

import sys

def making_change(amount, denominations, cache={}):
    """
    # If amount is 0 then there is 1 solution
    if amount == 0:
        return 1

    # If amount is < 0 there is no solution
    if amount < 0:
        return 0

    # If there are no denominations but there is an amount,
    # there is no solution
    if denominations == [] and amount > 0:
        return 0
    
    # if amount in cache:
        # return cache[amount]
    
    after_last_denom = making_change(amount - denominations[-1], denominations, cache)
    without_last_denom = making_change(amount, denominations[:-1], cache)
    
    cache[amount] = after_last_denom + without_last_denom
    
    return after_last_denom + without_last_denom
    """

    """for cents in range(amount+1):
        coinCount = cents
        for j in [c for c in denominations if c <= cents]:
                if minCoins[cents-j] + 1 < coinCount:
                    coinCount = minCoins[cents-j]+1
        minCoins[cents] = coinCount
    return minCoins[amount]"""

    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denominations) == 0:
        return 0

    return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")