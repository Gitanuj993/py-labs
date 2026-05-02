# insertion sort in python ! 

test = [11,5,7,23,3]
print(f"test is : " , test)
n = len(test)

for i in range(1,n) :
 	key = test[i]
 	j = i -1
 	while ( j >= 0 and key < test[j] ) : #	less than j
 		temp = test[j]
 		test[j] = test[j+1] 
 		test[ j+1 ] = temp
 		j -= 1
 	test[j + 1] = key
 	
print(f"test is : " , test) 	
 	


