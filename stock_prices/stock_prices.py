#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit = 0
    

    for index, first_num in enumerate(prices):
        for second_num in prices[index + 1:]:
            profit = second_num - first_num
            if max_profit == 0 or profit > max_profit:
                max_profit = profit
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
