#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #pass
  # MAX == find max price after a lower price
  max = 0
  sell_index = 0
  for i in range(1, len(prices)):
      if prices[i] > max:
          max = prices[i]
          sell_index = i
  # MIN == find min price that pre seeds the  MAX
  min = max
  for i in range(0, sell_index):
      if prices[i] < max and prices[i] < min:
          min = prices[i]
  # day losses min, not the "rpofit min from above"
  if max == min:
      max = prices[sell_index + 1]
      for i in range(sell_index, len(prices)):
          if prices[i] > max and prices[i] < min:
              min = prices[i]
  # PROFFIT ==  MAX - MIN

  print(f"MAX: {max}, at index {sell_index}")
  print(f"MIN: {min}")
  return max - min
  # O is O(n)? x2 or x3?


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
