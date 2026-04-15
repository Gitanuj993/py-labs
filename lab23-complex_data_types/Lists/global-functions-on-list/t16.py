# list.insert(x,y) function which insert element y at index x and shift previous element at
# index x to the next index say ( x + 1 )

l1 = [10,20,30,40,50]
print(f" list 1 is : {l1}")
# insert element 89 at index 3
#lets print the element at index 3
print(f" element at index 3 is : {l1[3]}")
l1.insert(3,89)
print(f"----------Modified list ---------------")

print(f" list is : {l1}")
print(f" element at index 3 is : {l1[3]}")

# shifting happen in case of insert , insert(x,y) method can't override the previous entry
# 1. It shift elements at index x to next index and so on
# 2. after shifting insert(x,y) method insert element y at index x
