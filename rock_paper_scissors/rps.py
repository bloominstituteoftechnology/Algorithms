#!/usr/bin/python

import sys
from itertools import product


# def rock_paper_scissors(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [['rock'],['paper'], ['scissors']]
#     else:
#         val = rock_paper_scissors(n-1) * (3)    
#         return(val)

def rock_paper_scissors(n):
    rpc = ['rock', 'paper', 'scissors']
    if n == 1:
        return [['rock'], ['paper'], ['scissors']]
    else:
        # itertools -> functions creating iterators for efficient looping
        # ** itertools standardizes a core set of fast, memory efficient tools that
        # are useful by themselves or in combination **
        # product('ABCD', 2) ... AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
        return [list(x) for x in list(product(rpc, repeat=n))]



# print(rock_paper_scissors(3))
# print(len(rock_paper_scissors(2)))
# print(len(rock_paper_scissors(4)))


# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')
