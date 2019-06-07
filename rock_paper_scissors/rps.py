#!/usr/bin/python



import sys

def rock_paper_scissors(n):
    permutation_list = []
    temp_list = []
    selections = ['rock', 'paper', 'scissors']
    if n <= 0:
        return None  

    return permutation_list


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')