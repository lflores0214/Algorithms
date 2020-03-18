#!/usr/bin/python

import argparse
'''
-receives a list of of prices
-supposed to return the max profit
-think of the list of prices as prices of one stock that increases or decreases each day
for example: [10, 12, 6] 10 would be the price of when you bought it, 12 would be the price the next day. and 6 would be the price for the day after that.
-you can only sell at 12 or 6
-selling at 12 would yield the max_profit of 2 (12 - 10)
also possible to have negative profit if the price of the stock keeps decreasing each day
So max_profit can be negative
can set it to float('-inf') found in help channel
min_price wouldn't have a cap on how high it could be so we can set it to float('inf')
loop through array to find the new lowest price and set it
find the difference between the last index of the array and everything to the left of the array
Will have to do a double loop to be able to iterate all prices
Turns out I'm not using min_price for anything ?
'''


def find_max_profit(prices):
    min_price = float('inf')
    max_profit = float('-inf')
    # loop through array
    for i in range(len(prices) - 1):
      # find the new min_price by looping and assign the lowest number to min_price
        if prices[i] < min_price:
            min_price = prices[i]

            for j in range(len(prices) - 1):
              # loop through the array and subtract prices[i] from prices[j] as j iterates and finds all differences between prices[j] and prices[i]
                # if j is <= to i pass since you cannot sell before you buy
                if j <= i:
                    pass
                else:
                    current_profit = prices[j] - prices[i]

                    print(current_profit)
                    if current_profit > max_profit:
                      max_profit = current_profit
    return max_profit


stonks = [10000, 1000, 5900, 50, 5000, 10]
find_max_profit(stonks)


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
