# List comparison , list compared to another list
# == Equality
# != Not Equality

test1  = [ 12,34,56]
test2 = [ 12 ,34 , 56]
test3 = [1,3,4 ]

ist1t2 = test1 == test2
ist1t3 = test1 == test3
ist_not_1t3 = test1 != test3
print(f" is test1 == test 2 : {ist1t2}")
print(f" is test1 == test 3 : {ist1t3}")
print(f" is test1 != test 2 : {ist_not_1t3}")


