"""
Welcome AT
module : pyjokes 
aim :	to use pyjokes !
procedure :	To use pyjokes on our system, first we install pyjokes module via 
>>	pip install pyjokes
after that we can use pyjokes module and get a joke using get_joke()
"""
import pyjokes
print("joke 1 :" , end = " ")
print(pyjokes.get_joke())
print(" joke 2 :" , end = " ")
print(pyjokes.get_joke(language='en' ,category='neutral'))
#print(" jokes :" , end = " ")
jokes = pyjokes.get_jokes()
#print(jokes)


"""
for joke in jokes :
	print(joke)


#you can use them 

"""
#lets print the available    supported language 
#print(f" supported lang :	{pyjokes.get_languages()}")
#print(pyjokes.get_languages())

# you will see different jokes each time you run code !
