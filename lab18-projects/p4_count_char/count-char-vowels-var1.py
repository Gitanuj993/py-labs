# program to count vowels , consonants , spaces and special symbols

def count_char(var) :
	no_vowels = no_consonants = no_numbers =  no_symbols = no_spaces = 0	
	for i in var :
		if ( i in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz") :
			no_consonants += 1 				
		elif ( i in "AEIOUaeiou") :
			no_vowels +=1
		elif ( i in "0123456789") :
			no_numbers+=1
		elif  i == " " :
			no_spaces +=1
		else :
			no_symbols +=1
			
	print(f" Number of vowels are : {no_vowels } ")
	print(f" Number of consonants are : {no_consonants } ")
	print(f" Number of numbers : {no_numbers } ")	
	print(f" Number of symbols are : {no_symbols } ")		
	print(f" Number of spaces  are : {no_spaces } ")	


if __name__ == "__main__" : # Default main functions in python
	test = input("Enter text :	") 
	count_char(test) 
