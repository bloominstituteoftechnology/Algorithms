#!/usr/bin/python

import argparse


def find_max_profit(prices):
    result = float("-inf")
    for index, first in enumerate(prices):
        for compare in prices[index+1:]:
            check = compare - first
            if check > result:
                result = check

    return result

# TODO Complete recursive version
#     max_profit = float("-inf")

#     if len(prices) == 1:
#         print(max_profit)
#         return max_profit

#     create_set(prices, max_profit)


# def create_set(prices, max_profit):
#     if len(prices) == 1:
#         pass
#     else:
#         find_max_set(prices, max_profit)
#         prices.pop(0)
#         create_set(prices, max_profit)


# def find_max_set(setlist, max_profit):
#     temp = setlist.copy()

#     if len(temp) == 1:
#         pass
#     else:
#         check = temp[-1] - temp[0]
#         # print(temp, max_profit, check)
#         if check > max_profit:
#             max_profit = check
#         temp.pop()
#         find_max_set(temp, max_profit)


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

find_max_profit([1050, 270, 1540, 3800, 2])
