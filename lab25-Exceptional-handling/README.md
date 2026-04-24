# Exception Handling 

<h3> What is an exception ? </h3>

```text
Exception is an event which disrupts normal flow of program execution causes termination of program.
```
```text
try : 
In this code for a code which may cause disruption and termination of the program.

except : 
except block is used to handle or catch the exception gracefully.
if code in try block raise exception then except block catch the error and terminate the termination of execution.

```
Types of Errors 
### Base exception super class
Base exception has three subclasses
1. Unbound local error class
2. Arithmetic error class 
   - ZeroDivisionError class
   - 
3. look-up error class
4. Name Error class
5. Attribute Error class
6. Key Error class
7. Index Error class
8. Value Error class
9. Indentation Error class
10. Type Error class
11. Syntax Error { This is an Error grammatical Error


If an exception is raised , first python or python interpreter search for try and except block if not found then exception is handled by python itself,

if we handle the exception then program will run normally as except is neutralized 
else python take it on itself and determine exception type and then abnormally terminate the program