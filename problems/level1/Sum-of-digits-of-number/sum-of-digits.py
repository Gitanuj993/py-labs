# Sum-of-digits-of-number
'''
Let's say if we have a number 12344 as an input
your task is to print the sum of all digits of the number

>> your output should be : 14

'''
print('Program to find the sum of all digits of a number !')
test1 = int(input(" Enter number : "))

# using for-loop
total_sum = 0
for i in str(test1) :
    
     total_sum += int(i)

print(f" Sum of all digits of the number is : {total_sum}")
