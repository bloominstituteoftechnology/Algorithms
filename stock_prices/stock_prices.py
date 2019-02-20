#!/usr/bin/python

import argparse


def find_max_profit(prices):
    profit = 0
    loss = 0
    difference = 0
    while len(prices) > 0:
        for num in range(len(prices)):
            difference = prices[num] - prices[0]
            if difference > profit:
                profit = difference
            if difference < profit:
                loss = difference
        del prices[0]
        if profit == 0:
            return loss
        return profit


myPrices = [100, 90, 80, 50, 20, 10, 200]
print(find_max_profit(myPrices))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
