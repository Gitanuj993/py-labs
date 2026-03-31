# relationa operetors on different data types - edge cases
# implicit type conversion
# string ascii and unicode

print(f" 'A' == 'a' is : {'A' == 'a'}")
print(f" 'A' == 'A' is : {'A' == 'A'}")
print(f"  1 == 1.0  is : { 1 == 1.0}")
print(f" 'A' == 65  is : { 'A' == 65} *") # ord("A") and chr(65) # why false
# python support use of unicode ( stored in Hexadecimal ) thus "A" is not equal to 65 in python
print(f"  99 == 1 is : {99 == 1}")
print(f" 1 == True is : { 1 == True }")
print(f" 1 == '' is : {1 == ""}")
print(f" False == '' is : {False == ''}")
print(f" False != '' is : {False != ''}")
print(f" 'apple' > 'apple is : {'apple' > 'apple' }")
print(f" 'apple' < 'apple is : {'apple' < 'apple' }")
print(f" 'apple' == 'apple is : {'apple' == 'apple' }")

print(" numerical compared to alphanumeric ")

print(" numeric to numeric either int to int , or float to float ")

print(" int , float to bool type ")
print(f" 5 > True is : {5 > True}")
print(f" 5 < True is : {5 < True}") # True

print("--------------",'\n')
print(f" 1 == True is : {1 == True}")
print(f" 1 != True is : {1 != True}")
print(f" 0 == False is : { 0 == False}")
print(f" 0 != False is : { 0 != False}")






