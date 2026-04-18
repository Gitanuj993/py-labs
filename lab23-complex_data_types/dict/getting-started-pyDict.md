# Python Dictionary 
```txt
dictionary is collection of key value-pair
from whick key are of immutable data type and values can be changed 
```
## Dictionary objects in python
1. key value pair enclosed in { } curly bracket
2. using dict() default parameter
3. using dict(<mapping>)
4. using dic(<iterable>) : [ (101,"a"),(102,"b")]




## Dict comprehension

```python
mydict = { x : x for x in range(5)}

```
### additonal
1.  We can use variable in the place of value : either type of list , tuple , set
2. 


### Accessing value from a dict using key
```python
dict1 = { 1 : "A" , 2 : "B" , "C" : 3}
print(dict1[1])
print(dict1[2])
print(dict1["C"])
```

## Comparison operation on python dict

1. ==
2. != 

## Global functions 
`` my_dict1 = { 1 : "A" , 2 : "B" , "C" : 3}``
1. len(my_dict1) : return rate 
2. any() : Truthy OR gate type
3. all() : Falsy AND gate type
4. enumerate()
5. zip()

> using any(dict1.values())

## Built in function of dict in
#### See data in the dict
1. my_dict1.values()
2. my_dict1.keys()
3. my_dict1.items()
#### return data from the dict
1. my_dict1.get(x) : return values of key x , return None if key not found
2. my_dict1.setdefault(<key> , <value>)
3. my_dict1.pop(x) : 
4. my_dict1.popitem() : one item removed from the dictionary

#### update the dict
1. my_dict1.update(<x>) : x : list of tuples( only two elements) , tuple of tuples ( only two elements) 
2. mu_dict.fromkeys()

### Nested Dictionary
> dictionary inside dict is termed as nested dictionary

1. values can be dictionary
2. keys can not has dictionary as dict is of immutable data type , part of dict keys are immutable