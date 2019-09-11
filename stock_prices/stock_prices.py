#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # For each of our stock prices we want to
    #  Loop through the rest of the stock prices going forward and calculate best profit
    best_profit = None

    # [5, 2, 6, 8]
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if best_profit is None:
                best_profit = prices[j] - prices[i]
                break
            if prices[j] - prices[i] > best_profit:
                best_profit = prices[j] - prices[i]

    return best_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
