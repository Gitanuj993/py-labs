# ends with startswith




test1 = "     AT    "
res1 = test1.split()
res2 = test1.strip()
res3 = test1.lstrip()
res4 = test1.rstrip()

print(f" test 1 is : {test1} and its length is :{len(test1)}")
print(f" split() : {res1} and its length is :{len(res1)}") # default argument is " " space return in list format
print(f" lstrip() : { res3} and its length is :{len(res3)}") # return in new string
print(f" rstrip() : { res4} and its length is :{len(res4)}") # return in new string ,
print(f" strip() : { res2} and its length is :{len(res2)}") # return in new string

print(" #### True False")

test1 = "hello"
test2 = "Engineer"
res1 = test1.startswith("h") # three parameters
# res2 =
print(f" is test1 : {test1} startswith H : {res1}")