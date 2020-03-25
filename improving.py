# [0, 1, 3, 5, 8, 13, 21]

cache = {0: 1, 1: 1}
def rec_fib(n):
    #base case
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    if n in cache:
        return cache[n]
    
    # if tis not in the cache, we must
    cache[n] = rec_fib(n-1) + rec_fib(n-2)
    return cache[n]

print(rec_fib(10))