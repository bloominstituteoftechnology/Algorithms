#!/usr/bin/python

import argparse

def find_max_profit(prices):
    """
    This function receives as input a list of stock prices 
    function should return the maximum profit that can be made from a single buy and sell
    find the difference between the smallest and largest prices in the list of prices.
   
    """  
    largest_profit = 0
    for index, initial_number in enumerate(prices):
        for secondary_number in prices[index + 1 : ]:
            profit = secondary_number - initial_number
            if largest_profit == 0 or profit > largest_profit:
                largest_profit = profit
    #Time complexity is O(n^2) as two loops involved.. 
    return largest_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))