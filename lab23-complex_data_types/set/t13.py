# .add(x)

t1 = { 45,56,67,90,46,67}
t2 = {5,6,7}
print(f" t1 is : {t1}")
# let's add an element 78 in t1
t1.add(78)

print(f" now updated set is : {t1}")

# now we want to to  add more than one element

t1 = { 45,56,67,90,46,67}
t2 = {5,6,7}
print(f" t1 is : {t1}")
print(f" t2 is : {t2}")

t2.update(t1) # t2 is updated
print(f" updated t2 is : {t2}")

# what if we take list as an argument in the .update(<it>) method