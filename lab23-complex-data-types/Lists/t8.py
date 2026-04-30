

import sys

a = 1
print(f" size of a : {sys.getsizeof(a)}")
l0 = []
l1 = [a]
l2 = [1]
print(f" size of a : {sys.getsizeof(l0)}")
print(f" size of a : {sys.getsizeof(l1)}")
print(f" size of a : {sys.getsizeof(l2)}")


# see help(list)