#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = 0
  for i in range(len(prices) - 1):
    for j in range(i + 1, len(prices)):
      if prices[j] > max_profit:
        max_profit = prices[j] - prices[i]
  return max_profit

def find_max_profit2(prices):
  min_price = prices[0]
  max_profit = 0.0

  for price in prices:
    min_price = min(min_price, price)
    compare_price = price - min_price

    max_profit = max(max_profit, compare_price)
  return max_profit
# def find_max_profit(prices):

#   lowest = prices[0]
#   highest = prices[0]

#   # highest = None
#   for value in prices[1:]:
#     if value < lowest:
#       lowest = value

#   for value in prices[1:]:
#     if value > highest:
#       highest = value

#   profit = highest - lowest
#   return profit
#   # return profit

# print(find_max_profit([5, 2, 1]))
# print(find_max_profit([1050, 270, 1540, 3800, 2]))
print(find_max_profit2([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


  '''
  function receives List of stock prices as input
  Buy first before selling
  target lowest stock
  target highest stock

  can assume we enite list of stock prices

  return bought minus sold
  '''

