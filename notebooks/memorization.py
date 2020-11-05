import sys
# memorization, closely related to dynamic programming
# DP: top down, breakthe problem up as you reuse previous result

# key is what you have, value is what you calculate

# fibonacci sequence
# a function that returns the n-th item in the fibonacci sequence
# golden proportion

# 0 1 1 2 3 5 8 13 21 34 55 89

# let's do it recursively
cache = {}


def fib(n):

    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib(n - 1) + fib(n - 2)

        return cache[n]


print(fib(3))  # 2
print(fib(11))  # 89
print(fib(25))
print(fib(500))
print(sys.getrecursionlimit())
