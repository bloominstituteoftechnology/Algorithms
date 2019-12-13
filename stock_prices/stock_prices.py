#!/usr/bin/python

"""
input --> list of stock prices
output -->  max-profit = single buy - single sell (but first buying before selling)

For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

We get this by subtracting 3800 - 270  = 3530

270 comes before 3800


HINTS:
maximum difference between smallest and largest prices

we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices. 

max_profit = next_price - previous_price

Because you bought at 3800 and sold at 2



loop through the array, store to a variable, compare, and reassign something

 3800 - 270  = 3530
[  1050  |  270  |  1540 |  3800 |   2   ]
|   i0   |   i1  |   i2  |   i4  |   i5  |

"""

import argparse


def find_max_profit(prices):

  
  #current_min_price will always hold at [0]
  current_min_price = prices[0]
 
  # Maximum Profit = Subtract price at [1] from the current_min_price which will always be at [0]
  max_profit = prices[1] - current_min_price

  n = len(prices)

  # Starting at 1, iterate through the length of the array
  for i in range(1, n):
    # if prices[i] is smaller than current_min_price
    if prices[i] < current_min_price:
      # Make current_min_price equal prices[i] --> this allows us to keep the lowest price to the left of the biggest price
      current_min_price = prices[i]
      print("Finding Lowest Price",current_min_price)

    # If prices[i] minus current_min_price is biggest than max_profit
    elif prices[i] - current_min_price > max_profit:
      # Change it to the bigger max_profit
      max_profit = prices[i] - current_min_price
      print("Finding max profit", max_profit)

  return max_profit
      

    

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

find_max_profit([10, 7, 5, 8, 11, 9])

