# to count prime numbers upto n range
# improved version of chatGpt provided solution
def is_prime(n) :

    #lets assume all the number are prime numbers , then we eliminate non prime numbers
    # let's create a list which containes a boolean data type to store a number is prime or not
    #initially all numbers are assumed a prime numbers , in which zero is also considered

    list_prime = [True] * (n+1) # n+1 becouse 0 is also included , as indexing start from the zero
    # above statement will create a list containing True values
    # print(list_prime)

    # lets False the values of 0 and 1 as they are not prime not composite numbers
    list_prime[0] = list_prime[1] = False

    # Now we can eliminate prime_numbers , we can eliminate multiple of numbers upto √n
    # why upto √n becouse within this range all the numbers can divide all the numbers upto √n
    # simplt from range 2 to √n+1 is sufficient. √n should be int or floor type
    for i in range(2,int(n ** 0.5) + 1) :
        # now eliminate Non prime numbers
        if  list_prime[i] == True :
            for j in range ( i * i , n + 1 , i) : # range to eliminate multiple of i
                # False if number is Non prime number
                list_prime[j] = False
    total_prime_no = sum(list_prime)
    total_composite_no = n - total_prime_no - 1
    print(f"Total Number of prime numbers within range of {n} is : {total_prime_no}")
    print(f"Total number of composite numbers within range is : {total_composite_no}")
    # print(list_prime)






if __name__ == "__main__" :
    uptoN = int(input(" Enter range upto n : "))
    is_prime(uptoN)

