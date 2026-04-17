# set operation using functions , a new set will be returned

s1 = { 45,56,67,90,46,67}
s2 = { 1,2,3,4}

print(f"s1 = {s1}")
print(f"s2 = {s2}")

s3 = s1.union(s2)
s4 = s1.difference(s2)
s5 = s1.symmetric_difference(s2)
print(f" union of s1 and s2 is : {s3}")
print(f" difference of s1 and s2 is : {s4}")
print(f" symmetric_difference of s1 and s2 is : {s5}")
