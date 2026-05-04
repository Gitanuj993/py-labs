# sorted global function
set2 = { 10, 20,40,30}
print(f"set2 : {set2}")
print(sorted(set2)) # sorted function would always return a list
print("========================")

set2 = { 10, 20,40,30} # set
print(f"set2 : {set2}")
list1 = sorted(set2)
print(f"sorted list of set2 : {list1}")
set3 = set(list1)
print(f"set 3 is : {set3}") # hashing value # output from

# constructor or using explicit type conversion
# print(f" reversed : { reversed(set3)}")
# TypeError: 'set' object is not reversible