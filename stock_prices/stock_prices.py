#!/usr/bin/python

import argparse


# buying and selling
# first element in the array = buying price
# second element in the array = selling price
# use a for loop to through the array
# in the array, pick the second number and minus it from the first number,
# pick the next number and minus it from the second number, repeat

def find_max_profit(prices):
    buying_price = prices[0]
    selling_price = prices[1]
    maximum_profit = selling_price - buying_price
    for i in prices[1:]:
        profit = i - buying_price
        maximum_profit = max(profit, maximum_profit)
        buying_price = min(i, buying_price)
        print(profit)
    return maximum_profit


find_max_profit([1050, 270, 1540, 3800, 2])

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
