

list1 = list() # list() created a new list
# list1 is a iterable
print(f"list 1 is : {list1}")
print(f"len of list1 is : {len(list1)}")


# list(*iterables) # sequence
# test1 = list(1,2,3)  # Type Error
# print(f" test1 is : {test1}")
# print(f" type of test1 is : {type(test1)}")


str1 = "Engineer"
test2 = list(str1)

print(f"str1 is : {str1}")
print(f" test 2 is : {test2}")

tuple1 = (1,3,4,5) # it is complex data type we will see it later
test3 = list(tuple1) # with the help
print(f"str1 is : {tuple1}")
print(f" test 3 is : {test3}")
