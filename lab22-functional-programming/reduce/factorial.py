# new class variables names ....
from functools import reduce 

test = [ 1 ,2,3,4,5]
print(test)
result  = reduce ( lambda x,y : x + y , test)
print(result)
factorial = reduce ( lambda x,y : x*y , test)
print(factorial)
