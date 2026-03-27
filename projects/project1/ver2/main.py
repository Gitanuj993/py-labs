from qLib import questions

# number of questions

def percentage(score,total) :
 	per = ( score / total ) *100
 	return per

if __name__ == "__main__" :
	print("Welcome AT")
	score = 0 
	neg = 0 
	no_questions = int(input(" Enter no of questions : "))
	total_q = no_questions
	
	for q in questions :
		no_questions-=1
		if (no_questions == -1) :
			break
		print(q["question"])
		for option in q["options"] :
			print(option)
		user_choice = input("Enter your choice : ").upper()
		if ( user_choice == q["ans"]) :
			score+=1
		else :
			neg+=1
	
	print(f"You answered {score} correct and {neg} wrong answers out of {total_q} questions ")
	
	# pass and failed test cases 
	
	perc = percentage(score,total_q)
	if ( perc < 27 ) :
		print(" Score is too low !")
	elif ( perc >80 ) :
		print( " Excelent !")
		
	else :
		print(" Good Score ")






	
