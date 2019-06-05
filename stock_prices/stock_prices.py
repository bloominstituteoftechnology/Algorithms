#!/usr/bin/python
'''
Understanding: 
Input: num of input price follow by the number of price.
Ouput: max profit output price

Plan:
if curPrice < nextPrice, then uptrend maxprofit = nextPrice - minPrice
if curPrice > nextPrice, then downtrend minPrice = curPrice


max profit = nextPrice - minPrice


'''
import argparse

def find_max_profit(prices):
  minPrice=0
  max_profit = 0
  
  print(prices)
  for i in range(len(prices)-1):
    if prices[i] < prices[i+1] :
      max_profit = prices[i+1] - minPrice
    else:
      minPrice =  prices[i+1]
  
  if max_profit == 0:
    max_profit = - minPrice
  
  return max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))