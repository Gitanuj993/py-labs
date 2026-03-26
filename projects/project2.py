"""
Welcome AT
Aim : To convert char to ascii code and vice-versa
"""
#from projects.project1 import user_input


def char2ascii_(char) : # what if we put more than one character in char
    ascii_code = ord(char)
    print(f" Code of character is {ascii_code}")

def ascii2char_(code) :
    char = chr(code)
    print(f" character of {code} is '{char}' ")

    # we should use decision making
    while True :
        print(" Choose Carefully \n 1. ascii to character \n 2. char to ascii ")
        user_input = int(input("Enter you choice : "))
        if ( user_input == 1) :
            input_code = int(input("Enter code to convert it into char : "))
            ascii2char_(input_code)

        elif ( user_input ==  2 ) :
            input_char = str(input("Enter char to convert it : "))
            char2ascii_(input_char)
        else :
            print(" Choose wisely !")
        user_input2=str(input("Do you want to continue (y/n) : "))
        if ( user_input2 == 'y' ):
             continue 
        else : break
