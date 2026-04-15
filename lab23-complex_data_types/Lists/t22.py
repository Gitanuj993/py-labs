# laxagraphical camparison

t1 = [10 , 20 , 30]
t2= [10 , 50 , 30]

print(f" t1 < t2 : { t1<t2}")
print(f" t1 > t2 : { t1>t2}")
print(f" t1 <= t2 : { t1<=t2}")

t1 = [10 , 50 , 30]
t2= [10 , 20 , 30]

print(f" t1 < t2 : { t1<t2}")
print(f" t1 > t2 : { t1>t2}")

t1 = [1 , 50 , 30]
t2= [10 , 20 , 30]
print(f" t1 > t2 : { t1>t2}") # False as 1 is not greater than 10

t1 = [10 , 5 , 100]  # t1 is greater than t2 becouse of 100
t2= [10 , 20 , 30]
print(f" t1 > t2 : { t1>t2}")  # Again False as Following

"""
t1 = [10 , 5 , 100]
t2= [10 , 20 , 30]

for t1 > t2 
 10 > 10 : Actually False but here it is taken as 10>= 10 : True
 5 > 20  : False 
 thus t1 is not greater than t2
 
"""








