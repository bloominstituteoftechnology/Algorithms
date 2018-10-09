#!/usr/bin/python

import sys


def making_change(amount, denominations):
    m = len(denominations)
    table = [0 for x in range(amount + 1)]
    table[0] = 1
    # Fill the entries for 0 value case (n = 0)

    # Fill rest of the table entries in bottom up manner
    for i in range(m):
        for j in range(denominations[i], amount + 1):
            print('what is j', j)
            print('what denominations[i]', denominations[i])
            print('value added to j', table[j - denominations[i]])
            table[j] += table[j - denominations[i]]
            print(table, '\n')

    return table[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
