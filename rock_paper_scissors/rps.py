#!/usr/bin/python

import sys

# define valid moves.....no 'spock', 'monster' etc.
validMoves = [['rock'], ['paper'], ['scissors']]


def rock_paper_scissors(n):
    valid_plays = [["rock"], ["paper"], ["scissors"]]
    # Base case: return empty list if n is zero
    if n == 0:
        return [[]]
    # If n is 1 return valid_plays
    if n == 1:
        return valid_plays

    # Create empty list to store results
    output = []
    # Recursively call function for rounds n
    rounds = rock_paper_scissors(n - 1)
    # For each round
    for round in rounds:
        # For each valid play
        for play in valid_plays:
            # Add new play to round in output
            new_play = round + play
            output.append(new_play)

    return output


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
