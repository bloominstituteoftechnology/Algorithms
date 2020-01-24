#!/usr/bin/python

import sys

# sys.setrecursionlimit(100000)

# Recursion - really really bad
#
# def making_change(amount, denominations):
#     if amount == 0:
#         return 1
#     if amount < 0 or (len(denominations) <= 0 and amount > 0):
#         return 0
#     else:
#         return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])


# with helper function+stack better, but still awful for bignums
def making_change(amount, denominations):
    dlength = len(denominations)

    def change_helper(stack: []):
        nonlocal dlength
        possibilities: int = 0
        while stack:
            nonlocal amount
            nonlocal denominations
            nonlocal dlength
            amount, dlength = stack.pop()
            if amount == 0:
                possibilities += 1

            if amount > 0 and dlength > 0:
                stack.append((amount, dlength - 1))
                stack.append((amount - denominations[dlength - 1], dlength))

        return possibilities

    return change_helper([(amount, len(denominations))])


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations),
                                                                     amount=amount))
    else:
        print("Usage: making_change.py [amount]")
