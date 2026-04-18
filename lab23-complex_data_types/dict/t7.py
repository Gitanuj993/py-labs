# Dictionary comprehension

list1 = [1, 2, 3, 4, 5]
print(f" list1: {list1}")

list2 = [1,"A",2,"B",3,"C",4,"D",5,"E"]
print(f" list2: {list2}")
for item in list2 :
    print(f"{item}",end= " ")

print("\n","-"*50)

myDict = {x : x for x in list2}
mydict2 = { x : x*x for x in range(10) }
print(f" myDict: {myDict}")
print(f" myDict2: {mydict2}")


