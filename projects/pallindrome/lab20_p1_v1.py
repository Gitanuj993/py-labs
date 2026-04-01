# lab20_p1 :	pallindrome number 
"""
what are pallindrome numbers ?
those numbers which looks same and remain identicle if numbers is reversed. 
for eg. 121 , if we can reverse that number we can get 121 the number itself

// lets create a mini project which does the same things with nunbers and  strings or texts
"""

class Pallindrome  :
	def __init__(self) :
		print(" Welcome to the class of pallindrome world ! ")
		
		
	def check_num(self , num) :
		temp = num  # createing a temp variable to store reverse number of num		
		temp = str(temp) # using type cast temp to string type to use string slicing funciton
		num = str(num) # we type cast num from int to str  to compare it with reversed number 
		temp = temp[ : : -1] # reversing the number 
		if ( num == temp) :
			print( f" {num} is a Pallindrome number !")
		else :
			print( f" {num} is  Not a Pallindrome number !")
		
		return -1 		
		
	def check_str(self,string) :
		temp = string[ : : -1 ]
		if ( temp == string ) :
			print( f" {string} is a Pallindrome number !")
		else :
			print( f" {string} is  Not a Pallindrome number !")
					

if ( __name__ == "__main__") : # __main__  !=   __main__ , white space matters
	print(" Welcome AT ")
	obj1 = Pallindrome()
	while ( True) :		
		print(" choose from the follwing ! \n 1. number \n2. string or text \n 3. Exit ")
		choice = int(input("Enter your choice : "))
		if ( choice == 1) :
			num = int(input( " Enter number to check for pallindrome number :  "))
			obj1.check_num(num)
	
		elif ( choice == 2 ) :
			string1 = input( " Enter number to check for pallindrome number :  ")
			obj1.check_str(string1)
		
		else :
			print(f" Nice to see you ! ")
			break 
	
		
		
	
	

	
	
	

