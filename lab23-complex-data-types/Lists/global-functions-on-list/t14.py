# Methods special methods of lists defined in list class
# list is a dynamic array or simply a resizable array,
# actually in any language array's size is not extended each time a new array is created
# l1 = [1,2,3,4,5]
l2 = [ 11 , 22 ,33]

print(f" l1 : {l1} of length : {len(l1)}")
print(f" l2 : {l2} of length : {len(l2)}")

print("---------------------after append ------------")
# list.append(x)

l1.append(l2) # it will not return a new list like immutable data types ,
print(f" l1 : {l1} of length : {len(l1)}")
print(f" l2 : {l2} of length : {len(l2)}")


# whether list are mutable or immutable , we can check it by id() function or by
# knowing address of the previous list and new list
