#!/usr/bin/python

import argparse


def find_max_profit(prices):
    profitsofar = prices[1] - prices[0]
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices) - 1):
            if(prices[j] - prices[i] > profitsofar):
                profitsofar = prices[j]-prices[i]

    return profitsofar


print(find_max_profit([1050, 270, 1540, 3800, 2]))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
