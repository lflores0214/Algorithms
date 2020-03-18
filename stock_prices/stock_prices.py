#!/usr/bin/python

import argparse
'''
receives a list of of prices
supposed to return the max profit
can only sell if the arr if you already bought
'''
def find_max_profit(prices):
  min_price = 0
  max_profit = 0
  for i in range(len(prices)):
    for j in range(len(prices)):
      if prices[i] < prices[j]:
        min_price = prices[i]
  print(min_price)

my_arr = [1050, 270, 1540, 3800, 2]
find_max_profit([1050, 270, 1540, 3800, 2])


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))