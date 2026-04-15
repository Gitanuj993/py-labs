# Aim is to reverse a string using indexes and
# we know that index starts from 0 to n - 1 , or -1 to -n

# lets take a string
test1 = "Welcome"
print(f" test1 is : {test1}")
# our task is to reverse it
store = ""
for i in test1 :
    print(i)
    store += i
print(f" store is : {store}") # program to copy a string

print('---------------------------------------')
# using negative indexing
store = ""
for i in range(-1, -(len(test1))-1,-1) :
    print(test1[i],end=" ")
    store+=test1[i]


print(f"\n store is : {store}") # program to copy a string
print('---------------------------------------')



