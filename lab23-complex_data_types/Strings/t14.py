#

var = "Programmer"
strLength = len(var)
i = 0
print( " see ---> [ " , end= " ")

while i < strLength :
    print(i, end=" ")
    i +=1
print("]")

print( " see ---> [ " , end= "")

j  = 0
while j < strLength :
    print(var[j], end="")
    j +=1
print(" ]")

print( " see ---> [ " , end= " ")
j  = 0
while j < strLength :
    print(var[j], end=" ")
    j +=1
print("]")