#!/usr/bin/python

import argparse

#Iterative solution
#Time complexity: O(n^2)
def find_max_profit(prices):
  maxProfit = -50000000
  for i in range(len(prices)): #O(n)
    currentPrice = prices[i]
    for j in range(i+1, len(prices)): #O(n)
      nextPrice =  prices[j]
      profit = nextPrice - currentPrice
      if profit > maxProfit:
        maxProfit = profit
      j = j + 1
  i = i + 1
  return maxProfit


print(find_max_profit([10, 7, 5, 8, 11, 9]))
if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))


