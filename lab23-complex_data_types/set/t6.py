# Difference of sets
set1 = { 1 , 3, 4, 5, 6} # duplicate elements will remove
set2 = { 3 , 4 ,5 ,6}
set3 = { 6,7,8,9,0}

print(f" set1 : {set1}")
print(f" set2 : {set2}")
print(f" set3 : {set3}")

# What would be the differnce of set1 from set 2 ?
print(f" difference of set1 - set2 is : {set1 - set2}") # 1,
print(f" difference of set2 - set2 is : {set2 - set2}") # set()
print(f" difference of set1 - set3 is : {set1 - set3}") # 1,3,4,5

print("------------------------------------------")

print(f" difference of set2 - set1 is : {set2 - set1}")
print(f" difference of set3 - set2 is : {set3 - set2}")
print(f" difference of set2 - set3 is : {set2 - set3}")
