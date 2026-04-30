t1 = [ 1 ,2,4,5]

revt1 = reversed(t1)

print(f" revt1 : {revt1}")
print(f" revt1 in list : {list(revt1)}")  # iterator is used

for i in list(revt1) : # Iterators can only be used once.
    print(i)