

arr1 = [ 2,4,6,8]
arr2 = [ 12, 45 , 78, 90]

arr = arr2 + arr1
arr  = [ 1,2,3,4,5,6,67,78,90,99]
arr.sort()
#print(" ar r : ",arr)

len_arr = len(arr)
#print(" len : ", len_arr)
mid = ( len_arr // 2 ) - 1
#print(" mid : ",mid)
if len_arr % 2 == 0 :
	median = ( arr[mid] + arr[mid+1]) / 2
else :
	median= arr[mid]
	
	
print(" median is   : ",median)

# average is not related to median 
avg = 0
for i in arr :
	avg += i
average = avg / len_arr
print( " average : ",average)

# time complexity O(m+n)
