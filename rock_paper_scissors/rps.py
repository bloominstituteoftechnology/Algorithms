#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    rps = ['rock', 'paper', 'scissors']

    # We need 3^(n-1) arrays starting with each hand
    # 3^(n-2) arrays starting with hadn1, hand2
    # 3^(n-3) arrays starting with hand1, hand2, hand3
    # etc.

    def add_hands(n, arr):
        if n == 0:
            return arr

        # for the first iteration we should have an array of length 3^(n-1)
        # for the first 3^(n-2) arrays of each hand, we need to add each hand
        for i in range(0, len(rps)):
            # first iteration: add rock to the first 3^(n-2) elements
            # 3^(n-2) is also the length of the array / 3
            length = int(len(arr) / 3)
            for j in range(length * i, length * (i + 1)):
                arr[j] += [rps[i]]
            
        return add_hands(n - 1, arr)

    result = []
    # set up arrays with their first elements
    for hand in rps:
        newArrs = [[hand] for i in range(0, pow(3, n - 1))]
        result += newArrs
        add_hands(n - 1, newArrs)
    return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
