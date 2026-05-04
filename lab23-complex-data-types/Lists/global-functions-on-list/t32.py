# Matrix can be represented as list of lists
list1 = [1,  # 1 is not iterable
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]
         ]

for i in list1:
    if type(i) == type(list1) : # this approach would fail in other iterables

        for j in i:  # we tried to iterate anything in i even integer
            print(j, end=" ")
        print()
    else : print(i) # non list type
