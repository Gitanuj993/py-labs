# sliding window approach to solve problems.
# find max subarray of length 3 from the array = [ 1,2,3,11,22,33,5,6,7,88,99,39]
arr = [ 1,2,3,11,22,33,5,6,7,88,99,39]
print(arr)
# set   max = 0
max = 0
# windows size
w = 3
n = len(arr)
# finding windows 
for i in range(w) :
	max += arr[i]
# storin maximum sum of subarray
max_subarray = max	

# now shifting window
for i in range( 1 , n - w + 1 ) :
	max =  max + arr[i+w-1] - arr[i-1]
		
	if  max > max_subarray :
		max_subarray = max
		
		
print("max array is :	" , max_subarray)

