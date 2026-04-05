# function to reverse a num
def length(num) :
	len = 0
	while  ( num // 10 != 0 ) :
		
		len+=1
		num//=10
	len+=1
	return len

# lets take input from the  user
n = int(input(' Enter num : '))
# variable declearation for  reversed number 
rev = 0
# length of num or total number of digits in a num
len = length(n)
#temporary variable to perform operations
temp = n
l = len
# logic 
while ( temp//10 != 0) :
	# decreasing length by 1
	l = l -1
	#logic 
	rev += (temp%10) * (10**l)
	
	# lets reverese others digits
	temp//=10
	
	#edge conditions if l == 1
	if ( l ==1) :
		rev +=  temp
	
	
	
print(f" Reversed digits is : { rev } ")


"""
Aspects  !
complexity : ↑
readabilitu : ↓


use of ! 
while -loop
created length function
patch case 


explanation : 
This  approach uses manual shifting 

like if number is  1234 then 
this approach looks like this 
rev = rev + (n%10) * (10**(l-1))
4000+300+20+1 =  4321


"""
