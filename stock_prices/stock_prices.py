#!/usr/bin/python

import argparse


def find_max_profit(prices):
    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
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


# find_max_profit([10, 7, 5, 8, 11, 9])  # 6
# find_max_profit([100, 90, 80, 50, 20, 10])  # -10
# find_max_profit([1050, 270, 1540, 3800, 2])  # 3530
# find_max_profit(
#     [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79])  # 94
