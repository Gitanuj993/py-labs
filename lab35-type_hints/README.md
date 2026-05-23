# Type Hints : Specify variable data types.
<h3>
We know that programming languages like C++ or Java are not dynamicaly typed . <br><br>
in this programming languages we have to specify data type of the variable and data structure.<br><br>
On the other hand programming languages like python which are dynamically typed which do not require data type to declear any variable or implement any data structure.
<br><br>
This dyanamically typed is an advantage in python but this benefits come with the flaws,
as at any time someone can change the data type of any variable.<br><br>

To provide knowledge of which data type should be used python provide type_hints which provide information to the developers.<br>
type_hints are used to validate data type.
</h3>


## Which is the Standard libraray for type_hints
library name is : ``typing`` <br>

## Data Types in python
1. str
2. float
3. int
4. byte
Type_hints also allow to specify data type as of a class
5. <class_name>

## Sample Program to implement Type_hints in variable
```
def sample( name : str , age : int ) :
	print(" Your name is : " , name , " and you are ", age  , " years old. " )

````

## Sample Program to use Type_Hints in python Data Structures
```
def sample_2( name : str , marks : list[int] , dict_1 : dict[str,int] ) :
	print(" your marks is : " , marks )
	print(" dict is " , dict_1 )
```



## Is type_hints strict ?
From the name itself we can observe that this type_hints are used to provide hints, 
type_hints are not strict , and does not give error even
if another data type is used or passed 
type_hint didn't convert data type to 'type_hint' provided.
```
## Program showing ' Whether type_hint is strict or not ? '
def sample( name : str) :
	print(" your name is " , name )
	print(" Type of name : " , type(name))
	
sample("Anuj")
sample(1)
sample(True)
```
### How to check whether the type_hint is strict or not.
1. write an program like above provided.
2. pass arguements in different data types and see the type of variable in the funciton using ' type() '
3. how to can we conclude ?
	- if each time type() prints same data type then we conclude " type_hints " convert to provide data type
	- we may say type_hints is strict if Error occure when different data type is passed or used.
4. From the observation None of the things given in step_3  happend, we can say that 
type_hints is not strict.

## How to use type_hints.
Type_hints provide information to the code Editor. you can see autocorrection and suggestions.

### Syntax of using type_hints
```

variable_name : data_type


```

### In simple data types.
1. string : `` name : str ``
2. integer : `` age : int ``
3. float : `` PI : float ``
4. boolean : `` isBig : bool ``
5. byte : `` kb : byte ``

### in complex data structures or data types.
1. list : `` marks : list[int] ``
2. tuple : `` keys : tuple[str] ``
3. set : `` set_1 : set[int] ``
4. dict : `` dict_1 : dict[str,int] ``



## Can more than one data type hints possible 
yes , we can state there may be more than two data types can be suggested, using '|'
Syntaxt is : `` variable_name : data_type_1 | data_type_2 ``
```pycon

def sample_1( name : str , marks : list[int] | list[float] ) :
	print( " name is : " , name )
	print( " marks is : " , marks )

```
We can also use default values with  using type_hints.
```pycon
def sample_2( name : str  , marks : list[int] | list[float] = None ) :
	print( " name is : " , name )
	print( " marks is : " , marks )
```

## Is we can also sepecify return type of any function
yes , we can do but what would be the syntax ?
syntax is :  `` -> ``
```pycon
def sample_3 ( name : str ) -> str :
	return name
```		



# How to use class name to specify data type or How to declear class_name as data type

```pycon
from pydint import BaseModel 

class Person(BaseModel) :
	name : str
	age : int

# then above class can be defined as

def sample( name : str , age : int , obj_1 : Person ) -> Person :
	obj_1.name = name 
	obj_1.age = age 
	return obj_1

```


## What if we want to specify that variable can be of any data type
To specify variable of any data type  ,
we would use a ``typing`` package 
which can be installed using : `` pip install typing ``

```pycon
from typing import Any 

def sample_4 ( name : Any ) :
	return name 
``` 

## Use cases of Type_hints.
1. used to specify or provide hints of data type in python
2. can be used in API to validate data.
	-  pydint and typing packages align with FastAPI


## use of metadata in the type_hints.

```pycon

from typing import Annotated

def sample( name : Annotated[str,'This is meta data message']) :
	pirnt(name)
```
