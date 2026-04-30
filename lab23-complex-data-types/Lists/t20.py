test = [[[70, 80, 90] ,10, 20,[70, 80, 90], 30], [40, 50, 60], ]

# let print 80
print(len(test)) # 2
print(test[0])
print(test[0][0])
print(test[0][0][0])
# print(test[0][0][0][0]) # TypeError: 'int' object is not subscriptable

print()
print(f" list is : {test}")
# print 40
print(test[1][0]) # done


# lets print len of each list inside list

print()
print(f" list is : {test}")

print(f" len of whole list test  : {len(test)}")
# print(f"")


