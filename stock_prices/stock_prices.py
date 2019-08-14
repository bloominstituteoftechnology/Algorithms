#!/usr/bin/python

# Write a function `find_max_profit` that receives as input a list of stock prices.
# Your function should return the maximum profit that can be made from a single buy and sell.
# You must buy first before selling; no shorting is allowed here.

# For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530,
# which is the maximum profit that can be made from a single buy and then sell of these stock prices.


# Use two loops.
# In the outer loop, pick elements one by one
# In the inner loop, calculate the difference of the picked element with every other element in the array
# compare the difference with the maximum difference calculated so far.


import argparse


def find_max_profit(prices):
    profit = prices[1] - prices[0]

    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
    return profit


print(find_max_profit([44, 30, 24, 32, 35, 30, 40, 38, 15]))
print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))