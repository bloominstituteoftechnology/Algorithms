#!/usr/bin/python

import argparse
import sys


def find_max_profit(prices):
    max_profit = float("-inf")
    for index, selling_price in enumerate(prices):
        for buying_index in range(index):
            profit = float(selling_price - prices[buying_index])
            if profit > max_profit:
                max_profit = profit
    return int(max_profit)

print(find_max_profit([1050, 270, 1540, 3800, 2]))  # should return 3530

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.'
    )
    parser.add_argument(
        'integers',
        metavar='N',
        type=int,
        nargs='+',
        help='an integer price')
    args = parser.parse_args()

    print(
        "${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(prices=args.integers)
        )
    )
