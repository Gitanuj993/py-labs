t1 = [ 1 ,2,4,5]

revt1 = reversed(t1)

print(f" revt1 : {revt1}")
for i in list(revt1) : # Iterators can only be used once.
    print(i)

print(f" reversed : {list(revt1)}") # empty list