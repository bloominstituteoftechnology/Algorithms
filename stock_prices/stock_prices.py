#!/usr/bin/python

import argparse

# first find all possible profits
# - prices[1] - [prices 0], prices[2]- prices[0], prices[3] - prices[0], prices[4] - prices[0]
##  prices[2] - prices[1], prices[3] - prices[1], prices[4] - prices[1]


def find_max_profit(prices):
    maxProfit = 0
    i = 0
    for i in range(len(prices) - 1):
        i += 1
        profit = (prices[i] - prices[i-1])
        print(profit)


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
