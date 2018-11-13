#!/usr/bin/python

import argparse

# find_max_profit([1050, 270, 1540, 3800, 2])

# To achieve O(N), I need to be able to do all calculations by traversing the list
# once. Anything faster than O(N) is unlikely as to find maximum we need to have
# inspected each element at least once
def find_max_profit(prices):
	
	last_index = len(prices) - 1
	
	largest = (prices[last_index], last_index)
	smallest = (prices[last_index - 1], last_index - 1)
	second_largest = (prices[last_index], last_index)
	
	non_increasing = False

	for index in reversed(range(0, len(prices))):
		if largest[0] <= prices[index]:
			largest = (prices[index], index)
			if index > 0:
				# Set's smallest number to number to th
				smallest = (prices[index - 1], index - 1)
				print(smallest)
		# set's second largest in case of non increasing list
		if index < last_index and second_largest[0] < prices[index + 1] and prices[index + 1] < largest[0]:
				second_largest = (prices[index + 1], index + 1)

# Set's the smallest number if there is a smaller number at index
		if index > 1 and smallest[0] > prices[index - 1]:
			smallest = (prices[index - 1], index-1)
			print(smallest)

	if largest[1] == 0:
		return second_largest[0] - largest[0]
	else:
		return largest[0] - smallest[0]

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))



prices = [100, 100, 90, 80, 50, 20, 10]
prices2 = [1050, 270, 1540, 3800, 2]
prices3 = [10, 7, 5, 8, 11, 9]

print(find_max_profit(prices))
print(find_max_profit(prices2))
print(find_max_profit(prices3))
