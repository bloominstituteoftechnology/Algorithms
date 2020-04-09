#!/usr/bin/python

def making_change(amount, denominations):

    return get_combinations(amount, denominations)
    # if you can subtract down to 0, return 1. Because that's one possibility
    # if it's < 0 return 0 because it doesn't match
    # for coin in array of coins, subtract the amount of the coin from the remaining and add the result to possible ways


def get_combinations(amount, denominations, index=0):
    total_ways = 0

    if amount == 0:
        return 1
    if amount < 0:
        return 0

    for current_index in range(index, len(denominations)):
        new_amount = amount - denominations[current_index]
        total_ways += get_combinations(new_amount, denominations, current_index)

    return total_ways


import sys
"""
20
    10
        0
    10
        5
        5
"""



print(making_change(6, [1, 5, 10, 25, 50]))

# if that combo.sort() not in dict, increase count






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
