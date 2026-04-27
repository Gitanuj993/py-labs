# finding median of a sorted array !

list = [ 1,2,3,4,7,8,67,78,90,99,100] 

i = 0
j = len(list) -1 
count = 0
print("i is : ",i)
print(" j is : ",j)

while ( ( j >i )) :
	count +=1
	i = i + 1
	j = j - 1
	print("i is : ",i)
	print(" j is : ",j)
	
print("="*45)
print("i is : ",i)
print(" j is : ",j)
if i == j :
	print(" odd case median is : ",list[i])
else :
	median = ( list[i] + list[j]) / 2
	print(" even case median is :	" , median)
	
	
