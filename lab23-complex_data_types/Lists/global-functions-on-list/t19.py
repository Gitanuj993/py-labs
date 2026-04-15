# inserting elements at out of bound index ,
# what if we insert element at index > n-1 (length of list left to right , positive indexing)
# index < -n ( -n used in negative indexing

# lets take a list of numbers upto 5 ,
list1 = [ 1,2,3,4,5] # index [ 0 , 1 , 2 ,3, 4 ] respectively

print(f" length of list : {list1} is : {len(list1)}")

# In case of positive indexing
list1.insert(99,11)
print(f" updated list is : { list1}")


# In case of Negative indexing
list1.insert(-99,900)
print(f" updated list is : {list1}")


