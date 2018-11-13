#!/usr/bin/python

import sys
# my main issue was had to look up US denominations of money : https://en.wikipedia.org/wiki/Coins_of_the_United_States_dollar#Coins_in_circulation
# going to use a chace to help with lookup hopefully will be a good enough for the test cases it is quite slow at 0.033s for 2 tests

def making_change(amount, denominations):
    # create a cache for this set the cache = a list of [0] + the ammount + 1 in case of a zero input
    cache = [0] * (amount + 1)

    # set the index of zero to 1
    cache[0] = 1 

    #using a nested for loop and adding to the cache
    # loop over the denom in denominations
    for denom in denominations:
        # inner loop - upper in range of denom to ammount + 1
        for upper in range(denom, amount+1):
            # set the inner index to the upper - the denom at current outer itteration
            inner_index = upper - denom
            # set increment the cache of upper by the cache of inner_index
            cache[upper] += cache[inner_index]

    # at the end we can return the cache at index of the ammount
    return cache[amount]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")