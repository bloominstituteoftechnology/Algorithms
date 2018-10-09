#!/usr/bin/python

import argparse


def findSmallest(x, y):
    print(f"x, y: {x}, {y}")
    if(x <= y):
        return x
    else:
        return y


def findBiggest(x, y):
    print(f"biggest x, y: {x}, {y}")
    if(x >= y):
        return x
    else:
        return y


def find_max_profit(prices):
    leastList = prices[0:-1]
    leastPrice = min(leastList)
    maxPrice = max(prices)
    print(maxPrice - leastPrice)
    return maxPrice - leastPrice


# find_max_profit([1050, 270, 1540, 3800, 2])


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
