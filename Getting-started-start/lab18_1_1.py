"""

aim : modulus
"""
a = -10
b = 3
print(f" a = {a} and b = {b}")
print(f" a / b is :   {a/b}")
print(f" a // b is : { a // b}") # why can't -3
print(f" a % b is : { a % b}") # why  can't  1

import math
# becouse of
# formula to calculate remainder is :
# a % b = a - (b * math.floor(a/b))
rem = a - (b * math.floor(a/b))
print(f" remainder of a % b is : {rem}")


