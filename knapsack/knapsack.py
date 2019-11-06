#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  table = [[0.0 for _ in range(capacity + 1)]
    for _ in range(len(items) + 1)]
  
  for i, item in enumerate(items):
    for room in range(1, capacity + 1):
      previous_items_value = table[i][room]
      if room >= item.size:
        value_freeing_weight_for_item = table[i][room - item.size]
        # only take if more valuable than previous item
        table[i + 1][room] = max(value_freeing_weight_for_item + item.size,
          previous_items_value)
      else:   # no room for this item
        table[i + 1][room] = previous_items_value
  # figure out solution from table
  solution = []
  room = capacity
  for i in range(len(items), 0, -1):   # work backwards
    # was this item used?
    if table[i - 1][room] != table[i][room]:
      solution.append(items[i - 1])
      # if item was used, remove its weight
      room -= items[i - 1].size
  return solution  

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