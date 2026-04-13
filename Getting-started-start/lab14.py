"""
Welcome AT
Aim :	to know about type conversions 

theory : to convert one data type into another data type 
"""

# to convert other data types into int using int() function
#test -cases

string = "10"
PI = 3.14

# lest print the test cases onto the console 
print(f" This is type of int-type conversion \n")
print(f" string : {string} ")
print(f" pi : {PI}	\n")

#lets convert test-cases into int data type

num1 = int("10")
num2 = int(string)
num3 = int(PI)

# lets display what we converted
print(f" num1 is :	{num1}")
print(f" num2 is :	{num2}")
print(f" num3 is :	{num3}\n")

# Now lets convert other data types into float data type

test1 = 12
test2 = "12"
test3 = "12.3"

#lest display the test-cases
print(f" This test for float-type conversion")
print(f" test 1 is :	{test1}")
print(f" test 2 is :	{test2}")
print(f" test 3 is :	{test3}\n")


#lest convert them into float using same variable name :	yes we can do that in python lang

test1 = float(test1)
test2 = float(test2)
test3 = float(test3)

# lets print the data 

print(f" test 1 is :	{test1}")
print(f" test 2 is :	{test2}")
print(f" test 3 is :	{test3}\n")


# str() :	to convert other data types into string type

#test-cases
test1 = 12
test2 = 12.23
test3 = None

# to display the test cases
print(f" This test for string-type conversion")
print(f" test 1 is :	{test1}")
print(f" test 2 is :	{test2}")
print(f" test 3 is :	{test3}\n")

# str type conversion
test1 = str(test1)
test2 = str(test2)
test3 = str(test3)

# display the results 
print(f" test 1 is :	{test1}")
print(f" test 2 is :	{test2}")
print(f" test 3 is :	{test3}\n")

# lets convert int , float , string into bool data type
print(" --> int , float and string into bool ")
int = 12
float = 23.0
string = "happy"

print(f" int : {int}")
print(f" flaot  : {float}")
print(f" string : {string}")

print(f" ---->  thier bool formates")
print(f" int to bool : {bool(int)}")
print(f" flaot to bool  : {bool(float)}")
print(f" string to bool : {bool(string)}")

print(f" Special cases !")
i = 0
print(f" i = 0 in bool is {bool(i)}")
i = 23
print(f" i != 0 in bool is {bool(i)}")
i = ""
print(f" i = '' in bool is {bool(i)} ")
i = " anything "
print(f" i != '' in bool is {bool(i)} ")




# complex data type conversion 
"""
list to tuple
tuple to list
string to list
"""