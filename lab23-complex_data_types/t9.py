
var = "python"
print(f" length of {var} is : {len(var)}") # 6
print(var[: :]) # by defalut

print(" by defalut operatior")
print(var[0: :])
print(var[: :1])
print(var[:6:])
print(" Change in default values")
print(var[1: :]) # change in <start>
print(var[: 4:]) # change in <stop>
print(var[: :2]) # change in <step> or <difference>
print(var[: : -1]) # reversing of a string

print(" what if we provide out of bound value")
print(var[0: :100])
print(var[0:100:])
print(var[100: :]) # nothing is there so no output

print(" experimenting with string slicing")
print(f" length of string is : {len(var)}")

print(var[0: : 2])
print(var[0: : -2])
var = "kfaslfjajfqjuroijweirwecewcrkwerjclkejoijoi3wkeckcewkckewcklerklec"
print(var[0: :])
print(var[0: :-2]) # error
print(var[-1: :-2])



