#!/usr/bin/python

import argparse

def find_max_profit(prices):
  low = prices[0]
  i = 0
  while i < len(prices):
    if prices[i] < low:
      low = prices[i]
    i += 1
  if low == prices[-1]:
    k = 0
    secondLow = prices[0]
    while k < len(prices) - 1:
      if prices[k] < secondLow:
        secondLow = prices[k]
      k += 1
    j = prices.index(secondLow)
    high = prices[prices.index(secondLow) + 1]
    while j < len(prices):
      if prices[j] > high:
        high = prices[j] 
      j += 1
    if high == secondLow:
      return -(high - low)
    else:
      return high - secondLow
  else:
    j = prices.index(low)
    high = prices[prices.index(low) + 1]
    while j < len(prices):
      if prices[j] > high:
        high = prices[j] 
      j += 1
    return high - low


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))