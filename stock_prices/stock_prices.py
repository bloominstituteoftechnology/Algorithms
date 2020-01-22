#!/usr/bin/python

import argparse

def find_max_profit(prices):
	# we need to substract all values with each other and return the greatest number of all substractions
	# a temporary variable that will hold all the subtractions made in the sequence
	max_profit = []
	# we need a loop to iterate over the list of prices
	for curr_index in range(0, len(prices) - 1):
		# another loop to compare indexes
		for next_index in range(curr_index + 1, len(prices)):
			# we check if the current index is greater than the current's next index
			if(prices[curr_index] < prices[next_index]):
				# if it is, we subtract the current's next index with the current index
				profit = prices[next_index] - prices[curr_index]
				# we append the profit to our max profit array
				max_profit.append(profit)
			# else, we subtract the current index with the current's next index
			elif(prices[curr_index] > prices[next_index]):
				profit = prices[next_index] - prices[curr_index]
				# we append the profit to our max profit array
				max_profit.append(profit)
	# once we are done with the loop, we return the max of the temporary index, holding the max profit.
	return max(max_profit)

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))