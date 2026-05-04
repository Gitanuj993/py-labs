# all() check for truthy and falsy values and keys


d1 = dict(a=1, b=2, c=3) # keyword positional arguments
print(f" d1 is : {d1}")

print("=======================")

d1 = { "a" : False , "b" : True , }
print(any(d1)) # True
print(any(d1.values())) # True
print(all(d1.values())) # False
print(all(d1.keys())) # True


