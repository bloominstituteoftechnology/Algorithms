#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    print ("Items",items)
    print ("Capacity",capacity)
    x = [[0] * (capacity + 1)] * (len(items) + 1)
    x = [[0 for j in range(capacity + 1)] for i in range(len(items) + 1)]
    selected = [[[] for j in range(capacity + 1)] for i in range(len(items) + 1)]
    #x[i][j] -> ith row and jth column value

    i=1
    for item in items:
        item_index, weight, value = item[0],item[1], item[2]

        for j in range(1, capacity + 1):
            #Trying to fill x[index of weight][index of capaicity]
            if weight <= j:
                if value + x[i-1][j-weight] > x[i-1][j]:
                    x[i][j] = value + x[i-1][j-weight]
                    selected[i][j] = selected[i-1][j-weight] + [item_index]
                else:
                    x[i][j] = x[i-1][j]
                    selected[i][j] = selected[i - 1][j]

                # x[i][j] = max(value + x[i-1][capacity-weight], x[i-1][capacity])

            else:
                x[i][j] = x[i-1][j]
                selected[i][j] = selected[i - 1][j]

        i += 1

    print(x)
    return {"Chosen" : selected[i-1][capacity],"Value":x[i-1][capacity]}

# print(knapsack_solver({2:4,3:2, 5:8, 6 : 4}, 10))

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