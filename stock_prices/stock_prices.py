#!/usr/bin/python

import argparse
import math


def find_max_profit(prices):
    # max profit variable start at initial index and compare
    # min price make it index independent
    max_profit = -math.inf
    min_price = math.inf
    for price in prices:
        max_profit = max(price - min_price, max_profit) # -inf, -780, 1270, 3530, 3530
        min_price = min(price, min_price) # 1050, 270...
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
