# Functions
function is reusable block of code , which is called when needed , we can use same function for different values which requre same functionality

### syntax to declear and define a fucntion in python
`` def <fun_name>() :``
### example of function declearation

```pycon
def function1() : #
    print(" This is function 1")


```
### function calling 
```pycon
def function1() : #
    print(" This is function 1")

function1() # function calling
```

```pycon
def sum(a,b) : # a,b are parameters
    sum = a + b
    return sum

print(sum(1,2)) # 1,2 are arguements
```
### parameters
 > parameters are the variables defined at the time of function declearation
 
### Arguements
> Arguements are the values or values present in the variables provided in the function calling.

## Functions can return a value

1. functions take input through parameters 
2. process the data with code-block in functions
3. provide output via 'return' keyword
 

> In python functions if nothing is return then by default 'None' is return 





## Errors and test understanding

### Type Error 
```pycon

def calculator(a,b,c,d) :
    total = a + b + c + d
    return total
    
res = calculator(1,2,"hii",3)
print(f"result is : {res}")
```
### return multiple values
```pycon
def calculator(a,b,c,d) :
    total = a + b + c + d
    return total
    
res = calculator(1,2,5,3)
print(res)
```
### functions returning multiple values
> returned values return in the form of tuple
```pycon
def calculator(a, b, c, d):
    total = a + b + c + d
    return total


res = calculator(1, 2, 3, 3)
print(res)
```

