# Arithematic operation using user defined functions

def mul(a,b) : # : is identation which defines the scope of code or area of code block
    return a*b # returning value as we can call values for operations then we can also return processed output

def add(a,b) :
    return a + b

def sub(a,b) :
    return a - b

def div(a,b) :
    return a/b

def floorDiv(a,b) :
    return a//b

def rem(a,b) :
    return a % b

while True :
    print(" 1. Multiplication \n 2. addition \n 3. Subtraction \n 4. Division \n 5. FloorDivision ")
    print(" 6. Remainder \n 8. Exit ")
    print()

    choice = int(input("Enter your choice : "))
     # using if-else conditions and decision making

    if choice == 1 :
        n1 = int(input("Enter num 1 : "))
        n2 = int(input("Enter num 2 : "))

        print(f" Multiplication of {n1} and {n2} is : {mul(n1,n2)}")

    elif choice == 2 :
        n1 = int(input("Enter num 1 : "))
        n2 = int(input("Enter num 2 : "))
        print(f" Addition of {n1} and {n2} is : {add(n1,n2)}")
    elif choice == 3 :
        n1 = int(input("Enter num 1 : "))
        n2 = int(input("Enter num 2 : "))
        print(f" Subtraction of {n1} and {n2} is : {sub(n1,n2)}")

    elif choice == 4 :
        n1 = int(input("Enter num 1 : "))
        n2 = int(input("Enter num 2 : "))
        print(f" Division of {n1} and {n2} is : {div(n1,n2)}")

    elif choice == 5:
        n1 = int(input("Enter num 1 : "))
        n2 = int(input("Enter num 2 : "))
        print(f" FloorDivision of {n1} and {n2} is : {floorDiv(n1,n2)}")
    elif choice == 6 :
        n1 = int(input("Enter num 1 : "))
        n2 = int(input("Enter num 2 : "))
        print(f" Remainder of {n1} and {n2} is : {rem(n1,n2)}")

    else :
        print(" See you Soon !")
        break















