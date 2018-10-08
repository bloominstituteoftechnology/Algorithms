#!/usr/bin/python

import sys

#Built dict determining the base number of whole actions possible for each option of 3,2,1 respectively 
#Next step is to iterate over n - base number of whole actions and the subsequent permutations to get n to 0 
#if options[3] > 0, then n - (3 * permutation(options[3])) and then recurse this until n = 0 for each option[x] reduction 
#keep dict of permutations and check to see if it's been called already via memoizer

def climbing_stairs(options, n):
  options = dict((k, int(n/k)) for k, v in options.items())
  count = 0
  
  print('options before checker', options)

  if options[3] = 0 and options[2] = 0 and options[1] = 0:
    count += 1
    stepClimber(options, n = 3)

  if options[3] > 0:
    options = {3: options[3] - 1, 2: options[2], 1: options[1]}
    n = n - 3
    stepClimber(options, n)  
  elif options [2] > 0:
    options = {3: options[3], 2: options[2] - 1, 1: options[1]}  
    n = n - 2
    stepClimber(options, n)
  elif options [1] > 0: 
    options = {3: options[3], 2: options[2], 1: options[1] - 1}  
    n = n - 1
    stepClimber(options, n)
  else:
    return
  
  print(options)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')