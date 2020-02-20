#!/usr/bin/python

import argparse

def find_max_profit(prices):
  lowest = prices[0]
  highest = prices[0]
  maximum = None
  for price in prices[1:]:
    diff = price - lowest 
    if maximum == None or diff > maximum:
      maximum = diff
    if price > highest:
      highest = price
    if price < lowest:
      lowest = price
  
  return maximum
    
    




if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))