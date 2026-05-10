class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False
    
        if x < 0 :
            isNeg = True
            x = -x
        rev = 0
        org = x + 0

        while ( x != 0) :
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10
            
        if rev > (2**31 -1) :
        	return 0 

        if isNeg :
            return -rev
        else :
            return rev
            
###
if __name__ == '__main__' :
	s = Solution()
	x = int(input("Enter number : "))
	res = s.reverse(x)        
	print(res)
