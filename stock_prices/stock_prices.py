#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profit = -1
# iterate thriough each number in the list
  for i in range(0, len(prices)-1):
    #define sell_price
    sell_price = prices[i +1]

    #define buy_price
    buy_price = prices[i]

    #if sell price is less than buy price we cannot make a profit so continue
    if sell_price < buy_price:
      continue

    #if sell price is greater than the buying price check if these will gives us the best profit
    else:
      temp_profit = sell_price - buy_price
      if temp_profit > profit:
        profit = temp_profit

    return profit

find_max_profit([1050, 270, 1540, 3800, 2])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))