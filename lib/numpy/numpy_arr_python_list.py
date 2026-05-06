import numpy as np

# creating numpy array ,  extension of c for python

arr = np.array([1,2,3,4,5])
print("numpy arr  : ", arr) #	numpy array's elements are not seperated by elements, as they are stored in contigeous memory locations.'
print(" type of  numpy array :: ", type(arr))
list_arr = [1,2,3,4,5]
print(" list arr : ", list_arr)  #	python lists are seperated by comma, and are not stored in contiginous memory locations , list stores the reference of element objects.
print("Type of python list : ", type(list_arr))
