#!/usr/bin/python

import argparse


def find_max_profit(prices):
    lowestPrice = prices[0]
    highestPrice = 0
    profit = 0
    maxProfit = 0
    for price in prices:
        if price < lowestPrice:
            lowestPrice = price
        elif price > highestPrice:
            highestPrice = price
        profit = highestPrice - lowestPrice
        if profit > maxProfit:
            maxProfit = profit

    # print(f'highest price: {highestPrice}')
    # print(f'lowest price:  {lowestPrice}')
    # print(f'max profit: {maxProfit}')

    return maxProfit


find_max_profit([10, 7, 5, 8, 11, 9])
if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
