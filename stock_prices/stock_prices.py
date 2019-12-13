#!/usr/bin/python

import argparse

# init commit


# i is 1 then j only goes to 0
# i is 2 then j goes to 0,1
# i is 3 then j goes to 0,1,2
# etc

# Pseudo
# Initialize max profite to second - first value
# Let i increment ahead and let j start from beginning
# Subtract i from j at 0, then j at 1, up to i, etc
# See if any are higher than max profit that was initialized and give it that value
def find_max_profit(prices):

  # Initializing max_profit
    max_profit = prices[1] - prices[0]
    for i in range(1, len(prices)):
        j = 0
        print("i", i)
        while j < i:
            print("j", j)
            if prices[i] - prices[j] > max_profit:
                max_profit = prices[i] - prices[j]
                print(max_profit)
            j += 1
    return max_profit


print(find_max_profit([10, 7, 5, 8, 11, 9]))
# Flow of this function:
# i = 1, j = 0,  7 - 10 = -3 initialized
# i = 2, j = 0,  5 -10 = -5, max_prof doesnt change
# i = 2, j= 1,   5 - 7 = -2 so max_prof is now -2
# i = 3, j = 0,  8 - 10 = -2, max_prof no change
# i = 3, j = 1,  8 - 7 = 1, max_prof = 1
# i = 3, j = 2,  8 - 5 = 3, max_prof = 3
# i = 4, j = 0,  11 - 10 = 1, max_prof no change
# i = 4, j = 1,  11 - 7 = 4, max_prof = 4
# i = 4, j = 2,  11 - 5 = 6, max_prof = 6
# i = 4, j = 3,  11 - 8 =  3, max_prof no change
# etc


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
