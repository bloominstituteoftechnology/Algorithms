#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  return greedy(items,capacity)
  
  
def greedy(items,capacity):
  itemsSelected =[]
  totalValue = 0
  capcityIntial = capacity
  sortedItemsValue = sorted(items, key=lambda k: k['value'],reverse=True)

  for item in sortedItemsValue:
    if capacity-item["weight"] < 0:
      continue
    itemsSelected.append(item['name'])
    capacity -= item["weight"]
    totalValue += item["value"]
  return {'Value':totalValue,"Size":capcityIntial-capacity,"Chosen":itemsSelected}


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