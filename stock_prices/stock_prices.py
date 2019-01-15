#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # define return profit variable
    profit_list = []
    # iterate through prices
    for i in range(len(prices) - 1):
        # check if current price is more than min(price) right of the current price
        if prices[i] < prices[i + 1]:
            profit_list.append(max(prices[i + 1:]) - prices[i])
    if profit_list == []:
        for i in range(len(prices) - 1):
            if prices[i] > prices[i + 1]:
                profit_list.append(min(prices[i + 1:]) - prices[i])
    return max(profit_list)
    # if the current price is larger find the difference between smallest price right of the current price with i and append to the profit list
    # once list is completed, return largest profit


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
