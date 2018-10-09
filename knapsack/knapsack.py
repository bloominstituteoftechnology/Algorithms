#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  sorted_items=sorted(items,key=lambda item: item.value/item.size,reverse=True)
  knapsack=[]
  for item in sorted_items:
    if capacity-item.size>=0:
      capacity-=item.size
      knapsack.append(item)
  knapsack_info={
    'Value':0,
    'Chosen':[]
  }
  for item in knapsack:
    knapsack_info['Value']+=item.value
    knapsack_info['Chosen'].append(item.index)
  knapsack_info['Chosen'].sort()
  return knapsack_info
  

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