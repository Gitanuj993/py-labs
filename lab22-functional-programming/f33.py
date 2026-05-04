#
# using *dict we can take multiple positional arguments
# using **dict we can take multiple keyword arguments

def show(**dic1,var1,var2) :
    print(f"")
    print(dic1)



show(name = "AT" , age = "20"  ) # named arguments are stored a string
type(show(name = "AT" , age = "20"  ))

#