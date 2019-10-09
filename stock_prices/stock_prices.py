#!/usr/bin/python

# 1. Understand the question
# Given an array of prices this function should,
# return the largest increase between two indexes, moving left to right.

# 2. Plan
# if current value is greater than what is in the initial value, replace the initial value
# for each item in the array,
# if price is less than min_profit, replace min_profit with that price
# if price - min_profit is greater max_profit, replace the max_profit with the new value
# loop through all items to find largest difference between two items 
# when loop finishes return the variable

# 3. Implement Plan
# start by creating variable(s)
# set minimum as the first item of given array
# set maximum as the difference between the first two items of given array
# loop through list

# 4. Revise
# Recursion?

import argparse

def find_max_profit(prices):
  min_profit = prices[0]
  max_profit = prices[1] - prices[0]

  for i in range(1, len(prices)):
    if prices[i] < min_profit:
      min_profit = prices[i]
    elif prices[i] - min_profit > max_profit:
      max_profit = prices[i] - min_profit

  return max_profit

print(f'{find_max_profit([1050, 270, 1540, 3800, 2])}')

#   max_profit = 0
#   for i in range(0, len(prices) - 1):
#     value = prices[i]
#     print(f'{i} returns {value}')

#     for j in range(i + 1, len(prices)):
#       current_raise = prices[j] - prices[i]
      
#       if current_raise > max_profit:
#         max_profit = current_raise

#   return max_profit

# find_max_profit([1050, 270, 1540, 3800, 2])



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))