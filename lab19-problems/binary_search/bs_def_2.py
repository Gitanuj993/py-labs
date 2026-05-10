
nums = [ 1,2,3,4,5,14,16,19,45,78,90]
target =  90
def binary_search(low,high) :	
	print("low : " , low)
	print(" high : " , high)
	mid =(  high + low  ) //2 	
	if nums[mid] == target :
		return mid
	if low == high :
		return -1		
	if nums[mid] > target :
		return binary_search(low, high - 1)# logical bug
	else :
		return binary_search(mid + 1, high)				
res = binary_search(0,len(nums)-1)
print(" res is :	" , res)
	

