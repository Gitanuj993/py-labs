# global-functions-on-list


### Table of content


## We can access and modify elements of list
> We can add and modify element of the list using its indexed ,
```pycon
list1 = [0,1,2,3,4,]
print(list1[0]) # access element of list at the index 0
```
# modify element 
```pycon
list1 = [ 1 , 2,3 ,4 ,5 ]
print(list1[0])
list1[0] = 99
print(list1[0])

```



1. 


## list of  global functions 
> Global functions are those which can perform operation isrrespective of data type

1. len(var) : Return length of list
2. max(var) : return max element
3. min(var) : return minimum element
4. sorted() : iterable as a parameter , return a new list
5. reversed() :
6. any()
7. all()
8. enumerate()
9. zip(list1,list2) : it combines consecutive elements of two complex data types


## Methods of lists 

> Without parameters


> Methods With Parameter  
1. list.append(<element>) # also another complex data type variable or whole data
`` This function add whole values at the end of the list as a single element``
2. list.extend(<iterable_or_value>) : it adds multiple elements of iterable as a seperate element of the list `` extend append the elements at the end of the list`` 
3. list.insert(<index>, <object>) : ``insert object <object> at index <index> ``
4. list.remove(x) `` x is object which is to be deleted``



### List Methods without parameters
1. list.clear() : `` Clear whole elements of the list , not the list
2. list.reverse()  : reverse the object or iterable or list , 
> .reverse() method reverse the list inplace 

### List methods with parameters and return a value
1. list.pop(<index>) : it takes an index and return the deleted element at index <index>
2. list.index(<object>) : it return the index of the object
3. list.count(x) : x is an object 
4. list.sort() : sort the interable using Tim sort ( insertion + Merge sort)
5. 