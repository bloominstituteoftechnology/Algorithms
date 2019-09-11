#!/usr/bin/python

import sys

# For each denomination get the number of ways to make change with that denomination


def making_change(amount, coins, memo=None):
    if memo is None:
        memo = [0] * (amount + 1)
        memo[0] = 1

    if amount <= 1:
        return 1

    if memo[amount] > 0:
        return memo[amount]

    memo[amount] += making_change(amount - 1, coins, memo)

    return memo[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")