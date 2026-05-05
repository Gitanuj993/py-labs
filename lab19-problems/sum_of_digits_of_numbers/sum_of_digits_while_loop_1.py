
# taking a number and printing sum of its digits : 

num = 12345
sum = 0
while num // 10 != 0 :
	digit = num % 10
	sum += digit
	print(digit)
	num //= 10
	print(num)
# patch for logic
sum = sum + num

print(" sum of all the number of ",num ," is :	" , sum)
