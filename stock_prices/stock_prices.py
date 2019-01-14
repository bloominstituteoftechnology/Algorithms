#!/usr/bin/python

import argparse


def find_max_profit(prices):
    prices = iter(prices)
    least = next(prices)
    yield 0
    for price in prices:
        least = min(least, price)
        yield price - least


# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))


prices = [100, 113, 110, 85, 105, 102, 86,
          63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
print(max(find_max_profit(prices)))
print(max(find_max_profit([1050, 270, 1540, 3800, 2])))
print(max(find_max_profit([10, 7, 5, 8, 11, 9])))
