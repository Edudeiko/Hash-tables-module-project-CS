

# expensive calculation on the fly

import math

lookup_table = {}


def inverse_root(n):
    return 1 / math.sqrt(n)


for ii in range(1, 1000):
    lookup_table[ii] = inverse_root(ii)


print(lookup_table[995])


# rainbow table
# hash common passwords ahead of time

# hashing function for pws schould be slow
