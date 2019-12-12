#!/usr/bin/python

import argparse

def find_max_profit(prices):
  pass


"""
function find_max_profit(prices) {
  let buy;
  let amount = prices[1] - prices[0];
  let amountIndex = 0;
  let currAmount;
  let holder = {}
  let highest = 0;

  for (let i = 1; i < prices.length -1; i++) {
    buy = prices[i]

    for (let j = i+1; j < prices.length; j++) {
      if (prices[j] > buy) {
        currAmount = prices[j] - buy
        if (currAmount > amount) {
          amount = currAmount
          amountIndex = j
        }
      }
    }

    if (amount !== 0) {
      holder[i] = {
        amount,
        buy: prices[i],
        sell: prices[amountIndex]
      }
    }

    if (i > 1) {
      if (holder[i-1] && holder[i]) {
        if (holder[i-1].amount > holder[i].amount) {
          if (highest < holder[i-1].amount) {
            highest = holder[i-1].amount
          }
        } else if (holder[i-1].amount < holder[i].amount) {
          if (highest < holder[i].amount) {
            highest = holder[i].amount
          }
        }
      }
    } else if (holder[i]) {
      highest = holder[i].amount
    }
    amount = 0
  }
  console.log(holder)
  return highest
}
"""


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))