import math
import random
import time

start = time.time()  # start timer


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


lookup_table = {}  # create an empty hache table
# precomputed table for caching the output of cryptographic hash functions
for x in range(2, 14):
    for y in range(3, 6):
        lookup_table[(x, y)] = slowfun_too_slow(x, y)


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    return lookup_table[(x, y)]


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')


finish = time.time()
result_time = finish - start
print('---------------------')
print(f'time to run "hached" test is {result_time:.2f} seconds')
