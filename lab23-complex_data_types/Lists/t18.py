# Indexing in lists

test = [ 10 , 20 , 30 , 40 , 50 ]

print(test)

print(test[0])
print(test[-1])
# print(test[5]) # Index Error : list index out of range !
print(test[-5])
# print(test[-6]) # Index Error : list index out of range !

# see code-line 9 and 11 , you wiil see , [5] is not valid , [-5 ] is valid
# thus list[len()] is not valid , list[-len(list)]