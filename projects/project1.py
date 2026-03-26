"""
Welcome AT
aim : To create a quize plateform and play some quizes
dependency :
theory : list , dict
workflow :
what is happening ?
"""
questions= [
    {
    "question" : " Which one of programming language use interpreter ?",
    "options" : [" A. python " , " B. C lang" , " C++ lang" , " java " ],
    "ans" : "A"
    }, #1st
    {
        "question" : "Which language is used for data analysis ?",
        "options" : [" A. python " , " B. C lang" , " C++ lang" , " java " ],
        "ans" : "A"
    }
        ]
score = 0
negative = 0

for q in questions :
    print(f"\n {q["question"]}")
    for option in q["options"] :
        print(f"{option}")
    user_input = str(input("Enter your answer : ")).upper()
    if ( user_input == q["ans"]) :
        score+= 1
    else:
        negative+= 1

print(f" Final result is  {score} \n you gave {score} right answers and {negative} answered wrong" )


