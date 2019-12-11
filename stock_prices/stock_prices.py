#!/usr/bin/python

import argparse

def find_max_profit(prices):
	maxi = prices[1] - prices[0]
	for i in range(1,len(prices)):
		j = 0
		while j < i:
			if prices[i] - prices[j] > maxi:
				maxi = prices[i] - prices[j]
			j +=1
	return maxi


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

