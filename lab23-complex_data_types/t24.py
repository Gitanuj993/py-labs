
# to check

#check for lower case
print("#check for lower case")
var = "welcome"
isLower_var = var.islower() # no arguments passed  # by default self is passed in the class
print(isLower_var)

#check for upper case
print("#check for upper case")
upper = "ADKDL"
print(upper.isupper())

# check for titles
print("# check for titles")
title = "New Like"
print(title.istitle())
title1 = "New like"
print(title1.istitle())


# digit1 = 123
# print(digit1.isdigit())  # Error

# pi = 3.14   # Atribute Error
# print(pi.isdecimal())

# check for digits
print("# check for digits ")
digit1 = "123"
print(digit1.isdigit())
digit2 = "123.33"
print(digit2.isdigit()) # false

print(" check for decimal")
pi = "3.14"
print(pi.isdecimal()) # why false

print(" check for numerics")
num = "123"
num2 = "123.32"
print(f" {num} is numeric : {num.isnumeric()}")
print(f" {num2} is numeric : {num2.isnumeric()}") # false float type

print(" check for Alphabets")
test1 = "HEllo"
test2 = "kfdkd"
print(f" {test1} is alpha : {test1.isalpha()}")
print(f" {test2} is alpha : {test2.isalpha()}") # false float type

# ex
print(" check for Alphanumeric ")
test1 = "HEllo123"
test2 = "kfdkd123.34"
test3 = "akdld#$#12"
print(f" {test1} is Alphanumeric : {test1.isalnum()}")
print(f" {test2} is Alphanumeric : {test2.isalnum()}") # false float type
print(f" {test3} is Alphanumeric : {test3.isalnum()}") # false float type


