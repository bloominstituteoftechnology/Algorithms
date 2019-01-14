#!/usr/bin/python

# COMMENTING INITIAL BOILERPLATE FOR NOW
# import argparse

# def find_max_profit(prices):
#   pass


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

##############
# solution 1 #
##############
def find_max_profit(prices):
    top_profit = 0

    for index in range(0, len(prices) - 1):
        x = prices[index]
        print(f'{index}: {x}')

        for jndex in range(index + 1, len(prices)):
            current_increase = prices[jndex] - prices[index]
            if current_increase > top_profit:
                top_profit = current_increase

    return top_profit

# find_max_profit([1050, 270, 1540, 3800, 2])
print(find_max_profit([1050, 270, 1540, 3800, 2])) # 3530


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

# 5 Implement improved solution