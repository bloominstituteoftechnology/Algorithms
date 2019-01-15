#!/usr/bin/python

import argparse
import sys

def find_max_profit(prices):
  max_profit = float("-inf") # -∞, smallest number possible
  
  # Loop from beginning to end-1
  # Want to compare every element to the next one (can't compare the last element)
  for (index, buy_price) in enumerate(prices[:len(prices)-1]):
    
    for sell_price in prices[index+1:]:
      profit = float(sell_price - buy_price)
      
      if profit > max_profit:
          max_profit = profit
          
  return max_profit

#print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))