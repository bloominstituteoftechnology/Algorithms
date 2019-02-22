#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit = None  # so that an initial negative value can be recorded
    for i, val in enumerate(prices):
        for j in range(i + 1, len(prices)):
            buy_sell = prices[j] - val
            if max_profit is None or buy_sell > max_profit:
                max_profit = buy_sell
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
