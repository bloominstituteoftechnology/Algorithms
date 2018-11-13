#!/usr/bin/python

import argparse

# research : http://book.pythontips.com/en/latest/enumerate.html
# had to use enumerate to fix an initial error
def find_max_profit(prices):
  largest_profit = 0
  # for index, initial_number in prices: (fixed)
  # 2 for loops nested : not very performant but just hashing out the idea of solving the problem 
  for index, initial_number in enumerate(prices):
    for secondary_number in prices[ index + 1: ]:
      # set the current profit variable to the secondary - initial
      profit = secondary_number - initial_number
      # test for profit being greater than largest profit
      if largest_profit == 0 or profit > largest_profit:
        # set the largest profit to the profit of this itteration
        largest_profit = profit
  # return the largest computed profit
  return largest_profit
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))