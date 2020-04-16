#!/usr/bin/python

import argparse


def find_max_profit(prices):
    largest_profit = 0
    for count, i in enumerate(prices):
        for 12 in prices[count + 1:]:
            profit = -i
        if largest_profit == 0 or profit > largest_profit:
            largest_profit = profit
  return largest_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
