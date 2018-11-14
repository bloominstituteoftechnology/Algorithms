#!/usr/bin/python

import sys

def climbing_stairs(n, cache={}):
  if n==0:
    return 1
  for x in range(1,n+1):
    total = 0
    print(f'Doing {x}')
    if x==1:
      cache['1'] = 1
      total += 1
    elif x==2:
      cache['2'] = 2
    elif x==3:
      cache['3'] = 4
    else:
      for left in range(1,4):
        if left > x:
          break
        total += cache[f'{x-left}']
      print(f"total: {total}")
      cache[f'{x}'] = total
    print(f"cache[{x}]:{cache[f'{x}']}")
  return cache[f'{n}']
        
    




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')