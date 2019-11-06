#!/usr/bin/python

import sys

cache = {}
# def making_change(amount, denominations):
    # pass
            





def making_change_one(amount, denominations):
    if amount in cache:
        return cache[amount]
    if (amount == 0):
        return 1
    elif (amount < 0 or denominations == []):
        return 0
    else:
        val = making_change_one(amount - denominations[-1], denominations) + making_change_one(amount, denominations[:-1]) 
        # val = making_change_one(amount, denominations[:-1]) + making_change_one(amount - denominations[-1], denominations) 
        # cache[amount] = val
        print(val)
        return val

denominations = [1,5,10,25,50]
# print(making_change_one(1, denominations))
# print(making_change_one(5, denominations))
print(making_change_one(100, denominations))
# print(making_change_one(15, denominations))
# print(making_change_one(20, denominations))
#
# denominations = [1,5,10, 25 ]
# print(making_change_one(1, denominations))
# print(making_change_one(5, denominations))
# print(making_change_one(10, denominations))
# print(making_change_one(15, denominations))
# print(making_change_one(20, denominations))
# print(making_change_one(25, denominations))
# print(making_change_one(30, denominations))
# print(making_change_one(35, denominations))

# if __name__ == "__main__":
#   # Test our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
#     denominations = [1, 5, 10, 25, 50]
#     amount = int(sys.argv[1])
#     print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
#   else:
#     print("Usage: making_change.py [amount]")
