#!/usr/bin/python

import sys

def reconstruct_trip(tickets):
  hash = dict()
  route = [0] * (len(tickets) - 1)

  for ticket in tickets:
    if ticket[0] == None:
      route[0] = ticket[1]
    hash[ticket[0]] = ticket[1]

  for i in range(1, len(tickets) - 1):
    route[i] = hash[route[i-1]]

  return route


if __name__ == "__main__":
  shorter = [
    (None, 'PDX'),
    ('PDX', 'DCA'),
    ('DCA', None)
  ]

  longer = [
    ('PIT', 'ORD'),
    ('XNA', 'CID'),
    ('SFO', 'BHM'),
    ('FLG', 'XNA'),
    (None, 'LAX'),
    ('LAX', 'SFO'),
    ('CID', 'SLC'),
    ('ORD', None),
    ('SLC', 'PIT'),
    ('BHM', 'FLG')
  ]

  print(reconstruct_trip(shorter))
  print(reconstruct_trip(longer))