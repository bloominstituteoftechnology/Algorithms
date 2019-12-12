#!/usr/bin/python

import argparse
def find_max_profit(prices):
 #global variable to hold profits
 profits = []
 #iterate through the array's length - 1
 for i in range(0, len(prices) - 1):
 #second for loop starting at index 1 to compare index's values
 	for j in range(i + 1, len(prices)):
 #compare if i is less than j, if it is then substract j from i and push result to profits
 		if prices[i] < prices[j]:
 			result = prices[j] - prices[i]
 			profits.append(result)
 #else if i is greater than j, subtract j from i and push results to profits
 		elif prices[i] > prices[j]:
 			result = prices[j] - prices[i]
 			profits.append(result)
 #return the max of the profits variable
 return max(profits)

# find_max_profit([12, 5, 6, 11, 9, 3])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))