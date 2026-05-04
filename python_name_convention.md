# Nomenclature of objects and variables in Python programming language  : Clean Code

Every programming languages has variables, functions, objects, classes has a name.
if we can name them randomly as per our creativity then it becomes less readable and less professional.

thus programmers follows a name convention , example of a name convention is : PEP-8

we all know that all identifiers should follow rules , 
different languages has different rules for naming of identifiers.

now if we move to next levels, we observed a need of stable identifier names those are readable and quickly differentiable

Let's see some name conventions in python.

1. variables :
	- varialble names should be clear,  precise and they itseflf tell their purpose,
	- variable names should be in small letters,
	- eg. average , addition, new_node , use_name 
2. Class Names 
	- Names starts with capital letters , like titles in python language.
	- no underscores between two words
	- eg. NameNotFound, UserNotFound , TypeError , Bank, NewUser, RegisterUser
3. objects names
	- objects names should be like variables name, 
	- name in small letters underscore may be used.
	- snake case : snake_case
4.   function names 
	- function names should be in snake case prefer.
	-  name in small letters followed by underscore _
	- function should do only one task.
5. Constants in python
	- python didn't provide constants.
	- but we can user convention that identifiers named in UPPERCASE are constant.
	- eg . PI = 3.14 , MAX_USER = 100



There are three types of styling methods or ways.
1. snake_case
	- words seperated by '_' underscore
	- used in python , c and sometimes in databases.
	-  eg. user_name , total_balance, roll_no , account_no.

2.  camelCase
	- First word lowe case , next word uppercase
	- Used in java , javascript programming languages.
	- eg. userName , javaScript, bankBalance

3. PascalCase or UpperCamelCase
	- Every words's first character is in capital.
	- used in naming conventions of classes.
	- eg. Bank, RegisterUser, PageNotFound , NameError, ValueError
