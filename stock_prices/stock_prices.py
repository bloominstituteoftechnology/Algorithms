#!/usr/bin/python

import argparse

def find_max_profit(prices):
  min_price = prices[0]
  max_profit = prices[1] - prices[0]
  for i in range(1, len(prices)):
    if prices[i] < min_price:
      min_price = prices[i]
    elif prices[i] - min_price > max_profit:
      max_profit = prices[i] - min_price
  return max_profit

  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

#beej solution
  #first swipe
  # if buy at first price, check the rest of the prices for potential max profit
  """def find_max_profit(prices):
    bought = prices[0]

    for p in prices[1:]:
      profit = p - bought
      print profit 
      #how then to keep track of max profit
      if profit > max_profit:
        max_profit = profit
        print(max_profit)"""
      #good but only tells you if you buy at first value, not at any random value
      #max(p - bought)

"""  def find_max_profit(prices):
    max_profit = 

    while prices != []:
      bought = prices[0]

      for p in prices[1:]:
        profit = p - bought
          if profit > max_profit:
            max_profit = profit
        
      prices.pop(0)
    
    print(max_profit)"""
    #works but not optimized

#optimized
"""def find_max_profit(prices):
  min_price = prices[0]
  max_profit = prices[1] - min_price

  for p in prices[1:]:
    profit = p - min_price

    max_profit = max(profit, max_profit)
    min_price = min(p, min_price)

  return max_profit"""