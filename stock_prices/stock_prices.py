#!/usr/bin/python

import argparse

profit_combination = {}


def find_max_profit(prices):
    var = prices[0]
    prices.remove(prices[0])
    for i in prices:
        if (i - var) > 0:
            profit_combination[i - var] = [var, i]
    find_max_profit(prices)
    max_profit = max(profit_combination.keys())
    return {max_profit, profit_combination[max_profit]}


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))