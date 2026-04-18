# frozenset - do not allow duplicate , used as global functions

set1 = { 1,2,3,4}
set2 = { 6,7,8,9}

print(f" set1 is : {set1}")
print(f" set2 is : {set2}")

# now we want a set inside a set
nestedSet = {frozenset(set2)}
print(f" nestedSet is : {nestedSet}")

set2.add(frozenset(nestedSet))
print(f" set2 is : {set2}")

set1.add(frozenset(set2))
print(f" set1 is : {set1}")

print("===============================================")

