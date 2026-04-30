#	map(f,x) functional programming use and use case :
	
	
list1 = [1,2,3,4,5,6]
print(list1)
list_squares = map( lambda x : x ** 2 , list1  ) 
# map return iterator
print(list_squares)
print(list(list_squares))
