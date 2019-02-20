#!/usr/bin/python

import sys

total = 0


def making_change(change, denominations=[1, 5, 10, 25, 50]):
    global total
    if change == 0:
        return 1
    if change < 0:
        return 0
    if len(denominations) == 1:
        return 1

    return making_change(change-denominations[-1], denominations) + \
        making_change(change, denominations[:-1])


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
