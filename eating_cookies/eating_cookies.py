#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    #* Not using cache
    if n <= 0:
        return 1
    if n == 1:
      return 1
    if n == 2:
        return 2
    if n == 3:
      return 4
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    
    #* Using Cache
    # if cache is None:
    #   cache ={0: 1, 1: 1, 2: 2, 3: 4}
    # if n <= 0:
    #     return 1
    # if n == 1:
    #     return 1
    # if n == 2:
    #   return 2
    # if n == 3:
    #   return 4
    # elif cache and cache[n]:
    #   if cache[n]:
    #     return cache[n]
    # else:
    #   cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    
    # return cache[n]
print(eating_cookies(10))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
'''
def eating_cookies(n, cache={0: 1}):
  if n < 0:
    return 0
  if n not in cache: cache[n] = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
  return cache[n]
'''