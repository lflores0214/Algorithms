# print the factorial of n


def rec_fac(n):
    # base case
    if n <= 1:
        return 1
    # what step can we do recursively
    prev = rec_fac(n-1)
    return n * rec_fac(n-1)


print(rec_fac(25))
