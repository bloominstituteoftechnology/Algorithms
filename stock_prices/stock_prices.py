#!/usr/bin/python

import argparse

def find_max_profit(prices):

  # input - array of whole numbers, no empty arrays

  # [10, 7, 5, 8, 11, 9] = max profit should be 6 (11 - 5)

  # find max profit by looping through stock price array (prices)
  # subtract each element in the array by each element in front of it and track the largest difference

  # REVERSE ARRAY COMPARISON
  # [10, 7, 5, 8, 11, 9]
  # 11: 11-8, 11-5, 11-7, 11-10

  # [9, 11, 8, 5, 7, 10]
  # 11: 11-8, 11-5, 11-7, 11-10

  # [100, 90, 80, 50, 20, 10]
  # 50: 50-80, 50-90, 50-100
  # 
  #  [100, 90, 80, 50, 20, 10]
  # [10, 20, 50, 80, 90, 100]
 

  r_prices = prices[::-1] # reverse the array to make finding all the possible differences easier
  max_profit = -99999999999 # initialize at insanely low number, since it's possible for a max profit to be a negative, we can't use zero
  for i,buy_price in enumerate(r_prices):     
    # loop through all the elements to the right of where we are in the main loop
    # if the difference between them is larger than the current largest difference, save it
    for j,sell_price in enumerate(r_prices[i+1:]): # make sure it doesn't subtract against itself
      # get and compare the difference between current numbers in loop to max_profit
      diff = buy_price - sell_price
      if diff > max_profit:
        max_profit = diff
  return max_profit
# print(find_max_profit([10, 7, 5, 8, 11, 9]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))