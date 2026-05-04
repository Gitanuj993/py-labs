# filter(x,y)

test = [ 1,2,3,4,5,6]
print(test)
result1 = list ( filter ( lambda i : i % 2 == 0 , test))
print(result1)
result2 = list ( filter ( lambda i : i % 2 != 0 , test ))
print(result2)
