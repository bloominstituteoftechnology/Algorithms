#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):  
    stair_count={0:1,1:1,2:2}    
    counter=3  
    while counter<=n:     
      stair_count[counter]=stair_count[counter-1]+stair_count[counter-2]+stair_count[counter-3]
      counter+=1
    return stair_count[n] 
    """This solution is O(n) time complexity and O(n) space complexity.   It keeps a compiled memory of the previous count and continues forward. it starts off at 3 
    
    so 3-3 = 0  stair_count[0] = 1 
    3-2 = 1  stair_count[1] = 1 
    3-1 = 2 stair_count[2] = 2
    2 + 1 + 1 = 4 so stair_count[3] = 4 
    (1,1,1) (1,2) (2,1) (3) 
    then counter += 1 
    on the next one  stair_count[4] = 
    stair_count[3] + stair_count[2] + stair_count[1] 
    which is equivalent  to   4(created from the first go arond)+ 2 + 1 
    so now  stair_count[4] = 7 
    (2,2)(4), stair_count[2] = (3,1), (1,3), stair_count[3](1,1,1,1) (1,2,1) (2,1,1) (1,1,2)

    (1,1,1,1) (1,2,1) (2,1,1) (4) (1,1,2) (1,3) (3,1), (2,2) **** confused  for some reason 4 produced 8. ***

    below is stair_count[5]  which should be 13 
    (1,1,1,1,1) (5) (3,2) (2,3) (4,1) (1,4) (1,1,2,1) (1,2,1,1) (2,1,1,1) (1,1,1,2) (1,3,1) (3,1,1) ( 1,1,3)

    I can visually see all other counts though just not when it equals 4. 

    But in general it will continue up using the previous values to calculate a new total. 
     """


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')