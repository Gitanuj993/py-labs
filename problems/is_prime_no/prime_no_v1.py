# program to check prime numbers

n = int(input(" Enter number to check prime Number : "))

for i in range (2,n) :
    if ( n % i == 0) :
        print(f" {n} is not prime No ")
        break # to stop the function when a divsor is found
else :
    print(f" {n} is a prime number ! ")