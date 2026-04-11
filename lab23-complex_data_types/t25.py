
# count : count the concerned element in simple data type
# find : return first occurance index of concerned element

# variable
logic = "Machine Learning"

# result 1
res = logic.count('a')
# result 2
res2 = logic.count('b',1,34)
# print result 1
print(res)
print(f" number if occurance of 'b' is : {res2}")

# find
find_a = logic.find('a')

print(f" 'a' is found at index : {find_a}")

find_a_res2 = logic.find('c',2,10)
print(f" 'c' is found at index : {find_a_res2} in \"{logic}\"")

# " \" Machine Learning \"  "
# /' , \" are escape sequence

test1 = "Welcome AT"
search = "come"
res_find_search = test1.find(search)
print(f" {search} found at : {res_find_search} in {test1}")

tofind = "new"
res_find_search1 = test1.find(tofind,-1)
print(f" {tofind} found at : {res_find_search1} in {test1}") #
# find  will return -1 if no value is found as "new" is not found in "machine Learning"



