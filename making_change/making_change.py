#!/usr/bin/python

import sys


def making_change(change, denominations=[1, 5, 10, 25, 50]):
    if change == 0:
        return 1
    elif change < 0:
        return 0

    return making_change(change-50, [1, 5, 10, 25]) + making_change(change-25, [1, 5, 10, 50]) + making_change(change-10, [1, 5, 25, 50]) + making_change(change-5, [1, 10, 25, 50]) + making_change(change-1, [5 10, 25, 50])


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
