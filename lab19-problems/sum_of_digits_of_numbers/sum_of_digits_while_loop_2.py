
# taking a number and printing sum of its digits : 
# take given number or take run time input
number = 12345
# storing it in another variable for operation , if we need the orignal one for another use case
temp = number + 0
#taking a variale to store sum of all the digits of the number
#sum = 0 # avoid using it, as python has a built in functions sum , we are casually overwriting one.
total = 0
# performing an repetition task of extracting digts add it into total and remove the last digit
while temp != 0 :
	# extracting digit
	digit = temp % 10
	#	adding digit into the total
	total += digit
	# removing last digit to continue the process
	temp //= 10	

print(" sum of all the number of ",number," is :	" , total)
