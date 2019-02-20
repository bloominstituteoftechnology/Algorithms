#!/usr/bin/python

import sys

def climbing_stairs(n, cache = None):
    """
    General Approach  : --
    -- check no. of steps
    -- As kid can jump 3 step hop or 2 step hop or 1 step hop
    -- To count the ways kid can climb
        -- Do successive substraction from no. of steps with hops.. 3, 2, 1 until no. of steps ZERO
        -- Count substraction levels

    Using Recursion  :--
    -- base case n < 0 return 0
                 n == 0 and n == 1 return 1
    -- call recursive for 3 hop, 2 hop, 1 hop and return addition of these all 
    
    """
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')