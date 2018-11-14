#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # NAIVE SOLUTION
  # profit = 0
  # # compare all pairs and return the max diff
  # for i in range(0, len(prices)):
  #   for j in range(i+1, len(prices)):
  #     if (prices[j] - prices[i]) > profit:
  #       profit = prices[j] - prices[i]

  # if profit == 0:
  #   # hard code to solve for negative profit (sloppy)
  #   return -10
  # else:
  #   return profit
 
  # RECURSIVE SOLUTION
  if len(prices) == 0:
    return 0
  elif len(prices) > 2:
    # set lowest known price to first entry
    low = prices[0]
    # find the next highest value
    high = max(prices[1:])
    # calc the difference between lowest known and highest known
    diff = high - low
    # recursively iterate over all sequential potential diffs to find the maximum profit
    # the [1:] iterator reduces our potential diffs until we're left with the highest profit
    return max(diff, find_max_profit(prices[1:]))
  else:
    # if only 2 values, return last minus first
    return prices[-1] - prices[0]

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))