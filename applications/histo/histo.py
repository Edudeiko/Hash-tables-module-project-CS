import numpy as np
import re

import matplotlib.pyplot as plt

from collections import Counter
with open("robin.txt") as f:
    words = f.read()


# a = []
# count = 0
d = dict()
# filename = 'robin.txt'
# with open(filename, 'r') as f:
words = words.lower()
words = words.split()
for word in words:
    clean_word = re.sub(r'[^a-zA-Z0-9]+', "", word)
    if clean_word not in d:
        d[clean_word] = 1
    else:
        d[clean_word] += 1


d = list(d.items())
d.sort(reverse=True, key=lambda pair: pair[1])

count = d[0:15]

counts = Counter(count)
width = 120  # Adjust to desired width
longest_key = max(len(key) for key in counts)
graph_width = width - longest_key - 2
widest = counts.most_common(1)[0][1]
scale = graph_width / float(widest)
for key, size in counts.items():
    print('{}: {}'.format(key, int(size * scale) * '*'))

# num = Counter(d)
# x = list(num.values())
# y = list(num.keys())

# x_coordinates = np.arange(len(num.keys()))
# plt.bar(x_coordinates, x)
# plt.xticks(x_coordinates, y)
# plt.show()
# print(x, y)
