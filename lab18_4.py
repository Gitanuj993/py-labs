# operators in the python are the special symbols which perform meaningful operations
"""
# logical operators , those opertors used in decison  making and to define inclusive and exclusive range.

logical operators are :	and , or , not
in which and specify  both condition should true like i
asked you what do you want a number greter than 2 and a number greater than 4 , if you choose 3 then number 3 is greater than 2 but not greater than 4 thus conditon become False 
and 
if conditon looks like this x is greter than 2 or x is greter than 4 , if number choosen is 3 then conditon become True as 
or logical operator gives True if atleast one of the conditon is True then conditon becomes True
if and is used then if atleast any case become False then whole case becomes False 
"""
# a game based on logical opertores


while (True):
	num = int(input("Enter number :	"))
	if (num < 0) :
		print(f" num is less than 0 ")
	
	elif ( num >= 1 and num <=10) :
		print(f" {num} is greter than 1 and less than 10")
		
	elif ( num >10 or num <=20 ) :
		print(f" Num is either greater than 10 or either less than 20")

	elif ( not (num <20)) :
		print(f"{num} is greater than 20") 
	
	else :
		print(f"you are out standing")











