#!/usr/bin/python

import argparse


def find_max_profit(prices):

    diff = 0
    for i, price in enumerate(prices):
        for nextPrice in prices[i+1:]:
            # profit
            if(nextPrice-price > 0):
                if (nextPrice-price) > (diff):
                    diff = nextPrice-price
            # loss
            else:
                if (nextPrice-price) > (diff) or diff == 0:
                    diff = nextPrice-price

    return diff


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
