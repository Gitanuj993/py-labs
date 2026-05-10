class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False
        print(" original value is : ",x)
        if x < 0 :
            isNeg = True
            x = -x
        rev = 0
        org = x + 0
        print("Original value : ",x)
        while ( x != 0) :
            digit = x % 10
            print("digit : ", digit)
            rev = rev * 10 + digit
            x = x // 10 

        if isNeg :
            return -rev
        else :
            return rev
            
###
if __name__ == '__main__' :
	s = Solution()
	x = int(input("Enter number : i"))
	res = s.reverse(x)        
	print(res)
