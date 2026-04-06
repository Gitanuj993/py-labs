# Welcome AT
<p> 
objective : control structure in python programming language !
</p>

## introductions to loops

***loops :***  Loops are the mechanism which can executes a code block multiple times , 

#### When to use them ?
- when we have to executes same code statement multiple times


## for-loop
***objective :*** for loop used when we know the total number of iterations or simply if we know how  many times a statement or code block run.

- for-loop sequentially iterate the data or elements


### syntax of data 

``  for <var> in <var or fun> :  ``
### program to print number from 1 to 10

```python
for i in range (11) :
    print(i)
```
### program to print charecters of a string 
```python
name = "Welcome AT "
for i in name :
    print(i)

```

### built in function for  iteration 
- range ( ) 

### range()
```txt
 range(<start>, <end> , <step>)
 This function support total 3 parameters    
 out of which minimum 1 parameter <end> is required ,

 <start> has default parameter of 0
 <step> has default parameter of 1

range supports only integer simple data types and boolean data types ,
More specifically in boolean as 
True turn into 1
False turns into 0

any other data complex data types like dict, list, tuple and set doesn't support range() built-in function


 range is and object of class range() , you can see the documentation of range using 
 ``help(range)``


```
### for - loop using complex data types
```py
str1 = "Hello"
for i in str :
    print(i)

```

```py
list1 = ["Hello" , 1, 3, 5 ]
for i in list1 :
    print(i)

```
```py
tuple1 = [ "Hello", 1,2,3 ]
for i in tuple1 :
    print(i)

```
```py
dict1 = { "name"  : "AT" , "age" : 20 }
for i in dict1:
    print(i)

```




