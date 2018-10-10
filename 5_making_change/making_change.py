#!/usr/bin/python

import sys

denominations = [1, 5, 10, 25, 50]

#practice with similar examples

# def return_change(to_return, coins = denominations):
#   flag = None
#   for c in coins:
#     if c == to_return:
#       return c
#     if c < to_return:
#       flag = c
#   temp_balance = round(to_return - flag, 2)
#   return [flag] + [return_change(temp_balance)]


# result = return_change(433)
# result

# def flatten(items):
#   for item in items:
#     try:
#       yield from flatten(item)
#     except TypeError:
#       yield item

# print(list(flatten(result)))


# def Coins(amt, cache):
#   arr = [50, 25, 10, 5, 1] #quarter, dime, nickel, penny
#   result = 0
#   if amt < 0:
#       return 0 #base case
#   if cache[amt] != 0:
#       return cache[amt]
#   if amt == 0:
#       return 1 #base case
#   for i in arr:
#       result += Coins(amt - i, cache)
#   cache[amt] = result
#   return result


def making_change(amount, denominations):
  count = 0
  if amount < 0:
    return 0
  if amount == 0:
    print("you cannot make change")
  if amount > 50:
    r1 = amount % 50
    count += r1
  return count

print(making_change(53,denominations))

# if amount/denomination < 1, then no making change
# if amount/denomination is an integer multiple of denomination, can make change with that denomination
# try amount/50, 25, 10, 5, 1
# try amount % 50, 25, 10, 5, 1



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")