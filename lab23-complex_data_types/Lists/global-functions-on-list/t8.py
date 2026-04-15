# iterator object address
# what is iterator

t1 = [ 1 ,2,4,5]
revt1 = reversed(t1) # reversed != sorted  # reversed is a global function
print(f" t1 : {t1}")
print(f" reversed t1 : {revt1}") # address would be returned

print(f" Actually reversed string looks like : {list(revt1)}")

for i in list(revt1) :
    print(i)


# why reversed() global function return address of the iterator
"""
Why Python does this

This design:

Saves memory (no new list is created immediately)
Makes iteration efficient
Follows the iterator protocol used throughout Python

source : chatgpt"""