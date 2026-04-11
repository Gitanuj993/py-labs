
# String Formmating

a = 10
b = 20

print(" a : ",a , " b is : ",b) # previous
name = "AT"
print(" Welcome " + name) # string concatenation
# print(" Hii" + a) # type Error

print(f" a is : {a} and b is : {b} ") # formatted string


# version

print( " id : %d and name is : %s"%(101,name) ) # %d is for int or digits , %f for float , %s for strings

# formatting in python
# .format() method
name = "AT"
age = 20

print(" Welcome {} ".format(name))

#
print("I am {1} and I am {0} years old".format(25, "Alice")) # o , 1
# 3. Keyword arguments
print("Name: {name}, Age: {age}".format(name="Alice", age=25)) # also used in DBMS + python



