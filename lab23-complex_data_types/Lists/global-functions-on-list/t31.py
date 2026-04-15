list1 = [ 1, # 1 is not iterable
    [1, 2 ,3],
    [4, 5, 6],
    [7, 8, 9],
    [10,11,12]
]

for i in list1 :
    for j in i : # we tried to iterate anything in i even integer
        print(j,end=" ")
    print()

# TypeError: 'int' object is not iterable
#  solve it as
lets solve it in another lab