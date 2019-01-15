#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  """
  i guess we need to build up a map to show us how to come up with the answer
  we will start will a dictionary of places we have been and how many steps it takes to get there
  the steps will rely on one another for totals
  for instance
  0:1, 1:1, 2:2, = +1:(last three totals | in this example 1+1+2, next would be 1+2+4 and so on..)

  psuedo code
  create dictionary
  add k+1 : k-1.v + k-2.v + k-3.v until i reach the inputed number, also storing the values for future look up
  """
  past_values = {0:1, 1:1, 2:2}
  if n in past_values:
    return past_values[n]
  else:
    past_values[n] = climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)
    return past_values[n]
    
# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_stairs = int(sys.argv[1])
#     print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
#   else:
#     print('Usage: climbing_stairs.py [num_stairs]')
