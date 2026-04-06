# Python program to find the total number of prime and composite number upto n numbers .

n = int(input("Enter range upto n : "))
# counter to count prime_numbers
count_prime = 0
#counter to count composite numbers
count_composite = 0
for i in range(1,n+1) :
    count = 0
    for j in range(1,i+1) :
        if ( i % j == 0) :
            count+=1
    if ( count > 2 ) :
        count_composite+=1
    else :
        count_prime += 1


print(f" total number if prime numbers is : {count_prime}")
print(f" total number if composite numbers is : {count_composite}")
