#!/usr/bin/python

import argparse


def find_max_profit(prices):

    # set default of prices to SOMETHING. if there is no possible
    # positive nums, this sets to a negative to compare with
    highest_dif = prices[1] - prices[0]

    # essentially just a bubble sort
    for i in range(len(prices)):
        # check for highest earning
        for j in range(i, len(prices)):

            # need to make sure not to compare same indexes because this
            # will always return 0 if best case senario is a loss
            if j == i:
                highest_dif = highest_dif
            elif prices[j] - prices[i] > highest_dif:

                highest_dif = prices[j] - prices[i]

    print(highest_dif)
    return highest_dif


find_max_profit([10, 7, 5, 8, 11, 9])  # 6
find_max_profit([100, 90, 80, 50, 20, 10])  # -10
find_max_profit([1050, 270, 1540, 3800, 2])  # 3530
find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43,
                 11, 47, 67, 89, 42, 49, 79])  # 94

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
