"""
WELCOME AT 
LAB : 14
AIM : To know about complex data types

following are the complex data types as follow
list data type : like array but can hold different types of data either int , float , string
tuple data type :	like list data type , tuple also hold the various types of elements  However it is immutable in nature.
set data type : like list but in set all the elements must be unique
dict data type : like json made of key value pair in which key is immutable and value is mutable or can be changed
"""
#Working with list 
# an empty list 
list0 = [] 
list1 = []
list0.append(99)
list2 = [1,2,3,4,5]
list3 = [1,1,2,3,4,5]



print(f" list 0 is :	{list0}") 
print(f" list 1 is :	{list1}") 
print(f" list 2 is :   {list2}") 
print(f"list3 is :	 {list3}")
# list inside a list
list1.append(list0)
print(f" List 1 is :	{ list1 } you can see that list has [] which mean list inside a list" ) 
print("\n")
# accessing elements using  indexes
print(list2[0])
print(list2[1])
print(list2[2]) # and so on 

# changing list elements using indices , yes we can do this 
print(f" list2 is :	{list2} ")
# lets change 2 , we replace 2 by 11 ,thus 2 comes in 1st index number then
list2[1] = 11
print(f" list2 is :	{list2} ")

# not limited to it.

