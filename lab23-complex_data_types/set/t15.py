# .pop()

s1 = { 45,56,67,90,46,67}
print(f" s1 : {s1}")
s1.pop() # remove a random element
print(f" s1 : {s1}")

print("===============================")
rm_ele = s1.pop() # removed element return
print(f" removed element is : {rm_ele}")
print(f" updataed element is : {s1}")

print("===============================")
# removing or poping element from empty set
s2 = set()
print(f" set 2 is : {s2}")
# s2.pop()#KeyError: 'pop from an empty set'
print(f" now set 2 is : {s2}")

print("=====++++++++++++++++++++===========")

s1 = { 45,56,67,90,46,67}
print(f" s1 : {s1}")
# print(s1.pop(32)) # .pop() method do to takes any argument

