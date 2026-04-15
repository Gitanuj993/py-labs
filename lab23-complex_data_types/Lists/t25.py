# Error case


t1 = [ "AT",  1 , 123]
t2 = [  1  , "BT" , 123]

print(f" t1 : {t1}")
print(f" t2 : {t2}")


print(f" t1 < t2 : {t1 < t2}")  # we can't compare string with integers
print(f" t1 > t2 : { t1 > t2}")
print(f" t1 == t2 : {t1 == t2}")


# TypeError: '<' not supported between instances of 'str' and 'int'
# Compatible type