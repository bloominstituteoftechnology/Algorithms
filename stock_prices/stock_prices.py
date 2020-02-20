#!/usr/bin/python
#[10*, 7*, 5, 8, 11, 9]

import argparse

def find_max_profit(prices):
  profit = prices[1] - prices[0] # -3
  for buy_price in prices:  #[10,7, 5, 8, 11, 9]
    for sell_price in prices[2:]:    
      if (sell_price-buy_price) > profit and (prices.index(sell_price) > prices.index(buy_price)):  #if 11-5 > -3 and 4 > 2 then profit = 6
        profit = sell_price-buy_price
        print(buy_price, sell_price)
        print(f"Profit: {profit}")    
  return profit  #6

# 7 - 10 = -3
# profit = -3


     
    
    
  
    


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))