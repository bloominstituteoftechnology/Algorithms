#!/usr/bin/python

import argparse


def find_max_profit(prices):
    if len(prices) < 2:
        return 0
    max = prices[1] - prices[0]
    min_seen = prices[0]
    p_iter = iter(prices)
    next(p_iter)
    for price in p_iter:
        if (price - min_seen) > max:
            max = price - min_seen
        if price < min_seen:
            min_seen = price
    return max


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
