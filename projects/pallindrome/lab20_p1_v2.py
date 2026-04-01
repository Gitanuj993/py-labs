# lab20_p1_v2 :	pallindrome number into a single number
"""
what are pallindrome numbers ?
those numbers which looks same and remain identicle if numbers is reversed. 
for eg. 121 , if we can reverse that number we can get 121 the number itself

// lets create a mini project which does the same things with nunbers and  strings or texts
"""

class Pallindrome  :
	def __init__(self) :
		print(" Welcome to the class of pallindrome world ! ")
		
		
	def check_plndrm(self,string) :
		temp = string[ : : -1 ]
		if ( temp == string ) :
			print( f" {string} is a Pallindrome number !")
		else :
			print( f" {string} is  Not a Pallindrome number !")
					

if ( __name__ == "__main__") : # __main__  !=   __main__ , white space matters
	print(" Welcome AT ")
	obj1 = Pallindrome()
	while ( True) :													
			print(" press 6 To exit the program !")																
			string1 = input( " –-----> Enter value to check for pallindrome  :  ")
			if (string1 == '6') :
				print("Thanks for using our functions")
				break
			obj1.check_plndrm(string1)
		
	