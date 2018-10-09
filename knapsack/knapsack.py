#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  if Item == 0 or index == 0 :
    return 0

  if (size[index-1] > Item ):
    return knapsack_solver('Item', ['index', 'size', 'value'])

  else:
    return max(value[index-1] + knapsack_solver(Item-size[index-1], size, value, index-1),
      knapsack_solver('Item', ['index', 'size', 'value']))
  

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