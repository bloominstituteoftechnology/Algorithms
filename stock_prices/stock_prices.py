#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # make a variable to hold current max profit
  max_profit = -2 ** 100

  # set cursor at index  1
  # we want to sell after we bought 
  cur = 1

  for i in range(len(prices)):
    cur = i + 1

    while cur < len(prices):
      profit = prices[cur] - prices[i]

      if profit > max_profit:
        max_profit = profit
      
      cur += 1

  return max_profit



print("Finding max profit")
prices = [1050, 270, 1540, 3800, 2]
print(find_max_profit(prices))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))