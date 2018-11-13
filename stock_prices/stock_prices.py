#!/usr/bin/python

import argparse

def find_max_profit(prices):    
  if len(prices) == 0: # --> Base case
    return 0
  
  profit = 0 # --> Best possible profit we can make with one buy/sell
  cheapest = prices[0] # --> Keep track of lowest value

  for i in range(1, len(prices)):
    cheapest = min(cheapest, prices[i]) # --> Here we update cheapest_stock value to be whatever is the smallest number between the current cheapest, and the current iterated price
    profit = max(profit, prices[i] - cheapest) # --> Update profit to be the highest between our old profit, and buying + selling at current price
  
  return profit

# print (find_max_profit([100, 90, 80, 50, 20, 10]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))