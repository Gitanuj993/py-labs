# Matrix can be represented as list of lists
# lets solve the previous problem
list1 = [1,  # 1 is not iterable
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]
         ]

# Without  using isinstances

for i in list1 :
    if (type(i) == type(1.0) or (type(i) == type(1))) :
        print(i)
    else :
        for j in i :
            print(j,end=" ")
        print()

