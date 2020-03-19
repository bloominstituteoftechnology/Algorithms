#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(capacity, items):
 # "running capacities" from 0 up to and including the maximum weight W.
  bestvalues = [[0] * (items + 1)
          for i in range(len(capacity) + 1)]

  # Enumerate through the items and fill in the best-value table
  for i, (value, weight) in enumerate(capacity):
    # Increment i, because the first row (0) is the case where no items
    # are chosen, and is already initialized as 0, so we're skipping it
    i += 1
    for j in range(items + 1):
      # Handle the case where the weight of the current item is greater
      # than the "running capacity" - we can't add it to the knapsack
      if weight > j:
        bestvalues[i][items] = bestvalues[i - 1][items]
      else:
        # Otherwise, we must choose between two possible candidate values:
        # 1) the value of "running capacity" as it stands with the last item
        #    that was computed; if this is larger, then we skip the current item
        # 2) the value of the current item plus the value of a previously computed
        #    set of items, constrained by the amount of capacity that would be left
        #    in the knapsack (running capacity - item's weight)
        candidate1 = bestvalues[i - 1][j]
        candidate2 = bestvalues[i - 1][j - weight] + value

        # Just take the maximum of the two candidates; by doing this, we are
        # in effect "setting in stone" the best value so far for a particular
        # prefix of the items, and for a particular "prefix" of knapsack capacities
        bestvalues[i][j] = max(candidate1, candidate2)

    # Reconstruction
    # Iterate through the values table, and check
    # to see which of the two candidates were chosen. We can do this by simply
    # checking if the value is the same as the value of the previous row. If so, then
    # we say that the item was not included in the knapsack (this is how we arbitrarily
    # break ties) and simply move the pointer to the previous row. Otherwise, we add
    # the item to the reconstruction list and subtract the item's weight from the
    # remaining capacity of the knapsack. Once we reach row 0, we're done
  reconstruction = []
  i = len(capacity)
  z = items
  while i > 0:
    if bestvalues[i][z] != bestvalues[i - 1][z]:
      reconstruction.append(items[i - 1])
      z -= items[i - 1][1]
      i -= 1

  # Reverse the reconstruction list, so that it is presented
  # in the order that it was given
  reconstruction.reverse()

  # Return the best value, and the reconstruction list
  return bestvalues[len(capacity)][items], reconstruction


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')