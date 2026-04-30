# Functions

<p>
Functions is perform a special task which can be reused in the program , 

use of functions supports code reusability
</p>



































## Built-in functions !
```pycon
X = divmod(10,2) 
print(type(x)) # class <tuple> 
# Mutable and immutable objects.
```
## Built-in functions for collection of sequen ce
```pycon
mylist = [ 1 ,3 ,4,5 2 ]
mytuple = ( 1 ,3 ,4,5 2 )
myset = { 1 ,3 ,4,5 2 } 
print(len(mylist))
print(sorted(mylist))
 

```
- >[!Note]
  > #### sorted() is a funciton used to sort the sequence or collection and return list of sorted elements

- >[!Note]
  > #### unordered collection becouse 'set' uses Hashing internally
```
Error : 
Name Error : Wrong variable name called 
Value Error : string to int
Type Error : Wrong type or arguments mismatch

```
```pycon
# Reveresed functions 
list1 = [  10 , 4 ,6 ,5 ] # list is an object
print(reversed(list1))


```
### Range()
```pycon
mylist = [ 1 , 2 ,3,4, 5]
mytuple = ( 1 , 3, 2 , 4 , 5 )
mystring = [ "abc" , 'ABC']

print(min(mylist))
print(min(mytuple))
print(min(mystring))

print(max(mylist))
print(max(mytuple))
print(max

```
### sum() 
```pycon
list1 = [ True , False , False ]
print(list1)
print(f"sum of list 1 is : {sum(list1)}")
```
``
help(sum)
``
- sum() is a function defined by a programmer which is used to , sum is not a addtion operator
### iterable iterator iteration 
```
iterable is a sequence , used in complex data types
```
## String concatenation
```pycon
str = " Welcome " + "AT"
print(str)
```