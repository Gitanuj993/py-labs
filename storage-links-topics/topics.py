

#INTRODUCTION TO FUNCTION          _________________________________(07/04/2026)
#BUILT IN FUNCTION 

   #  1.USER DEFINED FUNCTION 
   #  2.FUNCTION RETURN VALUE
#PARAMETERIZED & ARGUMENTS 
#TYPES OF ARGUMENTS 
#SCOPES
#   -GLOBEL   -(VARIABLE DECLARED OUTSIDE THE FUNCTION DEFINITION)
#   -LOCAL    -(VARIABLE DECLARED INSIDE  THE FUNCTION DEFINITION)
#   -NON-LOCAL 
#   -NON-GLOBAL
# RECURSION 
# LEMDA FUNCTIONS 
# HIGHER ORDER FUNCTION 

#---------------------------------------(08/04/26)---------------------

#MAKING FUNCTION WITH MULTIPLE VALUES (LIKE)
# TYPES PF ARGUMENTS AND PARAMETERS(PLACEHOLDER)
#     -1. Positional Arguments
#                        ~(Values are assigned to parameters in the order they are passed.
#                         Must be passed in the correct order.)~
#    -2. Keyword Arguments
#                        ~(Parameters are specified by name, so order doesn’t matter.
#                         Improves readability.)~
#
#    -3. Default Arguments
#                        ~(Parameters have default values if no value is provided.
#                         Useful for optional parameters.)~
#   
#    -4. Variable-Length Positional Arguments (*args)
#                        ~(Allows passing any number of positional arguments.
#                          Received as a tuple.)~
#
#    -5. Variable-Length Keyword Arguments (**kwargs)
#                        ~(Allows passing any number of keyword arguments.
#                          Received as a dictionary.)~
"""  Argument Type	         Syntax	Stored As	         Example
Positional	func(a, b)	     |  Variables in order	             greet("Alice", 25)
Keyword	func(b=2, a=1)	     | Variables by name	             greet(age=25, name="Alice")
Default	def func(a=10)	     | Variable with default	          greet("Bob")
*args	def func(*args)	     | Tuple	                         add_numbers(1,2,3)
**kwargs	def func(**kwargs)  |Dictionary	                      print_info(name="Alice") """
#               
#-----------------------------------(09/04/26)--------------------
#
# SCOPE
#              -(IT DETERMINES WHERE THE VARIABLES CAN BE EXCESSED OR MODIFY IN A PROGRAM)
#
#  [NOTE]: WE ARE NOT RUN CODE BEFORE DECLARING / WE ARE NOT USING VARIABLE BEFORE DECLARING    
#        : ALL FUNCTIPON DEFINITION STORE AS A """ STACK """
#        : FIRST PRIORITY IS FUNCTION LOCAL VRIABLE THEN GLOBAL VARIABLE IN FUNCTION,THE DEFINITION IS STORE
#          AS A STACK MEANS THE FUNCTION RUN """ AS ONE BY ONE""""
#   ***  : STACK HAS A DIFFERENT MEMORY ALLOCATION IN PYTHON (IMP)
#        : IF WE USE THE MULTIPLE VARIABLES WITH MULTIPLE VALUES IN FUNCTION THEN GLOBAL KEYWORD 
#          ACCESS THE VARIABLES WHICH IS AFTER THE EXECUTION OF LINE CODE 
#                    -EX_______
#                          A=10
#                          DEF SHOW():
#                                GLOBAL A    <-----------------------------<
#                                PRINT(A)                                  |  
#                                A="SDITS"   <---- MODIFIED A---->         |
#                               PRINT("INSIDE THE FUNCT",A)                |
#                           SHOW()                                         |
#                           PRINT("OUTSIDE THE FUNCT",A)                   |
#                                       """"IT ACCESS THE MODIFY VARIABLE "A" ---> WHICH IS SDITS"""
#
# NESTED FUNCTION 
# RECURSION  
# _______________________________________________(10/04/26)_______________          
# 
#  lemda function
#     -IT IS A SMALL ANONYMOUS FUNCTION DEFINED USING LEMBDA KEYWORD 
#     -IT CAN TAKE ANY NUMBERS OF ARGUMENTS AND PARAMETERS  
#     -IT CAN HAVE ONLY ONE EXPRESSION 
#     -IT RETURNS THE RESULT OF EXPRESSION
#     -IT PROVIDES A COMPACT WAY OF WRITING IN SINGLE WAY
#     -     SYNTAX___
#                        X=LAMBDA: 
# 
# 
# [NOTE]:[IMP]
#              -------------HIGHER ORDER FUNCTION-------------
#          
# 
# ________________________________________________________________(11/04/26)
# 
#  OBJECT ORIENTED PRIOGRAMING 
# PYCHARM (HAVE OWN INTERPRETER ) 
#       -CLASS PATH
#       -ENVIRONMENT VARIABLE( PATH OF DIFFERENT PYTHON WITH DIFF VERSION WITH OWN PYCHARM/JDK/MYSQL/ ETC)
#       -DIVIDE HARD DRIVEIN DIFF PARTS      
# COMPLEX DATA TYPE  (class)
#     -string (str)
#     -list
#     -tuple
#     =set
#     -dictionary
#
#  sting
#       -STRING OBJECTIS IMMUTABLE IN  NATURE 
#       
# STRING OPERATOR
#       -INDEXING 
#       -CONCATINATION 
#       =REPETITION  *
#       -IN , NOT IN MEMBERSHIP
#       -FOR LOOP
#       -FORMATED STRING INSTEAD OF %D, %F
# 
#    --INDEXING 
#           -IT IS A SEQUENCE OF CHARACTER WHICH IS STORED IN INDEX(WHICH STORES THE EACH CHARACTER)
#           -LEFT TO RIGHT (-N TO -1)
#           -RIGHT TO LEFT (-1TO -N)
#           -SHOWS INDEX ERROR 
#           -LEN() IS GLOBAL FUNCTION 
#           -SLICING
#    --SLICING 
#           -DIVIDING THE STRING INTO SUBSTRING 
#           -EXTRACT SUBSTRING FROM MAIN STRING 
#           - SYNTAX ___   STR[::]
#                       STR[START:STOP:STEP]
#                             |
#                          (INCLUSIVE)(EXCLUSIVE)(STEP)
#         -BY DEFAULT VALUES     
#              -<START> 0
#              -<STOP> N (DUE TO EXCLUSIVE)
#              -<STEP> 1
#         -string concatination
#                EX     st=str1+str2
#         
#        -string METHODS /MANIPULATION 
#             -1.CAPATALIZE()
#             -2.LOWER() 
#             -3.UPPER()
#             -4.SWAPCASE()   CONVERTS LOWER TO UPPER / UPPER TO LOWER
#             -5.TITLE()    
#             -6.ISLOWER()
#             -7.REPLACE()  IT CREATES NEW OBJECT WHEN REPLACED 
#             -8.ISDIGIT()
#             -9.ISDECIMAL() 
#             -10.ISALPHA()
#             -11.ISALNUM()
#             -12.COUNT()
#             -13.AT.COUNT(VARIABLE TO SEARCH,START,END)
#             -14.ISNUMERIC() 
#             -15.FIND() PROVIDES THE INDEX OF SUB-STRING OF STARTING LETTER / CHECK THE FIRST CHARACTER OF
#                            SUB-STRING IF FOUND  (--IF NOT FIND SUB-STRING IT RETURNS THE -1)
#             -16.RFIND() IT STARTS WITH FORWARD(SEARCHING) BUT GIVES THE REVERSE ORDER INDEXING
#                           REVERSE ORDER FIND / LAST OCCURANCE OF THE SUB-STRING
#             -17.INDEX()  IT GIVES INDEX VALUE / IT USES ONLY INTEGER OR BOOL
#             -18.STARTSWITH()/ENDSWITH()
#             -19.SPLIT()   SPLIT THE STRING WHEN SPACE OCCURE/ SPLIT(STRING / CHAR)
#             -20.REMOVE(PREFIX/SUFFIX)
#                     -REMOVEPREFIX()
#                     -REMOVESUFFIX()
#            -21.JOIN()
#                    SYNTAX__    
#                           STR=STR2.JOIN(STR1) 
# 
# _____________________________________(13/04/26)
# 
#  -LIST -
#          -LIST IS USE TO STORE THE HETROGENOUS(STORE SAME DIFFERENT TYPE OF DATA) TYPE OF DATA
#          -IN LIST HOMOGENOUS IS ALSO DEFINED AS DEFAULT
#          -PYTHON SUPPORT ARRAY AS A LIST 
#          -PYHTON DOES'NT SUPPORT ARRAY
#          -TT FIRST CREATED A REFERENCE VARIABLE 
#          -ASSIGN THE VARIABLE
#          -LIST IS BUILT IN CLASS RETURN IN C,C++ LANGUAGE(DUE TO C,C++ MALKE THE PYTHON INTERPRETER)
#          -STORE THE 'n' NUMBER OF ELEMENIS 
#          -LIST IS OEDERED(STORE AS A USER IN INSERTION TO STORE) SEQUENCE 
#          -LIST IS MUTABLE IN NATURE 
#          -LIST CAN MANY / ANYTYPE NUMBER OF ELEMENTS
#          -IF WE ADD VARIABLE IN LIST THEN IT ALWAYS THE STORE AT INDEX AND IT CAN SHIFT THE PREVIOUS 
#              ELEMNENT AND THE LIST WILL INCREASES
#          -LIST IS DYNAMIC IN NATURE  
#           
#   [NOTE]: CREATING DIFFERENT LIST THROUGH
#          list
#               Empty list: ~56 bytes.
#               Each element reference adds 8 bytes (on 64-bit).
# 
#          -connstructer
#                      -we can create an object of list through the constructer 
#                      -list contructer is a special type of method 
#                      -it is function(with no argumen and argument)
#                      -it can take as a complex data type
#                      -it convcerts another iterable into list 
#                      
#         -list comprehension
#                      -create new object for list  
#                      -IT IS USED TO MODIFIED THE LIS WHICH IS CREATED AND NOT MODIFIED PREVIOUS
#        -MULTI-DIMENSIONAL LIST 
#                      -LIST IN LIST 
#                      -list contain list,tuple,set only
#        -list
#             -indexing
#             -slicing
#             -list comarison operation
#             -list concatination (only list and list can concatinate)
#             -repetition
#             -membership operator 
#    ___________________________________________________(15/04/26)
#       -list comparison 
#             -1.lexo-graphical 
#             -2.equality 
#             -3.IN-equality
#        -COMPARISION OF LIST 
#      -global function 
#           -sorted()
#           -reversed()
#           -next()
#           -any()
#           -alt()
#           -enumerate()
#           -zip()
#           -append()
#           -extend()
#           -insert()
#           -pop()
#           -clear()  it clear only objects 
#           -delete()  it clear all reference variable with object 
#           -index()
#           -min()
#           -max()
#           -count() RETURNS THE REPETITION OF PARTICULAR ELEMENNT 
#           -SUM() 
#           -LEN()
#           -ID()
#           -SORT()
#           -
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#


