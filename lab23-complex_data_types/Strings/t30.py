# string type conversion

# we can convert any type of element into a string using str() functions
# let's see

num1 = 12
num2 = 12.3
bool = True
none = None

print(f" {num1} as string : {str(num1)}")
print(f" {num2} as string : {str(num2)}")
print(f" {bool} as string : {str(bool)}")
print(f" {none} as string : {str(none)}")

print(f" type of num1 is : {type(num1)}")
stringConversion = str(num1)
print(f" now type of converted object is : {type(stringConversion)}")