# any() global function

dict1 = {}
print(f" dict1 : { dict1 }") # {}
print(f" Truthy value , any() : {any(dict1)}") # False
print(f" all(dict1) : {all(dict1)}")  # False

# case 1 :
d1 = { 0 : "zero" , False : False}
print(any(d1)) #False
print(any(d1.values())) # True
print("---"*38)
d2 = {  1 : "One" , True : "True"}
print(any(d2)) # True
print(any(d2.values())) # True

print("---"*38)

# dictionaries are stored in hash tabel, dictionary used hashing , but why insertion order can't change.

# When True and False as key - empty string , Edge cases and brain teasing.
# can i have falsy case , magic or brain teasing
d3 = { 0 : "Zero", False : "False1"}
print(any(d3)) # False
print(any(d3.values())) # True
print(d3) # what does it print , False internally stored as 0 and True internally stored as 1.