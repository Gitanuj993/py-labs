"""
Welcome AT
aim : None

theory  : None suggest " Absence of value
    None can be used to declear variables without assigning any value
    None is an object
    None is a built-in constant
    None has 16 byte internal storage as datatype pointer takes 8byte , reference_counter takes 8 bytes
"""
import sys
a = None
b = None
c = None
a = b = c = None
#type : type of the data
print(f" type of a : {type(a)}")
print(f" type of b : {type(b)}")
print(f" type of c : {type(c)}")

#Memory address
print(f" Memory required by the None is : {sys.getsizeof(None)}")

#sys valuse
print(f" internal memory of a : {a}")
print(f" internal memory of b : {b}")
print(f" internal memory of c : {c}")

# refrernce counter : Adress
print(f" reference counter a : {sys.getrefcount(a)}")
print(f" reference counter b : {sys.getrefcount(b)}")