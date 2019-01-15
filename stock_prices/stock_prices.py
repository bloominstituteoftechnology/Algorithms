#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # second pass solution
    buy = prices[0]
    sell = 0

    for price in prices[1:]:
        if price < buy and sell < price:
            buy = price

        if buy < price and price > sell:
            sell = price

    max_profit = sell - buy

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices
          {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
