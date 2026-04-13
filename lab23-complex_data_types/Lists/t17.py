# list inside list  level2

list1 = [ [1,2,3] , [4,5,6,[12,34,[100]]]]
list2 = [ [10,20,30] , {5 ,6 , 7} , ( 1,3,4,56) , {"name" : "AT" , "id" : 121}]
print(f" list1 : {list1}")
print(f" list2 : {list2}")

print(f' Traversing list 1 ')

for i in list1 :
    print(i , end=" -> ")

print()
for j in list2 :
    print(j ,end = " ")

