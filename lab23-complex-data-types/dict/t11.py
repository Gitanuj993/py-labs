# Accessing Values from a key:value pair from the
dict1 = { 1 : "A" , 2 : "B" , "C" : 3}
print(f" dict1: {dict1}")
print(dict1[1])
print(dict1[2])
print(dict1["C"])

# Clearing dict1
dict1.clear()
print(f" dict1: {dict1}")

# Now completely delete dict1

del dict1
