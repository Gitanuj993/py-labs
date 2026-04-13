"""
Welcome AT
aim : boolean data types
"""
#To use sys function to know address and internal storage size
import sys
a = True
#b = false # false is not a bool type
b = False
c = False
print(f" a is : {a}")
print(f" b is : {b} ")
#lets check whether id are same or different for different variables storing same bool type
print(f" id of a : {id(a)}")
print(f" id of b : {id(b)}")
print(f" id of c : {id(c)}")
# you will see the same memory address : industry prefer good memory
print(f"type of a : {type(a)}")
print(f"type of b : {type(b)}")
#memory allocated
print(f" Memory allocated to a is : {sys.getsizeof(a)}")
print(f" Memory allocated to b is : {sys.getsizeof(b)}")
print(f" Memory allocated to c is : {sys.getsizeof(c)}")
# memory allocated same as of integer



