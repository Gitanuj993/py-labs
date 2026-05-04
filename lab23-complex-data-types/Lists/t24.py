#  string in list and laxagraphic comparison operators

t1 = [  1, "AT" , 123]
t2 = [  1, "AT" , 123]

print(f" t1 : {t1}")
print(f" t2 : {t2}")

print(f" t1 < t2 : {t1 < t2}")
print(f" t1 > t2 : { t1 > t2}")
print(f" t1 == t2 : {t1 == t2}")

print("--------------------------------------")

t1 = [  1, "AT" , 123]
t2 = [  1, "BT" , 123]

print(f" t1 : {t1}")
print(f" t2 : {t2}")

print(f" t1 < t2 : {t1 < t2}") # True
print(f" t1 > t2 : { t1 > t2}") # False
print(f" t1 == t2 : {t1 == t2}") # False

print("--------------------------------------")
print("--------------------------------------")
# # Error case :
# t1 = [ "AT",  1 , 123]
# t2 = [  1  , "BT" , 123]
#
# print(f" t1 : {t1}")
# print(f" t2 : {t2}")
#
# print(f" t1 < t2 : {t1 < t2}") # True
# print(f" t1 > t2 : { t1 > t2}") # False
# print(f" t1 == t2 : {t1 == t2}") # False

