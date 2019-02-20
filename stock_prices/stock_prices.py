#!/usr/bin/python

# buy sell amazon stock
# receives input list of stock prices
# function returns max profit from a single buy and sell
# must buy first before selling

# have two loops, initialize min and max to 0, profit to 0
# set min val = i
# set max val = j
# if max val - min val is greater than max, reassign new profit max

import argparse


def find_max_profit(prices):
    maxVal = 0
    minVal = 0
    profit = 0
    for i in range(0, len(prices)-1):
        minVal = prices[i]
        print(f" index of min: {i}. value of min:{minVal}")
        for j in range(i+1, len(prices)):
            maxVal = prices[j]
            print(f"index of max: {j}. value of maxVal {maxVal}")
            if profit < maxVal-minVal:
                profit = maxVal-minVal
                print(f"profit is: {profit}")
    return profit


arr1 = [1050, 270, 1540, 3800, 2]
max_profit = find_max_profit(arr1)
print(max_profit)

if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
