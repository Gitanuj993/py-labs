class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        def binary_search(low,high) :
            mid = ( low + high ) // 2
            if nums[mid] == target :
                return mid
            # base case
            if low == high :
                return -1

            # recursive call
            if nums[mid] > target :
                return binary_search( low , mid -1)
            else :
                return binary_search(mid+1,high)
        return binary_search(0,len(nums)-1)               
s = Solution()
num = [1,2,3,4,5]    
target = 1
res = s.search(num,target)
print(" : ", res)        
