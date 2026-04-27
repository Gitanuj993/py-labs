"""
Welcome AT

Aim :	project to encrypt data provided by user


"""
def encrypt(text) :
	encoded = text.encode("utf-16")
	print("--> Encryption Successfull !\n")
	return encoded 

def decrypt(code) :
	decoded = code.decode("utf-16")
	print("--> Decryption Successfull!\n")
	return decoded

if __name__ == "__main__" :
	
	# declear variables		
	text = None
	code = None
	isdecoded = False
	isencoded = False
	
	while True :
		print(f"Enter your choice ! ")
		print(" 1. Encode \n 2. Decode \n 3. display the code \n 4.check \n 5. Exit  ")
		
		user_choice = int(input("Enter your choice : "))
		#make errror free input
										
		#encryption
		if (user_choice == 1) :
			if (text != None) :
				print("you already have data !\n")
			else :
				text= str(input("Enter data to encrypt :	"))
				code = encrypt(text)
				isencoded = True
		#decryption 
		elif ( user_choice ==2) :			
			print("case 2 \n")
			if ( code == None ) :
				print("encryption unable !\n")
			else :
				code = decrypt(code)
				isencoded = False
			
		# to display the code
		elif ( user_choice ==3) :
			if ( code == None) :
				print('Code is empty ,push data first\n')
			else :
				print(f" code is : [ {code} ]\n")
				
		#to check whether data is encoded or decoded
		elif  ( user_choice == 4 ) :			
			if ( isencoded == True) :
				print(" --->	code is encoded and not readable !\n")
			else :
				print(" ---> code is readable\n")
		
		#exit
		elif ( user_choice == 5) :
			print("Happy to see you there !")
			break
	 #invalid-case		
	 #else :
	  #  	print("Invalid entry !!!\n")
			
			
"""
 Error : empty
"""			
	
		

