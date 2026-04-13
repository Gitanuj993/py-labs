"""
Welcome AT

aim : To take input from the user and To display the output
pre-requesite :
level : "level 0"

"""
import datetime

#let's take input from the user for our task
name = str(input("Enter your name : "))
year = int(input("Enter your birth year : "))
gender = str(input("Enter your gender : "))
now = datetime.datetime.now().year
age = now - year
schema = " "

#let's adds something into it like  year old is not smooth
if (age < 0) :
    age = 0


if ( age> 0 and age <3) :
    schema = "baby"
elif ( age >3 and age<17) :
    schema = " boy"
elif (age > 18 and age <28) :
    schema = " young"
elif ( age > 28 and age < 45) :
    schema = " adults"
else :
    schema = " elder"

# Now let's display what we collected from the user
print(f" Your are {name} , {age}  years {schema}  {gender}, Wish you meaningfull and sorted life-style ! ")