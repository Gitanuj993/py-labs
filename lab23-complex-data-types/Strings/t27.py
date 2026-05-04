# replace function in python

test1 = " one two one one one one one"
res1 = test1.replace("one","two")

print(f" {test1} when one is replaced by two is : {res1}")
res2 = res1.replace("two","one")
# now print test 1
print(f" Test 1 is : {test1}")
print(f" res1 is : {res1}")
print(f" res2 is : {res2}")