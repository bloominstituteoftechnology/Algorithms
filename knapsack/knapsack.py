#!/usr/bin/python

# ported from https://github.com/invegat/Knapsack I coded in Web4 
import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'weight', 'value'])
ro = namedtuple('ro', ['objects', 'value'])


def run_ring(o, W, above):  # W is both the total weight and the length of each row

    if above == None:
        above = []

        for j in range(o.weight):
            above.append(ro([], 0))
        for j in range(o.weight, W+1):
            above.append(ro([o], o.value))
        assert len(above) == W+1, 'first above is wrong length'
        return above

    row = []
    for j in range(o.weight):
        row.append(above[j])
    for j in range(o.weight, W+1):
        remaining = j - o.weight
        row.append(
            above[j] if above[remaining].value + o.value <= above[j].value else
            ro([*above[remaining].objects, o], above[remaining].value + o.value)
        )
    assert len(row) == W+1, 'row is wrong length'
    return row


def knapsack_solver(items, capacity):
    above = None
    for item in items:
        if item.weight > capacity:
          continue
        above = run_ring(item, capacity, above)
    if above is None:
      return 0
    r = above[-1]
    total_value = 0
    total_weight = 0
    chosen = []
    for i in range(len(r.objects)):
        total_value += r.objects[i].value
        chosen.append(r.objects[i].index)
        total_weight += r.objects[i].weight
    print('total weight:', total_weight)
    return {'Value': total_value, 'Chosen': chosen}


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
