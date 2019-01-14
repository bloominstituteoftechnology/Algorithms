#!/usr/bin/python

import argparse

def is_max_profit_negative(prices):
	for i in range(0, len(prices) - 1):
		if prices[i] < prices[i + 1]:
			return False
	return True

def find_max_profit(prices):
  if len(prices) == 0:
    return 0

  if is_max_profit_negative(prices) == True:
	  return -prices[-1]

  profit = 0
  cheapest = prices[0]

  for i in range(1, len(prices)):
    cheapest = min(cheapest, prices[i])
    profit = max(profit,prices[i] - cheapest)

  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))