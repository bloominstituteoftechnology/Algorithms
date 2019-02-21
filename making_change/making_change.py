#!/usr/bin/python

import sys
from collections import defaultdict


class Cache:
    def __init__(self):
        self.denom_dict = defaultdict(lambda: defaultdict(lambda: None))

    def store(self, denom, input, output):
        self.denom_dict[denom][input] = output

    def retrieve(self, denom, input):
        return self.denom_dict[denom][input]


def making_change(amount, denominations):
    sort_denoms = sorted(denominations)
    return helper(amount, sort_denoms, Cache())


def helper(amount, denominations, cache):
    if amount < 0:
        return 0
    if amount == 0:
        return 1

    else:
        total = 0

        while denominations:
            denom = denominations[-1]
            remaining = amount - denom
            cached = cache.retrieve(denom=denom, input=remaining)
            if cached is None:
                plus = helper(remaining, denominations[:], cache)
                cache.store(denom=denom, input=remaining, output=plus)
            else:
                plus = cached
            total += plus
            denominations.pop()

    return total


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

print(making_change(10, [1, 5, 10, 25, 50]))
