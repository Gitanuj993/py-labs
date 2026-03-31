"""
Welcome AT
aim : boolean data type

"""
print("-----------------------------------------------------------")

# converting int to bool
num = 12
int2bool = bool(num)
print(f" num : {num} type casting to bool is : {int2bool} of type {type(int2bool)}")
print(f" num : {num} type casting to bool is : {int2bool} of type {type(int2bool)}")
num= -22
int2bool = bool(num)

print(f" num : {num} type casting to bool is : {int2bool} of type {type(int2bool)}")
print("-----------------------------------------------------------")


# converting float to bool
area = 23.43
float2bool = float(area)
print(f" area : {area} type casting to bool is : {float2bool} of type {type(float2bool)}")
area = 0.0
float2bool = float(area)
print(f" float : {area} type casting to bool is : {float2bool} of type {type(float2bool)}")
print("-----------------------------------------------------------")

#None to bool
none = None
none2bool = bool(none)
print(f" {none} to  bool is :  {none2bool} type {type(none2bool)} no Type error")


# string to bool
string1 = ""
str2bool = bool(string1)
print("-----------------------------------------------------------")
print(f" string1 : '{string1}' converted to bool is : {str2bool}")
string2 = "anything"
str2bool = bool(string2)
print(f" string2 : '{string2}' converted to bool is : {str2bool}")
print("-----------------------------------------------------------")
