# observe the code
# variable length arguements

def show(* nums) :
    print(nums) # tuple  let's try to change them
    for i in nums :
        print(i , end = " ")
    
    
show(1,2,3,4,5,6,7)