#!/usr/bin/python

import sys

# Formula: if denomination <= amount,
# ways[amount] += ways[amount - denomination]
# Runs in O(nd) time where n is the amount and d is denominations
# and has O(n) space complexity because we create a new array


def making_change(amount, denominations):
    # Create an array of zeros to track number of ways to make change
    ways = [0 for i in range(amount + 1)]
    # Initialize ways[0] as 1 as base case
    ways[0] = 1
    # For each denomination:
    for denom in denominations:
        # Create a range from 1 to amount + 1
        for amt in range(1, amount + 1):
            # Confirm the denomination is less than or equal to
            # the current amt
            if denom <= amt:
                # Increment at that amt position in the ways array
                ways[amt] += ways[amt - denom]
    return ways[amount]


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
