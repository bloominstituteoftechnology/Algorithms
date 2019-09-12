#!/usr/bin/python

import argparse


def find_max_profit(prices):
	# create list to hold values
	profit_list = []
	for i in range(len(prices)):
		j = i + 1
		while j < len(prices):
			difference = prices[j] - prices[i]
			profit_list.append(difference)
			j += 1
	return max(profit_list)


if __name__ == '__main__':
	# This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(
		profit=find_max_profit(args.integers), prices=args.integers))
