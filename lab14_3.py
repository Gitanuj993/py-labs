"""
Welcome AT
aim : float type conversion
"""
# 1 . int to float
print("-------------------------------------")
print(f"int to float conversion ")
num = 12
num2float = float(num)
print(f" num : {num} type casted to float is : {num2float} type {type(num2float)}")
num = 0
num2float = float(num)
print(f" num : {num} type casted to float is : {num2float} type {type(num2float)}")
num = -12
num2float = float(num)
print(f" num : {num} type casted to float is : {num2float} type {type(num2float)}")


#2. string to float
print("-------------------------------------")
print(f" string to float conversion ")
str1 = "123"
str2float = float(str1)
print(f" string 1 : {str1} type casted to float is : {str2float} type {type(str2float)}")
str1 = "123.321"
str2float = float(str1)
print(f" string 1 : {str1} type casted to float is : {str2float} type {type(str2float)}")

#what if we want to convert al123 to float
str1 = "abc12"
# str2float = float(str1)
# # ValueError: could not convert string to float: 'abc12'
# print(f" string 1 : {str1} type casted to float is : {str2float} type {type(str2float)}")



#3. bool to float


#4. None to float

#5. float to float

