# enumerate() function

var1 = [ 10 , 30 , 20 , 50 ]
iter_var1 = enumerate(var1)

print(f" var : {var1}")
print(f" address of iterator : { iter_var1}")
print(f" Values in the iterator : {list(iter_var1)}")
print(f" values in the iterator : {tuple(iter_var1)}") # empty tuple # iterator already run
print(f" values in the tupel : {tuple(enumerate(var1))}") # tuple of tuple



