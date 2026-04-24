# Down Slide
"""
*  *  *  *  *
*  *  *  *
*  *  *
* *
*
"""
symbol = "*"
rangeN = 5

for i in range (rangeN,0,-1) :
    for j in range(i) :
        print(symbol,end = "    ")
    print()

