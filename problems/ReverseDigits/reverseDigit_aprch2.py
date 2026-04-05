# problem set : reverse digits 
# via shifting of digits 

n = int(input(' Enter number : '))

rev = 0

while n> 0 :
	digit = n % 10
	rev = rev *10 + digit
	n //=10 
	
print(f' reversed number is : {rev}')


"""
Aspects  !
complexity : ↓
readability : ↑


use of !
while -loop

explanation :
This  approach uses shifting of digitd

like if number is  1234 then
this approach looks like this
rev = rev *10 + (n%10)
rev = 0
0*10 + 4 = 4
4*10 + 3 = 43
43*10 + 2 = 432
432*10 + 1 = 4321

rev = 4321

"""

