#!/usr/bin/python
''' DYNAMIC SOLUTION IN PROGRESS --------

table = [[0 for x in range(m)] for x in range(amount+1)]

for i in range(m):
  table[0][i] = 1

'''


import sys

amount = 100
denominations =[1,5,10,25,50]
m = len(denominations)

def making_change(denominations, m, amount):
  if (amount == 0):
    return 1

  if (amount < 0):
    return 0
  
  if (m <=0 and amount >= 1):
    return 0
  
  return making_change(denominations, m - 1, amount ) + making_change(denominations, m, amount- denominations[m-1] ); 

print(making_change(denominations, m, amount))

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")