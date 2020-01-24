#!/usr/bin/env python3

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

class MyItem:
    # def __init__(self, index, size, value):
    #     self.index = index
    #     self.size = size
    #     self.value = value
    #     self.valueRatio = value/size

    def __init__(self, item):
        self.index = item.index
        self.size = item.size
        self.value = item.value
        self.valueRatio = item.value/item.size

    def ratio(self):
        return self.valueRatio

def knapsack_solver(items, capacity):
    items = [MyItem(x) for x in items if x is not None]

    items = sorted(items, key=MyItem.ratio, reverse=True)
    backpack = []
    totalValue = 0
    for item in items:
        if item.size < capacity:
            backpack.append(item.index)
            totalValue += item.value
            capacity -= item.size
    backpack.sort()
    return {"Value": totalValue, "Chosen": backpack}
    
    # print(items, capacity)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            # items.append(MyItem(int(data[0]), int(data[1]), int(data[2])))
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
