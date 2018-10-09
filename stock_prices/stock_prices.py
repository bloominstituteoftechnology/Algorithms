#!/usr/bin/python

import argparse

def find_max_profit(arr):
  if arr.index(max(arr)) > arr.index(min(arr)):
    return max(arr) - min(arr)
  else:
    if(arr[0] and arr[1]):
      min_value = arr[0]
      max_profit = arr[1] - arr[0]
      for price in range(1,len(arr)):
        if arr[price] < min_value:
          min_value = arr[price]
        elif arr[price] - min_value > max_profit:
          max_profit = arr[price] - min_value
      return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))