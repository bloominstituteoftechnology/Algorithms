#!/usr/bin/python

import argparse
import sys


def find_max_profit(prices):
    # O(n^2)
    """
    max_profit = float("-inf")
    for index, selling_price in enumerate(prices):
        for buying_index in range(index):
            profit = float(selling_price - prices[buying_index])
            if profit > max_profit:
                max_profit = profit
    return int(max_profit)
    """

    # O(n^2)
    """
    max_profit = float("-inf")

    while prices != []:
        bought = prices[0]

        for p in prices[1:]:
            profit = p - bought
            max_profit = max(max_profit, profit)

        prices.pop(0)

    return max_pofit
    """

    # O(n)
    min_buy_price = prices[0]
    max_profit = prices[1] - min_buy_price

    for price in prices[1:]:
        profit = price - min_buy_price
        max_profit = max(max_profit, profit)
        min_buy_price = min(min_buy_price, price)

    return max_profit


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
            profit=find_max_profit(prices=args.integers),
            prices=args.integers
        )
    )
