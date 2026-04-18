### Set 


1. Set is unordered collection of elements.
2. Set is mutable complex data type 
3. Set store elements using hashing 
4. set contains only distinct elements
5. 



### Set allows 
```markdown
1. int
2. flaot
3. string
4. Boolean

```
### Set do not allow : Unhashable types

> Immutable types are hashable in list

> Mutable type objects are not hashable , eg. Lists , Sets

> Set of set or set of list or set of any complex data type is not possible 
 
 

### Operations of set 

1. union 
2. intersection
3. difference
4. Symmetric Difference


### Sets and comparison operators

>``what if we perform comparison operators on sets``prompt on chatGPT 

###  Set operation
```markdown
 Subset , Superset , Proper subset and Proper superset

set 1 : { 1 , 2 ,3 ,4 ,5 }
set 2 : {  1,2,3 }

if all elements of a set (say A ) present in another set ( say B )
then we can say that  set A would be subset of set B and 
Set B would become superset of set A

In above case set 1 be the superset of set2  , set1 > set2 and set2 < set1
```
### proper set
> proper subset is a subset which contains upto total  elemets of the compared set , 

> if equal set setA == setB , if all the elements of set A present in the set B

> != Not equal , set A != set B , set A and set B do not have same number of elements and same elements

> proper subset , 
> If a set  may  contain all the elements of compared set ( another set ) and may not contain all elements 



#### Global functions of set 

1. len()
2. max() for comparable
3. min()
4. sum() of numeric elements
5. sorted()


### Functions for set class

1. .add(x) : adds an elements into the set , add one  element
2. .update(<iterable>) #no parameters , add many elements
3. .remove(x)
4. .pop() : remove random element , do not throw errro
5. .discard(x) : it takes 1 arg ,  , and doesn't raise any error if element not found
6. .clear() : it will clear all the elements from the set

### Set operations between two sets , s1 and s2
1. s1.union(s2)
2. s1.intersection(s2)
3. s1.symmetric_difference(s2)
4. s1.difference(s2)
> functions are slower than operators

> elemnts which are already in the set will be ignored
> 
#### check and copmare between two sets 
> s1 and s2
1. s1.issubset(s2)
2. s1.issuperset(s2)
3. s1.isdisjoint(s2)


### Frozen set 
> Frozenset are the immutable set which is defined in <class 'frozenset'> all the objects are immutable thus hashable,

> Thus we can use it inside a set like a set inside a set or nested set or set of set 
 
