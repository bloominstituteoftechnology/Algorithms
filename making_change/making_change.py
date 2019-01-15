#!/usr/bin/python

import sys
amount = 30
denominations =[1,5,10,25,50]

def making_change(amount, denominations):

  k= len(denominations)
  n= amount



  totalCombo = math.factorial(int(n))/math.factorial(int(k))*math.factorial(int(k))

  print(totalCombo)




making_change(amount, denominations)

'''
if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")'''