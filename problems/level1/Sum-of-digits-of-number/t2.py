# program using for loop with indices and range function

print('Program to find the sum of all digits of a number !')
test1 = int(input(" Enter number : "))

# using for-loop with index
str_test1 = str(test1)
total_sum = 0
for i in range(len(str_test1)):
    total_sum += int(str_test1[i])

print(f" Sum of all digits of the number is : {total_sum}")