 # zip , consecutive elements of two objects in a complex data type
t1 = { 1, 2 ,3 ,4,5,6 } # mutable objects has same object
t2 = { 11,22,33,44,55,66}
print(f" t1 : {t1}")
print(f" t2 : {t2}")
print(f" zip of t1  and t2 : {set(zip(t1,t2))}")
print(f" zip of t2 and t1 is : { list(zip(t2,t1))}")