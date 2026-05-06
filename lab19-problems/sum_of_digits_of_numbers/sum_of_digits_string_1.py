# sum of digits using string . 

def sum_of_digits(num) :
	total = 0 
	for i in str(num) :
		total = total + int(i)
	return total

		
if __name__ == '__main__' :
		print("Welcome to the program to sum of digits of numbers")
		while True :
			try :
				num = int(input("Enter your  number :	")) 						
			except Exception as e :
				print(e)
				print(" your attempt failed , try again !")		
			else :
				print(sum_of_digits(num))	
				print( " See you next time ")
				break
			finally :
				pass
	

