#!/usr/bin/python

import argparse

prices = [1050, 270, 1540, 3800, 2]


def find_max_profit(prices):#This function's time completity is O(n^2). I believe memory complexity is O(1) as var biggestProfit doesn't grow. 
    biggestProfit = 0 #O(1)
    
    for i in range(len(prices)): #len is O(1) but a nested for loop like this means going through each iteration n times where n is the length of the list, so O(n^2) 
        if i == len(prices) - 1:
            return biggestProfit
        for j in range(len(prices)): 
            if i + j > len(prices) - 1:
                biggestProfit
            elif prices[i+j] - prices[i] > biggestProfit:
                biggestProfit = prices[i+j] - prices[i]
            elif biggestProfit == 0 and prices[i+j] - prices[i] < 0:
                biggestProfit = prices[i+j] - prices[i]
            else:
                biggestProfit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))