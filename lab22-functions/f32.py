#


def show(**dict1) :
    print(f"Type of dict1 is : {type(dict1)}")
    print(dict1)



show(name = "AT" , age = "20"  ) # named arguments are stored a string
print(type(show(name = "AT" , age = "20"  ))) # it didn't print anything , i
# it only call the function
type(show(name = "AT" , age = "20"  )) # it didn't print anything , i
# correct spelling of the arguements is " Arguments "