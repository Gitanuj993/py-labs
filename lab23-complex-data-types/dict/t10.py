# None as a value in dictionary

dict1 = {1 : None, 2 : None, 3 : None}
print(f" dict1: {dict1}")

# list , tuple and set in dictionary

dict2 = {1 : None , 2 : [1,2,3] , 3 : (4,5,6) , 4 : {7,8,9}}
print(f" dict2: {dict2}")

# inserting value in variable into the dict
myList1 = [1,2,3,4,5]
myTuple1 = (1,2,3,4,5)
mySet1 = {1,2,3,4,5}
myString1 = "Hello"
print(f" myList1: {myList1}")
print(f" myTuple1: {myTuple1}")
print(f" mySet1: {mySet1}")

myDict3 = { 1 : myList1 , 2 : myTuple1 , 3 : mySet1 , 4 : myString1 }
print(f" myDict3: {myDict3}")

# now reverse the things , like mylist , tuple in key side

# myDict4 = {myList1 : 1 , }
# TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

myDitct4 = { myString1 : 1}
print(f" myDitct4: {myDitct4}") # immutable type string supported

# myDict4 = {mySet1 : 1 , }
# TypeError: cannot use 'set' as a dict key (unhashable type: 'set')

myDict4 = {myTuple1: 1, }
print(f" myDict4: {myDict4}") # immutable type string supported
