#!/usr/bin/python

import argparse
import math

# O(n^2)
# def find_max_profit(prices):
#     max = -1000
#     for i in range(len(prices) - 1):
#         for j in range(i, len(prices)):
#             subtract = prices[j] - prices[i]
#             if subtract > max and i != j:
#                 max = subtract
#     return max


# O(n)


def find_max_profit(prices):
    max = -math.inf
    highest = 0
    smallest = prices[0]
    highInd = 0
    smallInd = 0
    subtract = 0
    for i in range(len(prices)):
        if prices[i] > highest and i != 0:
            highest = prices[i]
            highInd = i
        if prices[i] < smallest and i != len(prices)-1:
            smallest = prices[i]
            smallInd = i
        if highInd < smallInd:
            subtract = smallest - highest
        elif highInd > smallInd:
            subtract = highest - smallest
        else:
            subtract = max

        if subtract > max:
            max = subtract
    return max


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}."
          .format(
              profit=find_max_profit(args.integers), prices=args.integers))
