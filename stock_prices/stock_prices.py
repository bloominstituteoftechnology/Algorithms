#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # Instantiate vars
    current_min_so_far = 1000000000
    max_profit = -1000000000
    
    # Loop through prices
    for i in range(len(prices)):
        current_profit = prices[i] - current_min_so_far
        if current_profit > max_profit:
            max_profit = current_profit
        
        if prices[i] < current_min_so_far:
            current_min_so_far = prices[i]
    
    return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))