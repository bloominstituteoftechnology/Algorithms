#!/usr/bin/python

import sys


def making_change(amount, denominations):
    count = 0
    total = amount
    reversedDenom = denominations[::-1]
    bc = reversedDenom[0]
    print(reversedDenom)
    count = 0

    def give_change(amount, denominations):
        nonlocal total
        if amount < 1:
            return 0
        elif amount == 1:
            return 1

        elif total < bc:
            reversedDenom.pop(0)
        elif total > bc:
            print(f"{bc} gets subtracted from total. The new total is {total - bc}")
            total -= bc
            return(give_change(total, reversedDenom))

    return give_change(total, reversedDenom)


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
