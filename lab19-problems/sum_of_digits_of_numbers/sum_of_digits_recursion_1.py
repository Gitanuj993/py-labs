# finding sum of all the digits of a number using recursion

def sum_of_digits(number) :
	if number == 0 :
		return 0
		
	digit = number % 10
	number //= 10
	return sum_of_digits(number) + digit
	
	
	
if __name__ == '__main__' :
	number = 12345
	total = sum_of_digits(number)
	print(" addition of all the digits of number ", number , " is :	", total)
