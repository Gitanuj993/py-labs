# slide pattern
"""
*
* *
* * *
* * * *
"""
p = "*"
n = 10
for i in range (n) :
    for j in range (i) :
        print(p , end = "  ")
    print()
