#!/usr/bin/python

import sys


def making_change_nocache(amount, denominations):
    if amount < 0:
        return 0
    if amount <= 4:
        return 1
    if amount <= 9:
        return 2

    return (making_change(amount - denominations[0], denominations) +
            making_change(amount - denominations[1], denominations) +
            making_change(amount - denominations[2], denominations) +
            making_change(amount - denominations[3], denominations) +
            making_change(amount - denominations[4], denominations))


def making_change(amount, denominations):
    cache = [0 for i in range(amount + 1)]
    cache[0] = 1
    for higher_amount in range(1, amount + 1):
        cache[higher_amount] += cache[higher_amount - 1]
    for higher_amount in range(5, amount + 1):
        cache[higher_amount] += cache[higher_amount - 5]
    for higher_amount in range(10, amount + 1):
        cache[higher_amount] += cache[higher_amount - 10]
    for higher_amount in range(25, amount + 1):
        cache[higher_amount] += cache[higher_amount - 25]
    for higher_amount in range(50, amount + 1):
        cache[higher_amount] += cache[higher_amount - 50]

    return cache[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
