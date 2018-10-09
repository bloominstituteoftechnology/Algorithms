#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    knapsack = []
    knapsack_size = 0
    knapsack_value = 0
    chart = [
        (item.index, item.size, item.value, item.value/item.size)
        for item in items]
    chart = sorted(chart, key=lambda x: x[-1], reverse=True)
    for k in chart:
        if knapsack_size + k[1] < capacity:
            knapsack.append(k[0])
            knapsack_size += k[1]
            knapsack_value += k[2]
    return {
        'Value': knapsack_value,
        'Chosen': sorted(knapsack)}


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
