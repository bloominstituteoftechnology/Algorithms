#!/usr/bin/python

import argparse


def find_max_profit(prices):
  max_profit = [0]

  for i in range(0, len(prices) - 1):
    cur_index = i

    for x in range(cur_index + 1, len(prices) - 1):

      if prices[x] - prices[cur_index] > max_profit[0]:
        max_profit[0] = prices[x] - prices[cur_index]



      elif prices[x] - prices[cur_index] < 0 and max_profit[0] == 0:
        max_profit[0] = prices[x] - prices[cur_index]

  return max_profit[0]
print('maxprofit')
print(find_max_profit([2,5,7,8,2,7,1,8,0,10]))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

    # Lambda Problem Solving Framework

    # UPER

    # U - UNDERSTAND
    # P - PLAN
    # E - EXECUTE
    # R - REFLECT

    # UNDERSTAND
    #   PROBLEM ---
    #   GET LIST OF NUMBERS EX: 4, 34, 6, 5, 574, 4
    #   the max profit is computed by subtracting some price by another
    #   price that comes before it; it can't come after it in the list of prices.

    #   GOAL
    #     GOING THRU LIST LEFT TO RIGHT, BUY AT LOW NUMBER, SELL AT HIGH NUMBER
    #     find the maximum difference between the smallest and largest prices
    #
    #
    #
    #
    #   EXPECTED RESULTS:
    #
    #     INPUT - [4, 5, 100, 10]
    #     OUTPUT - 95
    #
    #     INPUT - [90, 5, 1, 100]
    #     OUTPUT - 99

    #     INPUT - [3, 10, 5, 10]
    #     OUTPUT - 7

    # sudo
    # if first item in array = a  is smaller then 2nd = b,
    # then return b - a
    # else repeat on b and c
    # then c and d
    # until end of array

    #   REFLECT
    #     IS THIS EFFICIENT
    #

    # if first item in array = a  is smaller then 2nd = b,
    # end = len(prices)
    # for i in range(0, end):
    #   for j in range(0, end - 1):
    #     if prices[i] < prices[j]:
    #       # then return b - a
    #       arr = []
    #       j.append(arr)
    #       x = max(arr)
    #     return x
    #
    #   else:
    #     print("don't buy")

    # else repeat on b and c
    # then c and d
    # until end of array
    # return largest number
