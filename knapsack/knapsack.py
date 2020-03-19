#!/usr/bin/python

import sys
from collections import namedtuple
from operator import itemgetter

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    ratios = []
    for item in items:
        ratio = item[2] / item[1]
        ratios.append((item,ratio))
    ratios.sort(key = itemgetter(1), reverse = True)

    knapsack = []
    has_space = True
    while has_space:
        # repeat until there are no items left
        # or there isn't space left for the lightest item
        best_value = next((item for item in ratios if item[0][1] <= capacity), None)
        if best_value is None:
            has_space = False
        else:
            item = best_value[0]
            ratio = best_value[1]
            knapsack.append(item)
            capacity -= item[1]
            ratios.remove(best_value)

    knapsack.sort(key = itemgetter(0))

    result = {}
    result['Value'] = sum([item[2] for item in knapsack])
    result['Chosen'] = [item[0] for item in knapsack]

    return result


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
