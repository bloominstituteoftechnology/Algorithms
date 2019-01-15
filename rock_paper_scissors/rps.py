#!/usr/bin/python

import sys

# avoids mispelling them
rock = "rock"
paper = "paper"
scissors = "scissors"


def rock_paper_scissors(n):
    # number of possible outcomes
    """amount = 3 ** n

    if cache == []:
        cache.append([rock] * n)

    if len(cache) == amount or n <= 1:
        return cache

    for i in range(n):
        this = cache[iter]
        that = this
        this[i] = paper
        that[i] = scissors
        cache.append(this)
        cache.append(that)

    return rock_paper_scissors(n-1, cache=cache, iter=iter+1)"""

    results = [[rock], [paper], [scissors]]
    
    if n < 1:
        return [[]]
    elif n == 1:
        return results

    # O(n^2)
    final_results = []
    for _ in range(1, n):
        for result in results:
            final_results.append(result + [rock])
            final_results.append(result + [paper])
            final_results.append(result + [scissors])
        
        results = final_results
        final_results = []
    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
