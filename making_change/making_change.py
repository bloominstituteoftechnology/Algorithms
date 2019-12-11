#!/usr/bin/python

import sys



def making_change(amount, denominations):
	ways = 0
	for i in range(0,amount+1):
		for j in range(0,(amount//5) + 1):
			for k in range(0,(amount//10) + 1):
				for l in range(0,(amount//25) + 1):
					for m in range(0, (amount//50) + 1):
						if i + 5*j + 10*k + 25*l + 50*m == amount:
							# print(f'This is a solution ({i}, {j}, {k}, {l}, {m})')
							ways+=1
	return ways

  



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")