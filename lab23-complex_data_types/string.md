# Strings in python

1. strings are not primitive 




## ABout strings

`` str1 = "Welcome"``
str1 is a Reference variable takes 8 byte of memeory

## internal representation of string in python

1. string length 
2. Reference counter : count value , initially 0 , kitne variables and iski actually value ko point kiya
3. Type counter : class<str>
4. hash value of actual value
5. padding + utf unicode ( new version ) related to memory
6. iter , takes 1 byte , constant pool 
7. Actual value

Total minimum size ( old version ) : 42 Byte
New version : 


1. we can check address of any variable using id() built-in function
```pycon
var = "1"
print(id(var))

# id() takes only one parameter
```
 ### we see the use of intern and reference value

```pycon
var1 = "AT"
var2 = "AT"
var3 = "AT"
var4 = "AT"
var5 = "A"

print(f" Address of var1 is : {id(var1)}")
print(f" Address of var2 is : {id(var2)}")
print(f" Address of var3 is : {id(var3)}")
print(f" Address of var4 is : {id(var4)}")
print(f" Address of var5 is : {id(var5)}")
 
 # run this program 
 
 # you can see the var 1 to 4 have same address

```
1. we can utilize the object 
2. we do not have to create a new object for a same value each time or for every use
3. memory is occupied for same value
4. Memory is limited thus it is useful to reuse values
5. also applicable to int , float ,  


```pycon
st = "Hello Hi"
rt = "HelloHI"
print(f" Length of {st} is : {len(st)}")
print(f" Length of {rt} is : {len(rt)}")

```

## garbage collection
```pycon
st = "Hello"
print(f"id of {st} is : {id(stc)}")
st = " Hello"
print(f"id of {st} is : {id(stc)}")
st = "Welcome"
print(f"id of {st} is : {id(stc)}")

```
## Strings are immutable data type thus string objects can not be changed 
1. if we want to change or modify the string object then new object is created every time.


## String operators : 9 types or 8 
1. indexing --> 0 to ( size of string )-1 
2. slicing  [ <start> : <end> : <step>]
3. concatenation '+'
4. Repetation '*'
5. in , not in membership
6. for loop 
7. formated string instead of %d,%f like f"a is : {a}"


### Indexing
<p>
String is a sequence of charecters,
each charecter is placed in a position , 
numbering of position starts from the 0 .

indexing : positive start from 0 to valuse > 0 , 0 to (n - 1) from left to right 
Negative indexing : start from  to   value < 0 , -n to -1   from left to right 

right to left is -1 to -n
</p>

### Let's see some examples 
1. We can access the  the elements using index
```pycon
st = "Hello"
print(f" len of st is : {len(st)} ") 

# which charecter is at index 0 
print(f" 0 index is : {st[0]}")
```
1. var[] , index should given in square brackets [<index>] 

``t7.py``


### Slicing of string 
<p>
Dividing string into substring    <br>
or  <br>
Slicing allows substring extraction<br> 
or     <br>
extraction of string from an existing one , called as substring.<br>
</p>

##### Slcing syntax 
``
var[<start> : <end> : <step>]
``
<p>
where <start> , <stop> and <step> are index
likely interpretzation is , start from <start> to <stop> by the difference of <step>

by default <start> is : 0
by default <stop> is : exclusive n as n do not executes 
by default <p> is :  1 
</p>

1. Slicing happens according to indices and indexing
```pycon
var = "python"
print(var[: :]) # by defalut
```




### String concatentation





### String Repetition



### in , not in , membership operators in python

- t13.py
- t12.py


### comment in markdown files
"[//]: # ()"

[//]: # (###  ) here is some examples 
[//]: # () comment



### Formated string

```pycon
name = "AT"

```






