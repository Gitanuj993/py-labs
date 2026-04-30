# list.pop(<x>) method used to delete an element of the list using index of the element and it return deleted element

list1 = [ 1,2,3,4,5]

print(f" list 1 is : {list1}")

deleted1 = list1.pop() # it deleted last element by if no index is given
print(f" list 1 is : {list1} after deleting last element ")
deleted2 = list1.pop(0) # remove element ny its index
print(f" list 1 is : {list1} after poping element at first index")


