# program to take proper input of email.
# exception classes
class MailStartsWtihError(Exception) :
	def __init__(self) :
		super().__init__("Email do not startswith any number or any sybmol")
class EmailStructError(Exception) :
	def __init__(self) :
		super().__init__("Email can only contains alphabets , digits , ',' and '@' Symbol ")
class atSymbolError(Exception) :
	def __init__(self) :
		super().__init__("email can only contain only 1 '@' symbol  "  )
class atSymbolNotGiven(Exception) :
	def __init__(self) :
		super().__init__("email should contain '@' symbol "  )
class EmailNotHavingProperDomainName(Exception) :
		def __init__(self) :
			super().__init__("email should contain a proper domain name or Email provider's Name"  )
	
class EmailNotEndsWithDot(Exception) :
	def __init__(self) :
		super().__init__(" Email do not ends with '.' dot or period ")
		
class EmailNotHasNumsAfterSymbol(Exception) :
			def __init__(self) :
				super().__init__(" Email do not contain numbers after '@' symbol")
		
		
def set_user_email() :
	count = 0 
	while True :
		# email validation and error causing risky code in try block # based on priority
		try :
			#	take email  or email from the GET method, via API
			user_email = str(input("Enter email : ")).lower()
			len_user_email =   len(user_email)
			#   valid email checking.
			# if email starts with [ . , numbers , @ ]can't accepted
			# email can only contain @ symbol only one time
			count_at_symbol = 0
			
			# checking for valid sequences
			for i in user_email :
				if  i not in 'abcdefghijklmnopqrstuvwxyz.@0123456789' :
					raise EmailStructError
					
				# @ symbol validation
				if ( i in '@' ):
					# if @ comes more than 1 time then
					if count_at_symbol > 1 :
						raise  atSymbolError 
					count_at_symbol +=1
				
					
			# what if @ symbol not found in the email address provided
			if ( count_at_symbol != 1) :
					raise atSymbolNotGiven 
										
			# email do not starts with nums , . @ sign
			email_do_not_startswith = ['1','2','3','4','5','6','7','8','9', '.', '@' ]
			for i in email_do_not_startswith :
				if ( user_email.startswith(i)) :
					raise MailStartsWtihError 
					
				#     email do not contain numbers after @ sign . # this function would be removed if numbers accepted after @
				# if no domain_name or email name found after '@' symbol
				# to check proper domain name after @ symbol, to ensure domain name after @ symbol
		# email should have atleast 1 dot  or period after @ symbol						
				count_period = 0 #	to count number of periods after @ symbol
				
				str_valid_things_after_symbol = 'abcdefghijklmnopqrstuvwxyz.'
				for i in range(len_user_email) :
					if user_email[i] == '@' :
						for j in range(i+1,len_user_email) :
							if user_email[j] not in str_valid_things_after_symbol :
								raise EmailNotHasNumsAfterSymbol
							# to check for period sign
							if user_email[j] == '.' :
								count_period +=1
				
				# lets check for number of periods found after @ symbol , if not found  any raise an error
				if count_period == 0 :
								raise EmailNotHavingProperDomainName
								
				# email can't endswith '.'
				if user_email.endswith('.') :
							raise EmailNotEndsWithDot			
							# to ensure proper email 
					
					
					
		# Handling Errors without disrupting  normal control flow of program
		except EmailNotHavingProperDomainName as e :
			print(e)
		except EmailNotEndsWithDot as e :
			print(e)
		except atSymbolError as e :
			print(e)
		except       EmailNotHasNumsAfterSymbol as e :
			print( e)
		except atSymbolNotGiven as e :
			print(e)
		except EmailStructError as e: # handel if  email do  contain things other than alphabets, nums , . ,@ 
			print(e)
			
		except MailStartsWtihError as e :
			print(e)			
		except Exception as e:
			print("Enter correct email address",e)			
		else :
			print(" email is acceptable ") 
			break
	return user_email
			
			
if __name__ == '__main__' :
	user_email = set_user_email()
	print(" Your email is : ",user_email,sep = " ")
