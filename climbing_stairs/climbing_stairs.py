#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
    if (n == 1 or n == 0): 
        return 1
    elif (n == 2): 
        return 2
      
    else : 
        return climbing_stairs(n - 3) + climbing_stairs(n - 2) + climbing_stairs(n - 1) 

  
 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')

    print(climbing_stairs(5))

  #  ''' visualize steps
  #  0 steps:

     
  #    4 steps = 
  #     1,1,1,1,
  #     1,1,2
  #     2,1,1
  #     3,1
  #     1,3
  #     2,2

  #   '''
    

  # '''
  # 5 steps =

  # 3,2
  # 3,1,1
  # 2,3
  # 1,1,3
  # 2,2,1
  # 1,1,1,1,1
  # 1,1,1,2
  # 1,1,3
  # 1,1,2,1
  # 1,3,1
  # 1,2,1,1,
  # 1,2,2


  # '''
  

  
  
  

print(climbing_stairs(10))
