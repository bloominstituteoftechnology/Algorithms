#!/usr/bin/python
'''
Understanding: 
Input: num of input price follow by the number of price.
Ouput: max profit output price

Plan:
if prevPrice > curPrice && curPrice < nextPrice => buyPrice = curPrice
if prevPrice < curPrice && curPrice > nextPrice => sellPrice = curPrice

maxProfit = sell - buy


'''
import argparse

def find_max_profit(prices):
  buyPrice=0
  sellPrice =0
  max_profit = 0
  
  print(prices)
  for i in range(len(prices)-1):
    if  buyPrice == 0 and prices[i] < prices[i+1]:
      buyPrice = prices[i]
    elif buyPrice != 0 and prices[i] > prices[i+1]:
      if sellPrice < prices[i]:
        sellPrice =  prices[i]

  if buyPrice == 0:
    buyPrice =  prices[-1]
  max_profit = sellPrice - buyPrice

  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))