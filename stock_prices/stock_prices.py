#!/usr/bin/python

import argparse
import math


def find_max_profit(prices):
    profit = float("-inf")

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]

    return profit


print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )