#!/usr/bin/python

import argparse

# bought at $10
# best one so far $4
# sell on day 2, -3, day 3: -5, day 4: -2, day 5: 1, day 6: -1
# bought at $7, -2, 1, 4, 2
# buy on day 3 at $5 sell on day 5, make $6
# set my maximum profit at the second price minus the first price
# start at the first price, and pretend I'm buying that one
# loop through all the prices that are after the current one (that I bought)
# Every time I loop I'm going to calculate the "sell" price minus the "buy" price
# If that profit is more than the max profit that I have, set the max profit to this new higher profit
# go on to the next price, "buy" that one
# repeat the steps where I'm looping through all the prices after the current one, and do the comparisons

def find_max_profit(prices):
  # initialize profit as index 1 (bought) - index 2 (sold)
  profit = prices[1]-prices[0]
  min_value = prices[0]
  print(profit)
  if len(prices) <= 1: 
    profit = 0
    print(profit)
  else: 
    profit = prices[1]-prices[0]
    print(profit)
    for i in range(1, len(prices)):
      if prices[i]-min_value > profit: 
        profit = prices[i]-min_value 
      if prices[i] < min_value: 
        min_value = prices[i] 
      
  return profit
  
  

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))