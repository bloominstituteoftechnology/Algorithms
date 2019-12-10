#!/usr/bin/python

import argparse
import math

def find_max_profit(prices):
	# negative means profit

	# max profit variable
	maxProfit = math.inf
	# nested loop
	# reverse the sign of number at the end

	for i in range(0, len(prices) - 1):
		
		for j in range(i+1, len(prices)):
			# got things backwards lol
			# print(prices[i], prices[j])
			if (prices[i] - prices[j]) < maxProfit:
				maxProfit = prices[i] - prices[j]

	return -maxProfit				

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))