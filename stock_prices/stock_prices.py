#!/usr/bin/python

import argparse

def find_max_profit(prices):
  buy_price = float("inf")
  sell_price = 0

  if len(prices) == 1: # When there is only one price in prices return 0
    return 0

  for i, current_price in enumerate(prices):
    if i == len(prices) - 1:
      break

    next_price = prices[i + 1]

    if current_price < buy_price: # We want to find the lowest buy price, so if the current price is lower we set it as the new buy price.
      buy_price = current_price
      sell_price = next_price # When we found a new low-buy price we reset to the next price
      print(f"Curr_price: {current_price}, buy_price: {buy_price}")
      print(f"Next_price: {next_price}, sell_price: {sell_price} \n")
      continue

    if next_price > sell_price:
      sell_price = next_price
      print(f"New next_price: {next_price}, sell_price: {sell_price} \n")

  print(f"Profit: {sell_price - buy_price}  ---------- \n")
  return sell_price - buy_price

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))