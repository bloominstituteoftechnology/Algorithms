#!/usr/bin/python

import argparse

# first find all possible profits
# - prices[1] - [prices 0], prices[2]- prices[0], prices[3] - prices[0], prices[4] - prices[0]
##  prices[2] - prices[1], prices[3] - prices[1], prices[4] - prices[1]


def find_max_profit(prices):
    i = 0
    recursionCount = 0
    maxProfit = float("-infinity")
    for price in range(len(prices) - 1):

        recursionCount += 1
        print("Recursion", recursionCount)
        if i > len(prices):
            continue

        for price in range(len(prices) - 1):
            i += 1
            if i > len(prices) - 1 or recursionCount > len(prices) - 1:
                continue
            print("Iteration", i)
            profit = (prices[i] - prices[recursionCount-1])
            print("Max", maxProfit)
            print("")
            print(
                f"{prices[i]}({i}) - {prices[recursionCount - 1]} ({recursionCount - 1}) is: ", profit)
            print("")
            if profit > maxProfit:
                maxProfit = profit

        print("Result", maxProfit)
        i = recursionCount
        print("recursionCount", recursionCount)
    print("return: ", maxProfit)
    return(maxProfit)


if __name__ == '__main__':
                # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
