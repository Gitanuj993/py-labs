# any () function , return true if any value is true in a sequence
"""
Truthy values :
1. All non zero numbers
2. non empty lists


False Values !
1. 0
2. 0.0
3. " "
4. None

"""
t1 = [1,2,3,4]

print(f" t1 : {t1}")
print(f" any(t1) : {any(t1)}")
print(f" all(t1) : {all(t1)}")

print("============================")
t1 = [1,2,3,4,0] #
print(f" t1 : {t1}")
print(f" any(t1) : {any(t1)}")
print(f" all(t1) : {all(t1)}")

print("============================")

