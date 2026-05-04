

def show(id = 1 , name = "AT" , marks = 99) :
    return id,name,marks # if we return more than 1 value then values are return in tuple data type
# as return values are unique thus they are stored in immutable data type



student1 = show() # no parameters
student2 = show(2) # only one parameters
student3 = show(3,"BT") # only two parameters
student4 = show(4,"ST",78) # function call via positonal arguements
student5 = show(name = "DT" , id = 5 , marks = 87) # arguements passed using named arguements

print(f" student1 info is : {student1}")
print(f" student2 info is : {student2}")
print(f" student3 info is : {student3}")
print(f" student4 info is : {student4}")
print(f" student5 info is : {student5}")




