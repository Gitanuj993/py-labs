# .remove(x) : used to remove an element if found , throw an Key Error if element not found
s1 = { 45,56,67,90,46,67}
print(f" set 1 is : {s1} ")

# s1.remove() #TypeError: set.remove() takes exactly one argument (0 given)
s1.remove(45)
print(f" set 1 is : {s1} ")
