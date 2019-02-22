#!/usr/bin/python

import argparse

def find_max_profit(prices, largest = 0):
    local_largest = largest
    if len(prices) > 1:
        current = prices[0]
        rest = prices[1:]
        rest.sort()
        biggest_rest = rest[-1]
        current_result = biggest_rest - current

        if current_result > local_largest or local_largest == 0:
            local_largest = biggest_rest - current
        
        return find_max_profit(prices[1:], local_largest)

    else:
        return local_largest


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

##############
# solution 1 #
##############
# Iterave
# def find_max_profit(prices):
#     top_profit = 0

#     for index in range(0, len(prices) - 1):
#         x = prices[index]
#         print(f'{index}: {x}')

#         for jndex in range(index + 1, len(prices)):
#             current_increase = prices[jndex] - prices[index]
#             if current_increase > top_profit:
#                 top_profit = current_increase

#     return top_profit

# # find_max_profit([1050, 270, 1540, 3800, 2])
# print(f'SOLUTION 1 {find_max_profit([1050, 270, 1540, 3800, 2])}') # 3530

##############
# SOLUTION 2 #
##############
# Recursive

# def find_max_profit_2(prices, largest = 0):
#     local_largest = largest
#     if len(prices) > 1:
#         current = prices[0]
#         rest = prices[1:]
#         rest.sort()
#         biggest_rest = rest[-1]
#         current_result = biggest_rest - current

#         if current_result > local_largest:
#             local_largest = biggest_rest - current
        
#         return find_max_profit_2(prices[1:], local_largest)

#     else:
#         return local_largest

# print(f'SOLUTION 2 {find_max_profit_2([1050, 270, 1540, 3800, 2])}') # 3530

# NOTES
# 1 Understanding
  # given an array of prices in chronological order, this function
  # should return the largest increase possible between two indexes
  # moving from left to right

# 2 Sketch
  # what will this function do if passed the improper format method?
  # is that something we need to be concerned with?

# 3 come up with first plan
  # create a variable and set it to 0
  # for each item in the list subtract it from each
    # price to the right
  # if the current is greater than what is in the initial variable
    # over write the initial variable
  # when the loop finishes return the initial variable

# 4 Think of how to improve
    # after brute forcing it I needed to use 2 nested for loops
    # I believe we are looking at a complexity of O(n**2)

    # interested in looking for a recursive solution and testing
    # steps and time complexity of growing samples

# 5 Implement improved solution
    # Recursive solution implemented!!
    # Time to test each for the number of steps and time to solve
        # with various input lengths

# input             solution 1 steps            solution 2 steps
#[1,2]              15                          19
#[1,2,4]            26                          30
#[1,2,4,8,16]       57                          52
#[1,2,4,8,16,32,64,128,256,512,1024,2048] results below
#                   260                         129
#[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072]
#                   551                         195


# in general iterative in this case starts lower and ramps quicker
# recursive has higher overhead in the beginning but does not scale as rapidly
# Unfortunately I did not account for a negative profit being the highest
# need to look again

# altered line 14
# if current_result > local_largest:
# if current_result > local_largest or local_largest == 0:

# tests pass