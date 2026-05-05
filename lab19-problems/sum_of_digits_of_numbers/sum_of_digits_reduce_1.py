# sum of digits using sum function after convering numbers into strings. using lambda function
from functools import reduce
def sum_of_digits(num) :
	total = reduce( lambda x , y : int(x) + int(y) , str(num) )
	return total 	

	
	
if __name__ == "__main__" :
	print(" Welcome to the program of calculating sum of  digits of any number")
	while True :
	try :
		number = int(input("Enter your number : ")
		total = sum_of_digits(number)
	except Exception as e :
		print(e,"Try again ! ")
	else :
		print(" sum of digits of number ", number , " is : ",total)
		break
