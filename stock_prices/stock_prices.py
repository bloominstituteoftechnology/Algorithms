#!/usr/bin/python

# - Find the max profit by getting the biggest difference in prices
# must buy before selling so cannot justt use min and max
# - Find max price then split the array to the left of that point
# - Find the min of the array to the left and that min to the max should
# be the biggest profit for the left side of the list
# - Repeat for the right array and so on

import argparse


def find_max_profit(prices):
    reversed_list = list(reversed(prices))
    profit = 00
    print(reversed_list)
    for i, num in enumerate(reversed_list):
        right_list = reversed_list[i+1:]
        idx2 = 0
        while idx2 < len(right_list):
            num2 = right_list[idx2]
            diff = num - num2

            if diff > profit or profit == 00:
                profit = diff

            idx2 += 1
    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
