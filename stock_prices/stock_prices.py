#!/usr/bin/python


import math
import argparse
myList = [100, 90, 80, 50, 20, 10]
def find_max_profit(prices):
  # max_profit = 0
  # for i, buy_price in (prices):
  #   for j, sell_price in (prices):
  #     if i == 0 and j == 1:
  #       max_profit = sell_price - buy_price
  #     elif j > i and sell_price - buy_price > max_profit:
  #       max_profit = sell_price - buy_price
  # return max_profit


  n = len(prices)
  # math.inf * -1
  max_profit = -10000
  if n <= 1:
    return max_profit
  
  min_stock_price = prices[0]
# loop through list
  for i in range(1, n):
    current_profit = prices[i] - min_stock_price

    if current_profit > max_profit:
      max_profit = current_profit
    if prices[i] < min_stock_price:
      min_stock_price = prices[i]
  return max_profit

print(find_max_profit(myList))



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))