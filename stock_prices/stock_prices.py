#!/usr/bin/python

import argparse


def find_max_profit(prices):
    profit = []

    for i, num1 in enumerate(prices):
        min_price = num1
        for j, num2 in enumerate(prices):
            if j <= i:
                continue
            else:
                max_price = num2
                profit_margin = max_price - min_price
                profit.append(profit_margin)
    return max(profit)


# print(find_max_profit([13, 43, 8, 34, 4, 54]))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
