#!/usr/bin/python

#----NOTES----
# My solution is naive and fails @ complexity (on large)
# to improve this solution I would need to compare each highest value/size option
# against lesser efficient downstream combos that maximize the utility of remaining space.
# I did not have time to implement this solution

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def myFunc(e):
  return e.value

def knapsack_solver(items, capacity):
  newItems = []
  for item in items:
    newItems.append(Item(item.index, item.size, item.value/item.size))

  newItems.sort(key=myFunc, reverse=True)
  knapCap = 0
  answer = []
  value = 0
  cost = 0

  for item in newItems:
    #print(item.size)
    #print(item.value)
    #print(capacity-knapCap-item.size)
    #print('**')
    if(capacity-knapCap-item.size >= 0):
      #print('added')
      answer.append(item.index)
      knapCap+=item.size
      cost+=item.value
      value+=item.value*item.size
    answer.sort()
  return {'Value': int(value), 'Chosen': answer}

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