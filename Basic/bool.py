'''
Welcome AT

aim : In this lab we will know about bools or boolean values
There us two types of boolean values which follows boolean algebra

1. True : which means 1  or on condition
2. False : it interpreted as off , or 0
'''
# bool
# to know memory allocation to
import sys
a = True
b = False
# lets discuss about their type : how can we find out the data type of variable using built-in function type()
print(f" Type of a is : {type(a)}")
print(f" Type of b is : {type(b)}")

print(sys.getsizeof(a))
print(sys.getsizeof(a))

print(f" Adress of a is : {id(a)} ")
print(f" Adress of b is : {id(b)} ")