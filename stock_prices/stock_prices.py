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

  #Subtract previous price from next price
  #Price at index 0
  prev_price = prices[0]
  print("Previous", prev_price)

  #Price at index 1
  next_price = prices[1]
  print("Next", next_price)

  #Intializing the profit after subtracting prev_price & next_price 
  profit = 0
  # print("profit", profit)

  #Intializing the largest profit margin to be returned
  max_profit = 0
  # print("Max Profit", max_profit)

  n = len(prices)
  
  if n <= 2: #--> If the length of prices is smaller than or equal to 2
    return next_price - prev_price # --> Subtract next and previous prices = max_profit

  max_profit = next_price - prev_price

  # print(f"Max profit is {max_profit}")

  # Iterate through the list --> I know that our target should be 3800 - 270  = 3530 = max_profit
  for i in range(1, n - 1):
    profit = prices[i] - next_price
    # print("Profit in loop", profit )
    # print("Subtraction", profit - next_price)
    
    # If the total profit is bigger than our current max_profit 0, the replace with the larger profit number
    if profit > max_profit:
      max_profit = profit
      # print("Our Max Profit:", max_profit)

  return max_profit
      

    

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

find_max_profit([1050, 270, 1540, 3800, 2])


"""
# The total amount of profit after comparing the two numbers
    profit = []

    # max profit should be min_prices - max_prices --> final solution
    max_profit = 0
    
    #find the max number and isolate it. 
    max_price = sorted(prices)[-1]
    print("Max number is: ",max_price)

    index = int(prices.index(max_price))
    print("index", int(prices.index(max_price)))
    
    # #Find minimum price left of max
    min_price = min(prices)
    print("min number is: ", min_price)

    # previous price --> prev_price
    prev_price = [0]

    # next price --> next_price
    next_price = [1]
    
    # Loop through the prices
    # for i in prices:
    #   if i < max_price:
    #       profit = [max_price - i]
    #       max_profit = sorted(profit)
    #       # return max(max_profit)
    #   # print("max profit", max_profit, "profit", profit)

    # print("Out of loop",max( max_profit))
"""