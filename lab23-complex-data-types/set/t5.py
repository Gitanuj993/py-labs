# Intersection of sets return a new set containing common elements from both sets

set1 = { 1 , 3, 4, 5, 5} # duplicate elements will remove
set2 = { 3 , 4 ,5 ,6}
set3 = { 6,7,8,9,0}
print(f"set 1 : {set1}")
print(f" set 2 : {set2}")

# Intersection of two or more set is governed by '&' symbol
print(set1 & set2 & set3) # return empty set 'set()' if no thing is common

print("-----------------------------")
set1 = { 1 , 3, 4, 5, 6} # duplicate elements will remove
set2 = { 3 , 4 ,5 ,6}
set3 = { 6,7,8,9,0}
print(f"set 1 : {set1}")
print(f"set 2 : {set2}")

# Intersection of two or more set is governed by '&' symbol
print(f"Intersection of all these three set is : {set1 & set2 & set3}") # return empty set 'set()' if no thing is common
