s = input("Enter string: ")

left = 0
max_len = 0
window = set()

for right in range(len(s)):
    print("right is : ",right)
    while s[right] in window :                
        print("left is :	",left)
        print(" window is : " , window , end="")
        print(" removed element is : " , s[left])
        window.remove(s[left])
        print("after remove : " , window)
        
        left += 1        
        print("left : ",left)

    window.add(s[right])	
    print(" element added :	",s[right])
    max_len = max(max_len, right - left + 1)
    print(" max len : ", max_len)
    print(" set is : " ,window)

print("Maximum length:", max_len)
