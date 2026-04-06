# python program to find total number of prime numbers  and print!
# error !!!
# we will go back to this code soon
prime_no_list = []
composite_no_list = []
n = int(input(" Enter range upto : "))

for i in range(2,n) :
    for j in range(2,i) :
        if ( i % j == 0 ) :
            composite_no_list.append(i)
        # elif ( i % j != 0) :
        # else :  #wrong
        #     prime_no_list.append(i)


print(f" total number of prime no is : {len(prime_no_list)}")
for i in prime_no_list :
    print(i)

print(f" total number of composite_no  is : {len(composite_no_list)}")
for i in composite_no_list :
    print(i)