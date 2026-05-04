# Matrix can be represented as list of lists
# lets solve the previous problem
list1 = [1,  # 1 is not iterable
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]
         ]

# using isinstances
for i in list1 :
    # print(i)
    if (isinstance(i,int) or isinstance(i,float) ): # check for the instance of any class
        print(i)
    else :
        for j in i :
            print(j,end=" ")
        print()





"""
for item in list :
    if isinstance(item,list) :
        for sub in item :
            print(sub,end=" " )
    else :
        print(i)
    print()        
"""