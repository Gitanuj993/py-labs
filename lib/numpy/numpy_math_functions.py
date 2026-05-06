import numpy as np
#	mathematical functions of numpy : numpy is powerfull library backed by c programming language.

"""
# Arithematic functions.
np.sum(numpy_arr1,numpy_arr2)
np.multiply(numpy_arr1,numpy_arr2)
np.divide(numpy_arr1,numpy_arr2)
np.subtract(numpy_arr1,numpy_arr2)
np.pow(numpy_arr1,numpy_arr2)
np.mod(numpy_arr1,numpy_arr2)
"""
numpy_arr1 = np.array([10,20,30,40,50,60])
#numpy_arr2 = 5
#numpy_arr2 = np.array(())
#numpy_arr2 = np.array((5,)) # only int scalar can be converted to scalar index
#numpy_arr2 = np.array(5) #	out of axis bound error
# numpy_arr2 = np.array([5]) # only integer scalare
#print(type(arr_2))

# numpy broadcasting.
res_add = numpy_arr1 + 5
# numpy mathematical functions.

arr_1 = np.array([2,4,6,8])
arr_2 = np.array([1,2,3,4])
# print numpy arrays.
print(" arr_1 : " , arr_1 )
print(" arr_2 : " , arr_2 )


res_add = np.add([1,2,3],[1,2,3])
res_multiply= np.multiply(arr_1 , arr_2)
res_divide = np.divide(arr_1 , arr_2)
res_subtract = np.subtract(arr_1 , arr_2)
res_pow = np.pow(arr_1 , arr_2)
res_mod = np.mod(arr_1 , arr_2)

print("sum is :	", res_add)
print(" muliply is :	", res_multiply)
print(" divide is : " , res_divide)
print(" subtract is :	" , res_subtract)
print(" power is :	" , res_pow)
print(" modulous is :	" , res_mod)

# Now same thing using operators . 
print("\n same things using operators  arr_1 and arr_2  \n ")
print( " sum is :	" , arr_1 + arr_2)
print( " subtract is :	" , arr_1 - arr_2)
print( " multiplication  is :	" , arr_1 *  arr_2)
print( " divide  is :	" , arr_1 / arr_2)
print( " power  :	" , arr_1 ** arr_2)
print( " mod  is :	" , arr_1 %  arr_2)

print("\n")


numpy_arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("numpy_arr is : " , numpy_arr)
print(" square of all the elements of the numpy arr is : ")
print( numpy_arr + 0 )



