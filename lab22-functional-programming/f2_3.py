# Arithematic operation using user defined functions
# Faster Execution
# change : in previous program we used user inputs each time for each tasks , in this program we tackel the program

#
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
    print()
    print(" First Enter numbers then choose required operation ! ")
    n1 = int(input("Enter num 1 : "))
    n2 = int(input("Enter num 2 : "))
    print(" 1. Multiplication \n 2. addition \n 3. Subtraction \n 4. Division \n 5. FloorDivision ")
    print(" 6. Remainder \n 8. Exit ")
    print()

    choice = int(input("Enter your choice : "))
     # using if-else conditions and decision making

    if choice == 1 :
        res = mul(n1,n2)
        print(f" ---->  Multiplication of {n1} and {n2} is : {res}")

    elif choice == 2 :
        res = add(n1,n2)
        print(f"---->  Addition of {n1} and {n2} is : {res}")
    elif choice == 3 :

        res = sub(n1,n2)
        print(f"---->  Subtraction of {n1} and {n2} is : {res}")

    elif choice == 4 :

        res = div(n1,n2)
        print(f" ----> Division of {n1} and {n2} is : {res}")

    elif choice == 5:

        res = floorDiv(n1,n2)
        print(f"---->  FloorDivision of {n1} and {n2} is : {res}")
    elif choice == 6 :

        res = rem(n1,n2)
        print(f"---->  Remainder of {n1} and {n2} is : {res}")

    else :
        print("---->  See you Soon !")
        break















