#!/usr/bin/python
'''
the function takes n as a parameter 
n represents a the amount of money in cents 
so if n = 50 that would be 50 cents
the fn is supposed to figure out how many ways there are to make change for the amount of n 
if n = 50 the fn has to figure out how many ways there are to make change for 50 cents
the coins we can use are pennies(1c) nickels(5c) dimes(10c) quarters(25c) and half-dollars(50c)
for 50 cents we can make change using:
  1 half-dollar (50c)
  2 2 quarters (25c)x2
  50 pennies (1c)x50
  5 dimes (10c)x5
  10 nickels (5c)x10
  etc. 50 cents might be too big to do by hand
n = 10
  10 pennies
  5 pennies 1 nickel
  2 nickels
  1 dimes
    4 ways
n = 15
  15 pennies
  10 pennies 1 nickel
  5 pennies 2 nickels
  5 pennies 1 dimes
  3 nickels
  1 nickel 1 dime
    6 ways
the problem is a more difficult version of eating_cookies (how many ways are there to make up a given number)
only this time you can only make up that number using a certain numbers(coin values in this case)
will need to make a list of coins we can use
coins = [1, 5, 10, 25, 50]

'''
import sys

coins = [1, 5, 10, 25, 50]


def making_change(amount, denominations, cache=None):
    if cache is None:
        cache = [0] * (amount + 1)
        cache[0] = 1
    # if cache[amount] is not None:
    #   return cache[amount]
    for coin in denominations:
        print(f"coin: {coin}")
        for higher_amount in range(coin, amount + 1):
            print(f"higher_amount: {higher_amount}")
            difference = higher_amount - coin
            cache[higher_amount] += cache[difference]

    return cache[amount]


print(making_change(15, coins))
'''

n = 13
 - 13 pennies
 - 8 pennies 1 nickel
 - 2 nickels 3 pennies
 - 1 dime 3 pennies
  - 4 ways
n = 10
  10 pennies
  5 pennies 1 nickel
  2 nickels
  1 dimes
    4 ways
n = 15
  15 pennies
  10 pennies 1 nickel
  5 pennies 2 nickels
  5 pennies 1 dimes
  3 nickels
  1 nickel 1 dime
    6 ways
'''
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
