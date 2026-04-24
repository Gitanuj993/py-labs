# to find the total number of prime and composite number by previous

n = int(input(" Enter range : "))

prime = []
composite = []

for i in range(1,n+1) :
    if i == 1 :
        continue
    count = 0
    for j in range(1,i+1) :
        if ( i % j == 0 ) :
            count+=1
    if ( count > 2) :
        composite.append(i)
    else :
        prime.append(i)
else :
    print("\t All things works fine \t")
print(f" Total number of prime numbers upto {n} is : {len(prime)} [",end=" ")
for i in prime :
    print(i, end = " ")
print("]\n")
print(f" Total number of composite numbers upto {n} is : {len(composite)} [",end = " ")
for i in composite :
    print(i, end = " ")
print("]\n")
