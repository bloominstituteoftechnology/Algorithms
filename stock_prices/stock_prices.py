#!/usr/bin/python

import argparse

# find_max_profit([1050, 270, 1540, 3800, 2])

# To achieve O(N), I need to be able to do all calculations by traversing the list
# once. Anything faster than O(N) is unlikely as to find maximum we need to have
# inspected each element at least once
def find_max_profit(prices):
	smallest = None
	second_largest = None
	largest = (prices[0], 0)

	for index in range(1, len(prices)):
		if largest[0] < prices[index]:
			largest = (prices[index], index)
		if index == 1:
			smallest = (prices[index - 1], index)
		elif smallest[0] > prices[index - 1]:
			smallest = (prices[index - 1], index)

	if not smallest or not largest:
		return None
	elif largest[1] > smallest[1]:
		return largest[0] - smallest[0]





'''
	for index in reversed(range(0, len(prices))):
			if not largest:
				largest = prices[index]
				smallest = prices[index - 1]
			
			if index > 1 and smallest > prices[index - 1]:
				smallest = prices[index - 1]

			if largest < prices[index]:
				largest = prices[index] 
				if index > 1:
					smallest =  prices[index - 1] 
				else:
					smallest = prices[index]


	if not (smallest or largest):
		return None
	else:
		return largest - smallest
'''



'''
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
'''

prices = [100, 90, 80, 50, 20, 10]
prices2 = [1050, 270, 1540, 3800, 2]
prices3 = [10, 7, 5, 8, 11, 9]

print(find_max_profit(prices))
