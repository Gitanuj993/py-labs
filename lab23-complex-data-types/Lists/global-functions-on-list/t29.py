# Nested List

list1 = [
    [1, 2 ,3],
    [4, 5, 6],
    [7, 8, 9],
]

# Acess Elements line by line using index

# print element 1
print(f" element 1 is : {list1[0][0]}")
# print element 8
print(f" element 1 is : {list1[2][1]}")

for i in list1 :
    for j in i :
        print(j , end=" ")
    print()
# same thing you will see in libraries like numpy and pandas
