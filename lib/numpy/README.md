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
6. 

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
    -
3. 2D array : Matrix representation or table
    -
#### Tensor , ndarray , n dimensional array , dimension greater than 3
4. 3D array : collection of 2D array ,
    - 
5. 4D array collection of 3D arrays




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
res = a > 2  3 return a boolean list contaning True and false.



### broadcasting

