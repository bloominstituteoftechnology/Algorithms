#!/usr/bin/python

import argparse
# if x is negative, find the one closest to 0
# if x is positive, find the one farthest from 0.
#example: [10, 7, 5, 8, 11, 9]
# input: [1050, 270, 1540, 3800, 2]


def find_max_profit(prices):
    negative_list = []
    positive_list = []
    for index, x in enumerate(prices):
        if index < len(prices) - 1 and x >= prices[index + 1]:
            negative_list.append(-(x-prices[index+1]))
            negative_list.sort()
        elif index == len(prices)-1:
            break
        else:
            positive_list.append(prices[index+1]-x)
            positive_list.sort()

    print(negative_list)
    print(positive_list)
    if(positive_list == []):
        return negative_list[-1]
    elif(len(positive_list)-1 > 2):
        return positive_list[-1]
    else:
        return sum(positive_list)
    pass


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))