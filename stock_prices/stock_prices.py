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

	max_profit = -prices[0]

	if len(prices) == 1:
		return max_profit

	for x in range(0, len(prices)):
		temp_profit = -prices[x]
		for y in range(x + 1, len(prices)):
			if prices[y] - prices[x] > temp_profit:
				temp_profit = prices[y] - prices[x]
		if temp_profit > max_profit:
			max_profit = temp_profit

	return max_profit


if __name__ == '__main__':
	# This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))