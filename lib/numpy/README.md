# Numpy 
<h3> Numpy is a powerful library which works on  numbers or numberic values.
unlike python lists , NumPy uses Homogenous data strucure , and implement arrays. </h3>

1. NumPy uses vectorization, works on whole array at once.
2. continues memory locations. more memory efficient.
3. no loops required to perform operations.
4. fast mathematical operations unlike python lists.
5. automatic math operations unlike python lists manual operations.
6. NumPy is core library on which other libraries are depends on

### Why NumPy over python Lists
1. NumPy used vectorization.
2. list used slow interpreted loops.
3. python lists occupy more memory.
4. NumPy arrays are more memory efficient.
5. NumPy is faster because NumPy is written in c language.
6. NumPy A C-backed numerical engine that lets Python pretend it’s fast. 
7. Python alone = slow loops
NumPy = vectorized operations executed in optimized C



### Some libraries which works on top of NumPy 
1. Pandas
2. Matplot lib
3. SckitLearn
4. Pytorch
5. OpenCV
6. TensorFlow

### used in 
1. Data Science
2. Image processing
3. Simulation
4. Finance
5. AI/Ml

### Install NumPy in IDE 

1. using pip : `` pip install numpy`` in Code Editor's Terminal.


### 
1. 0D array : scalar arr
    - eg. a = 23
2. 1D array : vector
    - eg. [ 1,2,3,4 ]
    - Collection 0D arrays
3. 2D array : Matrix representation or table
    - collection of 1D arrays in list of list type.
    - eg. [ [1,2,3] , [4,5,6] ]
#### Tensor , ndarray , n dimensional array , dimension greater than 3
4. 3D array : collection of 2D array ,
    -  eg. [ [ [1,2,3], [4,5,6 ] ] ]
5. 4D array collection of 3D arrays
    - Collection of 3 D arrays.

### Shapes 
1. a = np.ones((1))
- 1D array containig only 1 element.
- also means 1 row, 1 coloumn, we can think of it, not actually it is.
2. a = np.shaoe((10))
- 1D array containing 10 elements.
- also means 1 row 10 columns nit actuallly
3. a = np.ones((2,3)
- 2D array containing 2 rows 3 coloumn.
- 
4. a = np.ones((1,2,3))
- 3D array containing 1 2D array which has two rows and 3 coloumns

5. a = np.ones((2,3,4))
- 3D array containing 2 2D arrays
- each 2D array has 3 rows and 4 coloumns.


6. Shapes are the metadat or data about the arrays.



1. import numpy
2. a = np.array([1,2,3,4])
np.array is an method to create numpy array.

#### properties or attributes  of numpy array
a = np.array([1,2,3,4])
- These are stored information not functions.
1. a.ndim
- tells number kd dimensions
2. a.shape
- tells the shape of array.
3. a.size
- tell size of the array
4. a.dtype
- tells tyoe of the stored data , as numpy array stores only homogenious data
5. wants to look whole atributes see, dir(a)

a.dtype → type of elements
a.itemsize → bytes per element
a.nbytes → total memory used

a.base → original array (if it's a view)

Real/Imaginary (for complex numbers)
a.real
a.imag
Transpose shortcut
a.T


Slightly advanced (rare but powerful)
a.flat → iterator over array
a.ctypes → low-level C interface
a.__array_interface__ → internal structure





# in numpy we can also specifiy or take multiple elements using more than one index .

like if we had to take various elements
a = [ 1,2,3,4]
res = a[1] # done
res = a[[0,2,3]] # not possible in python lists
but possible in numpy.

a = np.array([1,2,3,4,5])
res = a[1]
res = a[[1,3,2]]

boolean indexing lets us filter elements in numpy array. based on condition. instead of indices like 0,1
we can use boolean array which contains True and False to pick the values.


a = np.array([1,2,3,4,5])
res = a > 2 , it will return a boolean list contaning True and false.
result will return an numpy array of type boolean on which True and False are contained based on the condition. ,boolean indexing.

arr = np.array([1,2,3,4,5])
res = arr[arr>=2] # it wil return actual output.
it will return all the elements which satisfy the condition.
or it stores only True values of simple conditions.

filtering in 1D arrY  ,2D array


### math operations.
1. numpy provides fast and efficient , elements wise mathematical operations without using loops.
2. loops are already in the internal c program .
3. mathematical operation between
   - arrays of same shape 
   - array and scalars , scalars have single value.
 
### mathematical operations between different shapes can be done using broadcasting.
   - np.sort(arr)
   - np.sum(arr)
   - np.std(arr)
   - np.mean(arr)



### broadcasting

Broadcasting allows numpy to do math on arrays of different shapes automatically by stretching smaller array to larger one.

#### Rules of broadcasting in numpy
1. Compare shapes from  right to left , right is the last dimension of array shape.
2. Two dimensions are compatible if they are equal or one of them is 1. 
3. 
