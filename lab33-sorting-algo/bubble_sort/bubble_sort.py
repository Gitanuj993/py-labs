# bubble sorting method is : 

	
test = []
for i in range(5) :
	num = int(input("Enter num : "))
	test.append(num)
print(" test is : " , test)
n = len(test)

for i in range(n-1) :
	
	for j in range(n-i-1) :
		if ( test[j] > test[ j + 1]) :
			temp = test[j]
			test[j ]=  test[j+1]
			test[j+1] = temp
print(" test is : " , test)
