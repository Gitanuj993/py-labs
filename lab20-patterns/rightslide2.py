# right al8gned pyramid

n = 5
temp = n -1 # index value
for i in range(n) :
	for j in range(n) : 
		 if ( j >=  temp) :
		 	print("*",end = " ")
		 else :
		 	print(" ",end = " ")
	temp -=1
	print()
