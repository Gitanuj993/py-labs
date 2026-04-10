#to count prime numbers upto n range
# improved version of chatGpt provided solution
def is_prime(n) :

    #lets assume all the number are prime numbers , t>
    # let's create a list which containes a boolean d>
    #initially all numbers are assumed a prime number>

    list_prime = [True] * (n+1) # n+1 becouse 0 is al>
    # above statement will create a list containing T>
    # print(list_prime)

    # lets False the values of 0 and 1 as they are no>
    list_prime[0] = list_prime[1] = False

    # Now we can eliminate prime_numbers , we can eli>
    # why upto √n becouse within this range all the n>
    # simplt from range 2 to √n+1 is sufficient. √n s>
    for i in range(2,int(n ** 0.5) + 1) :
        # now eliminate Non prime numbers
        if  list_prime[i] == True :
            for j in range ( i * i , n + 1 , i) : # r>
                # False if number is Non prime number
                list_prime[j] = False
    total_prime_no = sum(list_prime)
    total_composite_no = n - total_prime_no - 1
    print(f"Total Number of prime numbers within range is : { total_prime_no } ")
    print(f"Total number of composite numbers within range is : { total_composite_no} ")
    # print(list_prime)
    
    print()
    print(" prime Numbers → [ ",end=" ")
    for i in range(2,n+1) :
    	if list_prime[i] :
    		print(i,end=" ")
    print(' ] ')
    
    print()
    print(" Composite Numbers → [ ",end=" ")
    for i in range(2,n+1) :
    	if list_prime[i] == False:
    		print(i,end=" ")
    print(' ] ')
    




if __name__ == "__main__" :
     uptoN = int(input(" Enter range upto n : "))
     is_prime(uptoN)
    
    
    
