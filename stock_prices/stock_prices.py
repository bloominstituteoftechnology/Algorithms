#!/usr/bin/python

import argparse

# def find_max_profit(prices):
#   low = prices[0]
#   high = prices[1]
  
#   for i in range(0, len(prices)-1):
#     if low > high:
#       pass
#     elif prices[i] <= low:
#       low = prices[i]
#     elif prices[i+1] >= high:
#       high = prices[i+1]

#   max_profit = high-low

#   return max_profit

#so long as the highest number doesn't come before the lowest number

def find_max_profit(prices):
  # dex_lo = 0
  # dex_hi = 0
  # low = prices[0]
  # high = prices[0]
  # max_profit = 0

  # for i in range(0, len(prices)-1):
  #   if prices[i] < low:
  #     low = prices[i]
  #     print(low)
  #   if prices[i] > high:
  #     high = prices[i]
    
  #   diff_max = high-low
  #   print(diff_max)

  # max_profit = prices[i] - low

  # buy = prices[i]
  # sell = prices[0]

  max_arr = []
  for i in range(len(prices)):
    for j in range(0, len(prices)-1):
      if i > j:
        max_arr.append(prices[i]-prices[j])

  
  print(max_arr)
  max_profit = max(max_arr)
  print(max_profit)

  # print(f'The high is ${high} and the low is ${low} max profit is ${max_profit}')
  return max_profit

find_max_profit([10, 7, 5, 8, 11, 9])
find_max_profit([100, 90, 80, 50, 20, 10])
find_max_profit([1050, 270, 1540, 3800, 2])

    # for each element that came b4 check to see if it's price
    # is lower

    #check newest price against previous low => calculate profit 
    #
    #


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


# for i in range(0, len(arr)):
#   # high = if i+1 > i 
#     for 
#       diff = high - arr[i]
#       if diff > max_profit: max_profit = diff