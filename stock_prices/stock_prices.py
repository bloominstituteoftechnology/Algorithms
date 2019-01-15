#!/usr/bin/python
import argparse
import math

def find_max_profit(prices):
  '''
  function description:
    returns the maximum profit that can be made from a single buy and sell

  pseudo code: 
    - start with a loop
    - at the index compare the other values to the right of it, if the right value is greater it'll find the difference
      - add something to hold the profit value
    - the loop will continue and when it reaches another greater right value it'll return the profit and check if it's 
      greater than the previos profit value, which it'll then keep the greatest profit
    - it'll do this through the whole array until there is only one max profit
  '''
  # stores max_profit current value and will handle negative values
  max_profit = -math.inf
  # first for loop, price on the left
  for i in range(len(prices)):
    # second for loop, price on the right
    for j in range (i+1, len(prices)):
      # checking that the new values are greater than the current max_profit
      if (prices[j] - prices[i]) > max_profit:
        # if the new values are greater, it'll store that difference as the current max_profit and continue the loop until it ends
        # if the new values are lower, it'll skip those values and continue the loop until it ends
        max_profit = prices[j] - prices[i]
  return max_profit

  # # First Pass Instructor Solution O(n^2):
  # max_profit = -math.inf

  # while prices != []:
  #   bought = prices[0]

  #   for p in prices[1:]:
  #     profit = p - bought
  #     if profit > max_profit:
  #       max_profit = profit
      
  #   prices.pop(0)

  # return(max_profit)

  # # Second Pass Instructor Solution O(n):
  # min_buy_price = prices[0]
  # max_profit = prices[1] - min_buy_price

  # for p in prices:
  #   profit = p - min_buy_price

  #   # # These 2 lines can replace the 2 if statements below
  #   # max_profit = max(profit, max_profit)
  #   # min_buy_price = min(p, min_buy_price)

  #   if profit > max_profit:
  #     max_profit = profit

  #   if p < min_buy_price:
  #     min_buy_price = p
  
  # return max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))