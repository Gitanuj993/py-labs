
# list inside list
# while loop : we can also access elements of a list using indices

l1 = [ 10 , 20 , 30 ]
l2 = [ 40 , 50 , 60 ]
l3 = [ 70 , 80 , 90 ]
l4 = [ 10 , 20 , 30 ]

test1 = [l1 , l2 , l3 ]

print(test1)

print(" print --------------------------\n")

i = 0
while i < len(test1) :
    print(test1[i][i])
    i = i + 1
