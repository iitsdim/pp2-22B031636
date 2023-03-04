from time import sleep

import numpy as np
import operator as op

# 1
# L = [1, 2, 4]
# print(np.prod(L))

# 2
# s = 'AbwwW'
# print(sum (1 for x in s if x.islower()))
# print(sum (1 for x in s if x.isupper()))

# 3
# s = "wwA"
# print(list(x for x in s) == list(reversed(s)))

# 4
# x = int(input())
# wait = int(input())
# sleep(wait / 1000)
# print(f"Square root of {x} after {wait} miliseconds is {x ** (1/2)}")

# 5
my_tuple = (True, True, True)
print(all(my_tuple))