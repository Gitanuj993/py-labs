# program to check prime numbers

n = int(input(" Enter number to check prime Number : "))
if n == 0 or n == 1 :
    print(f" {n} is neither prime nor composite number")
else :
    for i in range (2,n) :
        if ( n % i == 0) :
            print(f" {n} is composite number ")
            break # to stop the function when a divsor is found
    else :
        print(f" {n} is a prime number ! ")