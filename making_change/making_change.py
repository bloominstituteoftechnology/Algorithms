#!/usr/bin/python

import sys

denominations = [1, 5, 10, 25, 50]


def making_change(amount, denominations, denoms_used):
    if sum(denoms_used) == amount:
        yield denoms_used
    elif sum(denoms_used) > amount:
        pass
    elif denominations == []:
        pass
    else:
        for d in making_change(amount, denominations[:], [denoms_used[0]]):
            yield d
        for d in making_change(amount, denominations[1:], denoms_used):
            yield d

        # allWays = []
        # eachWay = []
        # while amount >= 0:
        #     for i in range(len(denominations), 0, -1):
        #         if amount >= denominations[i - 1]:
        #             eachWay.append(denominations[i - 1])
        #             amount - denominations[i - 1]

        # allWays.append(eachWay)
        # return allWays


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
