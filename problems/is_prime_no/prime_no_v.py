
# program to check for prime numbers !

def check4prime() :
    n = int(input("Enter Number to check prime Number : "))
    for i in range(2, n):
        if (n % i == 0):
            print(f" {n} is not prime No ")
            break  # to stop the function when a divsor is found
    else:
        print(f" {n} is a prime number ! ")


if __name__ == "__main__" :
    check4prime()
















if __name__ == "__main__" : # main function like other programming languages
    print("Welcome AT ")