
# program to check for prime numbers !

def check4prime() :
    n = int(input("Enter Number to check prime Number : "))
    if n == 0 or n == 1 :
        print(f" {n} is neither prime nor composite numbers !")
    else :
        for i in range(2, n):
            if (n % i == 0):
                print(f" {n} is composite Number ")
                break  # to stop the function when a divsor is found
        else:
            print(f" {n} is a prime number ! ")


if __name__ == "__main__" :
    check4prime()
















if __name__ == "__main__" : # main function like other programming languages
    print("Welcome AT ")