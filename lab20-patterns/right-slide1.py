
n = 5
for i in range( 1, n+1) :
	for j in range(n-i) :
		print(" ",end=" ")
	for j in range(n-i,n,) :
		print("*", end = " ")
	print()
