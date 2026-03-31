import random
arr = []
total_q = 2
# adding question into the list
while ( len(arr) < total_q) :
	num = random.randint(1,10)
	arr.append(num)
	arr = set(arr)
	arr = list(arr)

print(arr)
for r in arr :
    print(r)