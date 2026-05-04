# Try to sort heterogeneous type of data in a list

t1 = [ 1 , 2 , "A"]
print(f" Sorted t1 : {sorted(t1)}")   # str > str  : allowed , str < int : not allowed ,
print(f" Sorted t2 : {sorted(t2)}") #