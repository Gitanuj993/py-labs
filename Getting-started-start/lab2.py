"""
Welcome AT
AIM :	to  know about strings data type 
"""
"""
Qans :  string is a collection of characters , used to store text .
space is also included in  string
"""
import sys
text = " Welcome AT "
string = text
print(text)

print(f" Adress of text : { id(text)}")
print(f" Adress of string: { id(string)}")
print(f" Length of string as number of characters in the text : {len(text)}")
print(f" Size of string internally is :	{ sys.getsizeof("") } ")
print(f" Size of string internally is :	{ sys.getsizeof(text) } ")
print(f" address of reference factor is :	{ sys.getrefcount(text)}")

