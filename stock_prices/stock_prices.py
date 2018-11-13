#!/usr/bin/python

import argparse

# first attempt: create array of all possible buy/sell spreads, then find the largest
# def find_max_profit(prices):
#   possible_spreads = []
#   for i in prices:
#     # for idx, s in enumerate(prices, start = b ):
#     for j in prices[prices.index(i):]:
#       if j - i != 0:
#         possible_spreads.append(j - i)
#   print('******************')
#   print('possible spreads:', possible_spreads)
#   print('possible_spreads n:', len(possible_spreads))
#   print('max profit:', max(possible_spreads))
#   return max(possible_spreads)
#   # return(possible_spreads)

# 2nd attempt: same as first but with different loop syntax
# ----- Best solution so far -----
def find_max_profit(prices):
  possible_spreads = []
  for i in range(0, (len(prices) - 1)):
    for j in range((i +1), (len(prices) - 1)):
      possible_spreads.append(prices[j] - prices[i])
  print('******************')
  print('possible spreads:', possible_spreads)
  print('possible_spreads n:', len(possible_spreads))
  print('max profit:', max(possible_spreads))
  return max(possible_spreads)

find_max_profit([100, 90, 80, 50, 20, 10])
find_max_profit([10, 7, 5, 8, 11, 9])


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))