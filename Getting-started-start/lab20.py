#llab  :	string functions lets check them out

# here is the example  of string 
string = "Welcome AT"
#lets print or display what you entered
print(string)

# is we change it lts try to do it as string uses indexing from zero , so we can display and have access an elelmetn via index
print(string[0])	 #it will print first character from the string or char which has index 0 in this case output is 'w'

#lets try to print whole string using index slcing or string slicing ,  slicing mean slicing chareacters presnt in the string

print(string[:]) # via this we can print whole string , if we try to print some part of the string  let's do it 
# string[start : stop ] this formula or way used to print whole string
# element or charcters only traversed from start to 1 index less  than stop , like in function

#we can also print' middle charecters
print( string[ 1 : 5 ])
print( string [ 0 : -1 ]) # why can't whole string printed thus  [stop ] stopping index isn't printed'

# we can also skip some elements or traverse whole string consecutively with differnce of more then 1 elements between two results like if  we print
print( f" differnce is 1 : then string looks like : [ {string[ : : 1 ] } ]")
print( f" differnce is 2 : then string looks like : [ {string[ : : 2 ] } ]")
print( f" differnce is 3 : then string looks like : [ {string[ : : 3 ] } ]")
print( string [ : : 2 ]) # it will traverse whole string but with the differnce of two elements


# we can also traverse reverse as via negative indexing like -1 is for last elemetn 
#lets traverse string in reverse
print( f" string in reverse is : [ { print( string[ : : -1 ])} ]") # why output is none
print( f" string in reverse is : [ {  string[ : : -1  ]} ]")

# we can also reverse any string or also check for a pallindrome number 

#lets try to change the element present in the string 
#string[0] = "n" # try this code and see what occure 
print(f" new string after change is : { string } ")

# lets try to reassign a new string to the string variable or string container
string = " new string !"
print(f" new string after change is : { string } ")


# strings are immutable we can not change elements present in it , we create a new string by re using the same variable name , thus this action leads to  deletion of  previous value



