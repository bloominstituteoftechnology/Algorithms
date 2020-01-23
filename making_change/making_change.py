#!/usr/bin/python

import sys

def make_change(amount, denominations, cache):
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    elif len(denominations) == 1:
        return 1

    else:
        try:
            if cache[f'{amount}-{denominations}'] > 0:
                return cache[f'{amount}-{denominations}']
        except KeyError:
            pass
        perms = 0
        while denominations[-1] > amount:
            print(denominations[-1])
            denominations.pop()
        for i in range(amount//denominations[-1] + 1):
            perms += make_change(amount - (i * denominations[-1]), denominations[:-1], cache)
        cache[f'{amount}-{denominations}'] = perms
        return perms


def making_change(amount, denominations):
  if amount is 0 or amount is 1:
    return 1
  else:
    print(f'print amount {amount}')
    return make_change(amount, list(denominations), {})
    # return make_change(amount, list(denominations), [0 for i in range(amount + 1)])


solution = making_change(10, [1, 5, 10, 25, 50])
print('solution')
print(solution)



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")