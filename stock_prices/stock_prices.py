#!/usr/bin/python

import argparse


def find_max_profit(prices):

    lowest = prices[0]  # base for initial buying, 1st number in array
    maxProfit = prices[1] - prices[0]  # compare to get base max profit
    index = 2

    while True:
        if index > len(prices):  # if index is less than total length of array, exit
            break
        for price in prices[index-1:]:
            # starting at beginning of array, compares initial ( or current) prices to next day to see profit margin,
            # if larger than base maxProfit, make new maxProfit.
            if price - lowest > maxProfit:
                maxProfit = price - lowest
        lowest = prices[index-1]
        index += 1  # increment index to advance through array
    return maxProfit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
